from PIL import Image

# Open the uploaded image
image_path = "/mnt/data/WhatsApp Image 2024-01-22 at 10.28.11 PM (1).jpeg"
image = Image.open(image_path)

# Display the image
image.show()
