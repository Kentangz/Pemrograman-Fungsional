from PIL import Image

# TODO 1 : Buka gambar
cat_stare = Image.open(r'Modul6\Codelab\images\cat stare.jpg')
cat_elgato = Image.open(r'Modul6\Codelab\images\cat el gato.jpg')

# TODO 2 : Konversi overlay ke mode RGB (menghilangkan alpha channel)
overlay_image = cat_elgato.convert('RGB')  

# TODO 3 : (Optional) Perkecil ukuran gambar overlay menggunakan resize()
overlay_image1 = overlay_image.resize((100, 100))

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background

x_center = (cat_stare.width - overlay_image1.width) // 2
y_center = (cat_stare.height - overlay_image1.height) // 2


cat_stare.paste(overlay_image1, (x_center, y_center))

# TODO 5 : Simpan gambar hasil edit
output_path = r'C:\Users\Lenovo\VSC\GitHub\Pemrograman-Fungsional\Modul6\Codelab\images\codelab3.jpg'
cat_stare.save(output_path)

# TODO 6 : Tampilkan gambar hasil edit
cat_stare.show()

print(f"Gambar hasil overlay berhasil disimpan: {output_path}")

