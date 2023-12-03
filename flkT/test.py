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
