def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

# Define your key. This can be any integer.
key = 5

# Test the function
text = "hello world"
encrypted = xor_cipher(text, key)
decrypted = xor_cipher(encrypted, key)

print(f"Original text: {text}")
print(f"Encrypted text: {encrypted}")
print(f"Decrypted text: {decrypted}")