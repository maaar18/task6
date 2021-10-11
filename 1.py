array = list(map (int, input("Введите массив:")))
delta = input("Введите delta:")
try:
   delta = int(delta)
except ValueError:
   print("Ошибка")
   exit()
c = abs(delta)
a = min(array)
b = len([x for x in array if x == a + c])
print(b)