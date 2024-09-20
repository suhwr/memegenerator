# Python Meme Generator

## Introduction
Ini adalah Meme-Generator untuk Python, menggunakan PIL (dengan FreeType). Meme ini dapat memberi keterangan di bagian atas dan bawah gambar.

## Requirements
Untuk menggunakan Meme Generator, Anda harus memiliki Python (tentu saja!) dan PIL (Python Image Library) dengan FreeType yang berfungsi.

## Installation

Unduh atau fork atau apa pun Repositori ini, ia memiliki semua yang Anda butuhkan. Ia bahkan dilengkapi dengan beberapa templat meme untuk membantu Anda memulai.

## Command-Line Usage

Memegenerator.py menggunakan gambar dengan ekstensi `.jpg, .png, .webp, .gif` dalam folder yang sama.

Jadi, dengan asumsi skrip tersebut menggunakan `~/dev/memegenerator/`, semua berkas gambar juga harus ada di sana.

Misalnya: Jika Anda ingin membuat Meme Anak Sukses, Anda akan meletakkan file `successkid.jpg` (dengan templat kosong) ke dalam `~/dev/memegenerator/`. Sebenarnya tidak terlalu sulit.

Jika Anda ingin menggunakan Generator dari Command Line, Anda hanya memasukkan `python memegenerator.py successkid "Top Caption" "Bottom Caption"`, tekan Enter, dan itu akan menghasilkan `temp.<ext>` dan menyimpannya ke direktori ini

The `temp.<extension>` will have the same size as the template you put in. It will be overwritten the next time you use the Generator, so rename or move it, if you want to keep it.
The `temp.<extension>` will have the same size as the template you put in. It will be overwritten the next time you use the Generator, so rename or move it, if you want to keep it.

`temp.<extension>` akan memiliki ukuran yang sama dengan templat yang Anda masukkan. Templat tersebut akan ditimpa saat Anda menggunakan Generator berikutnya, jadi ganti nama atau pindahkan templat tersebut jika Anda ingin menyimpannya.


### INSTALL PILLOW 
```bash
  pip install pillow
```

### FILE SUPPORT 
• png
• jpg
• webp (animation support)
• gif +

### Arguments

Generator mengambil beberapa argumen dan memperlakukannya sebagai berikut:

#### Two Arguments
``` bash
$ python memegenerator.py filename.png "Lorem Ipsum"
```

#### Three Arguments
``` bash
$ python memegenerator.py filename.gif "Lorem Ipsum" "Dolor Sit"
```
Ini menggunakan Argumen kedua sebagai keterangan atas, dan yang ketiga sebagai keterangan bawah.

Memegenerator tidak mendukung lebih dari tiga Argumen saat ini.

## API Usage

Memegenerator juga dapat digunakan sebagai pustaka impor. Modul memegenerator memiliki satu metode tingkat atas, `make_meme(topString, bottomString, filename)`. Dua argumen pertama menentukan teks yang akan muncul pada gambar. Argumen terakhir adalah nama berkas lengkap dari gambar sumber yang akan digunakan. File dengan nama 'temp.<extension>' akan ditempatkan di direktori saat ini. Jika tidak ada teks yang diperlukan untuk bagian atas (atau bawah), masukkan string kosong.

## Notes

Jangan ragu untuk menggunakan, mengembangkan dan meningkatkan, serta kirimkan Pull Request kepada saya jika menurut Anda ada sesuatu yang hebat yang perlu disertakan di sini.
