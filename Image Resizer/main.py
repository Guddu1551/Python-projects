from PIL import Image

img = Image.open('Ace.jpg')

print(f"Current size : {img.size}")

resize_img = img.resize((5158,6448))

resize_img.save('ace_resize.jpg')