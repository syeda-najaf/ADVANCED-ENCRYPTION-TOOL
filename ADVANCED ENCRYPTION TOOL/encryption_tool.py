from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# AES Key (must be 32 bytes for AES-256)
KEY = b"ThisIsA32ByteLongSecretKey123!"

def encrypt_file(input_file, output_file="encrypted.aes"):
    """ Encrypts a file using AES-256 (CBC Mode) """
    iv = get_random_bytes(16)  # Generate a random IV (16 bytes)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)

    with open(input_file, "rb") as f:
        plaintext = f.read()

    # Pad the plaintext to be a multiple of 16 bytes
    padding_length = 16 - (len(plaintext) % 16)
    plaintext += bytes([padding_length]) * padding_length

    ciphertext = cipher.encrypt(plaintext)

    with open(output_file, "wb") as f:
        f.write(iv + ciphertext)  # Store IV + encrypted data

    print(f"✅ File Encrypted: {output_file}")

def decrypt_file(input_file, output_file="decrypted.txt"):
    """ Decrypts a file encrypted with AES-256 (CBC Mode) """
    with open(input_file, "rb") as f:
        data = f.read()

    iv = data[:16]  # Extract IV (first 16 bytes)
    ciphertext = data[16:]  # The rest is encrypted data

    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)

    # Remove padding
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    print(f"✅ File Decrypted: {output_file}")

# Example Usage
if __name__ == "__main__":
    choice = input("Choose:\n1. Encrypt File\n2. Decrypt File\n> ")

    if choice == "1":
        file_to_encrypt = input("Enter file name to encrypt: ")
        encrypt_file(file_to_encrypt)

    elif choice == "2":
        file_to_decrypt = input("Enter file name to decrypt: ")
        decrypt_file(file_to_decrypt)

    else:
        print("❌ Invalid choice! Please enter 1 or 2.")
