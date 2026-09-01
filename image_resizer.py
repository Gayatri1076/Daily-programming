from PIL import Image

image_name = input("Enter image name: ")
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))

try:
    image = Image.open(image_name)

    resized = image.resize((width, height))

    resized.save("resized_image.jpg")

    print("Image resized successfully!")
    print("Saved as: resized_image.jpg")

except FileNotFoundError:
    print("Image not found!")