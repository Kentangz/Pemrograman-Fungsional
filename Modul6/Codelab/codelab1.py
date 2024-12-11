from PIL import Image, ImageFilter


img = Image.open(r'Modul6\Codelab\images\Maba-UMM-Sambut-Muktamar.jpg')

# Terapkan filter CONTOUR
fil2 = img.filter(ImageFilter.BLUR)
filtered_img = fil2.filter(ImageFilter.CONTOUR)

# Tampilkan gambar asli (Before)
print("Before:")
img.show()

# Tampilkan gambar hasil filter (After)
print("After:")
filtered_img.show()

filtered_img.save(r'Modul6/Codelab/images/codelab1.jpg')