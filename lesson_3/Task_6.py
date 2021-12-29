def my_function(text):
    magic = list(text)
    magic[0] = text[0].upper()
    return ''.join(magic)

print(my_function('text'))

text = "text test good"
for i in text.split():
  print(my_function(i), end=' ')
