import re
import os
from PIL import Image, ImageDraw, ImageFont, ImageSequence
import sys

dir_path = os.path.dirname(os.path.abspath(__file__))

def remove_emojis(text):
    # Regular expression for matching emojis
    emoji_pattern = re.compile(
        '['
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
        '\U000024C2-\U0001F251'
        ']+', flags=re.UNICODE)
    return emoji_pattern.sub(r'', text).strip()

def get_upper(somedata):
    '''
    Handle Python 2/3 differences in argv encoding
    '''
    result = ''
    try:
        # Decode and remove emojis
        cleaned_data = remove_emojis(somedata.decode("utf-8"))
        result = cleaned_data.upper()
    except AttributeError:  # Handle Python 3 strings
        cleaned_data = remove_emojis(somedata)
        result = cleaned_data.upper()
    return result

def get_lower(somedata):
    '''
    Handle Python 2/3 differences in argv encoding
    '''
    result = ''
    try:
        # Decode and remove emojis
        cleaned_data = remove_emojis(somedata.decode("utf-8"))
        result = cleaned_data.lower()
    except AttributeError:  # Handle Python 3 strings
        cleaned_data = remove_emojis(somedata)
        result = cleaned_data.lower()
    return result

def getsize(font, text):
    left, top, right, bottom = font.getbbox(text)
    return right - left, bottom - top
 
def make_meme(topString, bottomString, filename):
    # Open the image
    original = Image.open(filename)
    
    if original.format in ['GIF', 'WEBP']:
        frames = []
        for frame in ImageSequence.Iterator(original):
            img = frame.copy().convert("RGBA")
            process_frame(img, topString, bottomString)
            frames.append(img)
        
        if original.format == 'WEBP':
            frames[0].save("temp.webp", save_all=True, append_images=frames[1:], loop=0, duration=original.info['duration'])
            print("file save in temp.webp")
        else:
            frames[0].save("temp.gif", save_all=True, append_images=frames[1:], loop=0)
            print("file save in temp.gif")
    else:
        img = original
        process_frame(img, topString, bottomString)
        img.save("temp." + )
        print(f'file save in temp.{original.format.lower()}')

def process_frame(img, topString, bottomString):
    imageSize = img.size

    # Find the biggest font size that works
    fontSize = int(imageSize[1] / 7.5)
    font = ImageFont.truetype(f"{dir_path}/Fonts/impact.ttf", fontSize)
    topTextSize = getsize(font, topString)
    bottomTextSize = getsize(font, bottomString)
    while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
        fontSize -= 1
        font = ImageFont.truetype(f"{dir_path}/Fonts/impact.ttf", fontSize)
        topTextSize = getsize(font, topString)
        bottomTextSize = getsize(font, bottomString)

    # Find top centered position for top text
    topTextPositionX = (imageSize[0] / 2) - (topTextSize[0] / 2)
    topTextPositionY = 0
    topTextPosition = (topTextPositionX, topTextPositionY)

    # Find bottom centered position for bottom text
    bottomTextPositionX = (imageSize[0] / 2) - (bottomTextSize[0] / 2)
    padding = imageSize[1] * 0.07
    bottomTextPositionY = imageSize[1] - bottomTextSize[1] - padding
    bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

    draw = ImageDraw.Draw(img)

    # Draw outlines
    outlineRange = int(fontSize / 15)
    for x in range(-outlineRange, outlineRange + 1):
        for y in range(-outlineRange, outlineRange + 1):
            draw.text((topTextPosition[0] + x, topTextPosition[1] + y), topString, (0, 0, 0), font=font)
            draw.text((bottomTextPosition[0] + x, bottomTextPosition[1] + y), bottomString, (0, 0, 0), font=font)

    draw.text(topTextPosition, topString, (255, 255, 255), font=font)
    draw.text(bottomTextPosition, bottomString, (255, 255, 255), font=font)

if __name__ == '__main__':
    args_len = len(sys.argv)
    topString = ''
    meme = 'standard.jpg'

    if args_len == 1:
        # No args except the launch of the script
        print('args plz')

    elif args_len == 2:
        # Only one argument, use standard meme
        bottomString = get_upper(sys.argv[-1])

    elif args_len == 3:
        # Args give meme and one line
        bottomString = get_upper(sys.argv[-1])
        meme = sys.argv[1]

    elif args_len == 4:
        # Args give meme and two lines
        topString = get_upper(sys.argv[-2])
        bottomString = get_upper(sys.argv[-1])
        meme = sys.argv[1]
    else:
        # Too many args
        print('too many args')
    
    filename = str(meme)
    make_meme(topString, bottomString, filename)
    
