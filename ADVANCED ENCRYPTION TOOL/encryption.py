from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

KEY = get_random_bytes(32)  # Generate AES-256 key

def encrypt(data):
    cipher = AES.new(KEY, AES.MODE_CBC)
    iv = cipher.iv
    padding_length = 16 - (len(data) % 16)
    data += bytes([padding_length] * padding_length)
    return iv + cipher.encrypt(data)
def decrypt(data):
    iv = data[:16]  # Extract the IV from the first 16 bytes
    cipher = AES.new(KEY, AES.MODE_CBC, iv)  # Use correct IV
    decrypted_data = cipher.decrypt(data[16:])  # Decrypt the remaining data
    return decrypted_data.rstrip(b"\0")
