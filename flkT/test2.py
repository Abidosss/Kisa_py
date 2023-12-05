# with open(".\json\schema_ccrequest.json","r") as f:
#     data = f.read()

# print(type(data))

def caesar_decrypt(ciphertext):
    max_count = 0
    best_letter = ""
    
    #计算文本
    letter_counts = {}
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    #计算频率与字母
    for letter, count in letter_counts.items():
        if count > max_count:
            max_count = count
            best_letter = letter
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ord(best_letter) + ord('e') - ascii_offset) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    
    print(f"The letter '{best_letter}' appears {max_count} times.")
    print(f"Decrypted message: {plaintext}")


ciphertext = input("请输入要解密的密文：")
caesar_decrypt(ciphertext)