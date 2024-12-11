from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

img = Image.open(r'Modul6/Codelab/images/cat el gato.jpg')
filtered_img = img.filter(ImageFilter.CONTOUR)
rotated_img = img.rotate(45)

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(filtered_img)
plt.title("Filtered: CONTOUR")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(img)
plt.title("Annotated Image")
plt.axis("off")
plt.text(10, 50, "CAT CAT CAT", fontsize=12, color="yellow", bbox=dict(facecolor="red", alpha=0.5))
plt.annotate(
    "El gato",
    xy=(200, 200), xycoords="data",
    xytext=(400, 400), textcoords="data",
    arrowprops=dict(arrowstyle="->", lw=2, color="blue"),
    fontsize=10, color="blue"
)

plt.subplot(2, 2, 4)
plt.imshow(rotated_img)
plt.title("Rotated Image")
plt.axis("off")





plt.show()

# from PIL import Image, ImageFilter, ImageDraw

# # Buka gambar
# img = Image.open(r'C:\Users\Lenovo\VSC\GitHub\Pemrograman-Fungsional\Modul6\Codelab\images\cat el gato.jpg')

# # Terapkan filter CONTOUR
# filtered_img = img.filter(ImageFilter.CONTOUR)

# # Putar gambar 45 derajat
# rotated_img = img.rotate(45)

# # Tampilkan gambar asli
# img.show(title="Original Image")

# # Tampilkan gambar dengan filter CONTOUR
# filtered_img.show(title="Filtered: CONTOUR")

# # Menambahkan anotasi pada gambar
# annotated_img = img.copy()
# draw = ImageDraw.Draw(annotated_img)
# draw.text((10, 50), "CAT CAT CAT", fill="yellow") 