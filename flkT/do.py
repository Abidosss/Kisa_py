from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)

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

# 测试代码
sentence = "AbcD!"
result = converter(sentence,2)
print(result)

def parser(text):
    text = ''
    return

###################################################################


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text=request.form.get('text')
        digit=request.form.get('digit')
        result=converter(str(text),int(digit))
        return render_template('index.html',text=text,digit=digit,result=result)

    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files

if __name__ == '__main__':
    app.debug = True
    app.run()