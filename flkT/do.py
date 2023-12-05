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

###################################################################


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        de_text = None
        en_text = None
        de_result = None
        en_result = None
        de_text=request.form.get('de_text')
        en_text=request.form.get('en_text')
        de_result = caesar_decrypt(de_text)
        return render_template('index.html',de_text=de_text,en_text=en_text,de_result=de_result,en_result=en_result)

    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files

if __name__ == '__main__':
    app.debug = True
    app.run()