"""Doc."""
# работа со строками
# text = 'съешь ещё этих мягких французских булок'
# help(text.istitle)  # встроенная справка языка python
# print(len(text))  # 39
# print('ещё' in text)  # True
# print(text.isdigit())  # False верхнего регистра
# print(text.islower())  # True нижнего регистра
# print(text.replace('ещё', 'ЕЩЁ')) # замена
# for c in text:
#     print(c)

# работа со строками (срезы)

text = 'съешь ещё этих мягких французских булок'
print(text[0])  # c
print(text[1])  # ъ
print(text[len(text)-1])  # к
print(text[-5])  # б
print(text[:])  # print(text)
print(text[:2])  # съ
print(text[len(text)-2:])  # ок
print(text[2:9])  # ешь ещё
print(text[6:-18])  # ещё этих мягких (счет с конца)
print(text[0:len(text):6])  # сеикакл
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...
