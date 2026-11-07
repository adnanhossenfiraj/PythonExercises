# Problem 45 — Caesar cipher একটি ইংরেজি string-কে নির্দিষ্ট shift দিয়ে encrypt ও decrypt করো; punctuation ও case বজায় রাখার চেষ্টা করো।


import time

def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.islower():
            shifted = (ord(char) - ord("a") + shift) % 26 + ord("a")
            encrypted_text += chr(shifted)

        elif char.isupper():
            shifted = (ord(char) - ord("A") + shift) % 26 + ord("A")
            encrypted_text += chr(shifted)

        elif char.isnumeric():
            shifted = (ord(char) - ord("0") + shift) % 10 + ord("0")
            encrypted_text += chr(shifted)

        else:
            encrypted_text += char
            
    return encrypted_text

def caesar_decrypt(text, shift):
  return caesar_encrypt(text, -shift)


message = "hello"
shift_key = time.localtime().tm_hour

encrypted = caesar_encrypt(message, shift_key)
print("Shift Key:", shift_key)
print("Encrypted:", encrypted)

decrypted = caesar_decrypt(encrypted, shift_key)
print("Decrypted:", decrypted)