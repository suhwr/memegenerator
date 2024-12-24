# Python Meme Generator

## Introduction
Ini adalah Meme-Generator untuk Python, menggunakan PIL (dengan FreeType). Meme ini dapat memberi keterangan di bagian atas dan bawah gambar.

## Requirements
Untuk menggunakan Meme Generator, Anda harus memiliki Python (tentu saja!) dan PIL (Python Image Library) dengan FreeType yang berfungsi.

## Installation

Unduh atau fork atau apa pun Repositori ini, ia memiliki semua yang Anda butuhkan. Ia bahkan dilengkapi dengan beberapa templat meme untuk membantu Anda memulai.

### INSTALL PILLOW 
```bash
  pip install pillow
```

## Example
```python
from memegenerator import memegenerator

print(memegenerator(".path_to_file/example.jpg", "top text 😁", "bottom text 😁"))
#output: "{DIRNAME}/meme_example.jpg"
```

### FILE SUPPORT 
• png

• jpg

• webp + animation

• gif 

## API Usage

Memegenerator juga dapat digunakan sebagai pustaka impor. Modul memegenerator memiliki satu metode tingkat atas, `memegenerator(filename, topString, bottomString)`. Argumen pertama adalah nama berkas lengkap dari gambar sumber yang akan digunakan. Dua argumen selanjutnya menentukan teks yang akan muncul pada gambar.
File dengan nama 'meme_{basename}' akan ditempatkan di direktori saat ini. Jika tidak ada teks yang diperlukan untuk bagian atas (atau bawah), masukkan string kosong.

## Notes

Jangan ragu untuk menggunakan, mengembangkan dan meningkatkan, serta kirimkan Pull Request kepada saya jika menurut Anda ada sesuatu yang hebat yang perlu disertakan di sini.
