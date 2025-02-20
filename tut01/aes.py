import os
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import psutil

def generate_key():
    """Generate a 256-bit AES key."""
    return get_random_bytes(32)

def encrypt_file(input_file, output_file, key):
    """Encrypt a file using AES-256 encryption."""
    try:
        with open(input_file, 'rb') as f:
            data = f.read()
        
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        
        with open(output_file, 'wb') as f:
            f.write(cipher.iv + ciphertext)

        print(f"File {input_file} encrypted successfully to {output_file}.")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_file(input_file, output_file, key):
    """Decrypt a file using AES-256 encryption."""
    try:
        with open(input_file, 'rb') as f:
            iv = f.read(16)
            ciphertext = f.read()
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        
        with open(output_file, 'wb') as f:
            f.write(data)

        print(f"File {input_file} decrypted successfully to {output_file}.")
    except Exception as e:
        print(f"Error during decryption: {e}")

def measure_speed_and_memory(input_sizes):
    """Measure encryption and decryption speeds and memory usage for different input sizes."""
    key = generate_key()
    results = []

    for size in input_sizes:
        input_data = os.urandom(size)
        
        # Measure encryption speed
        cipher = AES.new(key, AES.MODE_CBC)
        start_time = time.time()
        ciphertext = cipher.encrypt(pad(input_data, AES.block_size))
        encryption_time = time.time() - start_time

        # Measure decryption speed
        start_time = time.time()
        cipher_decrypt = AES.new(key, AES.MODE_CBC, cipher.iv)
        unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
        decryption_time = time.time() - start_time

        # Measure memory usage
        process = psutil.Process()
        memory_usage = process.memory_info().rss

        results.append({
            "size": size,
            "encryption_time": encryption_time,
            "decryption_time": decryption_time,
            "memory_usage": memory_usage
        })

    return results

if __name__ == "__main__":
    # File Encryption/Decryption Example
    input_file = "./example.txt"
    encrypted_file = "./example.enc"
    decrypted_file = "./example_decoded.dec"

    # Ensure the input file exists
    if not os.path.exists(input_file):
        with open(input_file, "w") as f:
            f.write("This is a test file for AES encryption.")
        print(f"{input_file} created with sample content.")

    # Generate a key
    key = generate_key()

    # Encrypt the file
    encrypt_file(input_file, encrypted_file, key)

    # Decrypt the file
    decrypt_file(encrypted_file, decrypted_file, key)

    # Speed and Memory Measurement Example
    input_sizes = [1024, 10 * 1024, 100 * 1024, 1024 * 1024]  # 1 KB, 10 KB, 100 KB, 1 MB
    results = measure_speed_and_memory(input_sizes)

    for result in results:
        print(f"Input Size: {result['size']} bytes, Encryption Time: {result['encryption_time']:.6f} sec, "
              f"Decryption Time: {result['decryption_time']:.6f} sec, Memory Usage: {result['memory_usage']} bytes")
