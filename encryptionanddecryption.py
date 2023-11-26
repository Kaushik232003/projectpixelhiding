from PIL import Image
import os

def encrypt(image_path, secret_message, output_path):
    # Open the image
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Convert the secret message to binary
    binary_secret = ''.join(format(ord(char), '08b') for char in secret_message)

    # Ensure the image can hide the secret message
    if len(binary_secret) > len(pixels):
        raise ValueError("Error: Message is too long to be hidden in the image.")

    # Hide the secret message in the image
    encrypted_pixels = []
    for i in range(len(binary_secret)):
        pixel = list(pixels[i])
        pixel[-1] = int(binary_secret[i])
        encrypted_pixels.append(tuple(pixel))

    # Update the image with the encrypted pixels
    img.putdata(encrypted_pixels)
    img.save(output_path)

def decrypt(image_path):
    # Open the image
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Extract the binary message from the image
    binary_secret = ''.join(str(pixel[-1]) for pixel in pixels)

    # Convert binary to ASCII
    decrypted_message = ''.join(chr(int(binary_secret[i:i+8], 2)) for i in range(0, len(binary_secret), 8))

    return decrypted_message

if __name__ == "__main__":
    # Paths
    image_path = "myimage.png"  # Replace with your image file path
    output_path = "encrypted_image.png"  # Replace with the desired output path
    secret_message = input("Enter secret message: ")

    # Encryption
    encrypt(image_path, secret_message, output_path)
    print("Image encrypted and saved to", output_path)

    # Decryption
    decrypted_message = decrypt(output_path)
    print("Decrypted message:", decrypted_message)
