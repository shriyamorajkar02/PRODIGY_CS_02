from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """ Encrypts an image using pixel manipulation. """
    img = Image.open(input_path)
    img_array = np.array(img)

    # Encrypt by adding the key value to pixel values
    encrypted_array = np.clip(img_array + key, 0, 255)
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as: {output_path}")

def decrypt_image(input_path, output_path, key):
    """ Decrypts an image using reverse pixel manipulation. """
    img = Image.open(input_path)
    img_array = np.array(img)

    # Decrypt by subtracting the key value from pixel values
    decrypted_array = np.clip(img_array - key, 0, 255)
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))

    decrypted_img.save(output_path)
    print(f"Decrypted image saved as: {output_path}")

# File paths (Updated for your Desktop)
input_image = r"C:\Users\SANDEEP\Desktop\smartphone.jpg"
encrypted_image = r"C:\Users\SANDEEP\Desktop\encrypted.png"
decrypted_image = r"C:\Users\SANDEEP\Desktop\decrypted.png"

key = 50  # Change this for different encryption

print("Encrypting image...")
encrypt_image(input_image, encrypted_image, key)

print("Decrypting image...")
decrypt_image(encrypted_image, decrypted_image, key)
