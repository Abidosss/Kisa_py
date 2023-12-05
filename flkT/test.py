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
sentence = "Abc!"
result = converter(sentence,1)
print(result)
