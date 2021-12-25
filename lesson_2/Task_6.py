i = 1
structure = []
while True:
  name = input('Name: ')
  price = int(input('Price: '))
  count = int(input('Cout: '))
  measure = input('Measure: ')
  structure.append((i, {'name': name, 'price': price, 'count': count, 'measure': measure}))
  i += 1
  if i >= 4:
    break

out = {}
name = []
price = []
count = []
measure = set()
for e in structure:
  name.append(e[1].get('name'))
  price.append(e[1].get('price'))
  count.append(e[1].get('count'))
  measure.add(e[1].get('measure'))

my_list = list(measure)

print({'name': name, 'price': price, 'count': count, 'measure': my_list})