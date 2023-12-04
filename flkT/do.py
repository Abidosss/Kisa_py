from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)

def converter(sentence,digit):
    new_sentence = ''
    for char in sentence:
        if char.isalpha():
            new_sentence += chr(ord(char)+digit)
        else:
            new_sentence += char
    return new_sentence.lower()

# 测试代码
sentence = "AbcD!"
result = converter(sentence,2)
print(result)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text=request.form.get('text')
        digit=request.form.get('digit')
        result=converter(str(text),int(digit))
        return render_template('index.html',text=text,digit=digit,result=result)

    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()