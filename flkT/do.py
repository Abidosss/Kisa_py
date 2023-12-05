from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)

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
    return plaintext

def converter(sentence,shift):
    new_sentence = ''
    for char in sentence:
        if char.isalpha():
            if char.islower():
                new_sentence += chr((ord(char)-ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                new_sentence += chr((ord(char)-ord('A') + shift) % 26 + ord('A'))
        else:
            new_sentence += char
    return new_sentence

###################################################################


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt',methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        shift = request.form.get("Shift")
        text = request.form.get("OriginalText")
        result = converter(text,int(shift))
        return render_template("encrypt.html",EncryptResult=result,OriginalText=text)
    return render_template("encrypt.html")

@app.route('/decrypt',methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        text = request.form.get("EncryptText")
        result = caesar_decrypt(text)
        return render_template("decrypt.html",DecryptResult=result,EncryptText=text)
    return render_template("decrypt.html")

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files

if __name__ == '__main__':
    app.debug = True
    app.run()