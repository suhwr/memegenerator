from PIL import Image, ImageDraw, ImageFont, ImageSequence
from os import path
from re import match


__dirname = path.dirname(path.abspath(__file__))


def is_emoji(char):
  return match(
    r'['
    '\U0001F600-\U0001F64F'  # Emoticons
    '\U0001F300-\U0001F5FF'  # Symbols & Pictographs
    '\U0001F680-\U0001F6FF'  # Transport & Map Symbols
    '\U0001F700-\U0001F77F'  # Alchemical Symbols
    '\U0001F780-\U0001F7FF'  # Geometric Shapes Extended
    '\U0001F800-\U0001F8FF'  # Supplemental Arrows-C
    '\U0001F900-\U0001F9FF'  # Supplemental Symbols and Pictographs
    '\U0001FA00-\U0001FA6F'  # Chess Symbols
    '\U0001FA70-\U0001FAFF'  # Symbols and Pictographs Extended-A
    '\U00002702-\U000027B0'  # Dingbats
    '\U000024C2-\U0001F251'  # Enclosed Characters
    ']+', char)

def getsize(font, text):
  left, top, right, bottom = font.getbbox(text)
  return right - left, bottom - top


def process_frame(img, topString, bottomString):
  imageSize = img.size
  fontPath = path.join(__dirname, 'Fonts', 'impact.ttf')
  emojiFontPath = path.join(__dirname, 'Fonts', 'NotoColorEmoji.ttf')

  fontSize = int(imageSize[1] / 7.5)
  font = ImageFont.truetype(fontPath, fontSize)
  emojiFont = ImageFont.truetype(emojiFontPath, 109)

  def calculate_text_size(text):
    width, height = 0, 0
    for char in text:
      char_width, char_height = getsize(font, char)
      width += char_width
      height = max(height, char_height)
    return width, height

  topTextSize = calculate_text_size(topString)
  bottomTextSize = calculate_text_size(bottomString)
  while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
    fontSize -= 1
    font = ImageFont.truetype(fontPath, fontSize)
    topTextSize = calculate_text_size(topString)
    bottomTextSize = calculate_text_size(bottomString)

  topTextPosition = ((imageSize[0] - topTextSize[0]) / 2, 8)
  bottomTextPosition = ((imageSize[0] - bottomTextSize[0]) / 2, imageSize[1] - bottomTextSize[1] - imageSize[1] * 0.07)

  draw = ImageDraw.Draw(img)
  outlineRange = int(fontSize / 20)

  def draw_text_with_outline(draw, position, text):
    x, y = position
    cx, cy = x, y

    for char in text:
      if not is_emoji(char):
        for ox in range(-outlineRange, outlineRange + 1):
          for oy in range(-outlineRange, outlineRange + 1):
            draw.text((cx + ox, cy + oy), char, fill=(0, 0, 0), font=font)
        cx += getsize(font, char)[0]

    cx, cy = x, y
    for char in text:
      if is_emoji(char):
        current_font = emojiFont
        char_width, char_height = getsize(current_font, char)
        emoji_image = Image.new("RGBA", (char_width, char_height))
        emoji_draw = ImageDraw.Draw(emoji_image)
        emoji_draw.text((0, 0), char, font=current_font, fill=(255, 255, 255), embedded_color=True)
        emoji_image = emoji_image.resize((fontSize, fontSize), Image.Resampling.LANCZOS)
        img.paste(emoji_image, (int(cx), int(cy) + 5), emoji_image)
        cx += fontSize
      else:
        draw.text((cx, cy), char, fill=(255, 255, 255), font=font)
        cx += getsize(font, char)[0]
  
  draw_text_with_outline(draw, topTextPosition, topString)
  draw_text_with_outline(draw, bottomTextPosition, bottomString)

def memegenerator(inputPath, topString = "", bottomString = ""):
  topString = topString.upper()
  bottomString = bottomString.upper()
  original = Image.open(inputPath)
  outputPath = path.join(__dirname, f"meme_{path.basename(inputPath)}")
  
  if original.format in ['GIF', 'WEBP']:
    frames = []
    for frame in ImageSequence.Iterator(original):
      img = frame.copy().convert("RGBA")
      process_frame(img, topString, bottomString)
      frames.append(img)
    
    if original.format == 'WEBP':
      frames[0].save(outputPath, save_all=True, append_images=frames[1:], loop=0, duration=original.info['duration'])
    else:
      frames[0].save(outputPath, save_all=True, append_images=frames[1:], loop=0)
  else:
    img = original
    process_frame(img, topString, bottomString)
    img.save(outputPath)
  
  return outputPath

if __name__ == '__main__':
  print(memegenerator("successkid.jpg","top text 😁"))
