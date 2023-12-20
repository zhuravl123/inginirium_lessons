

              выводение чисел
chisla = [3,4,2,5,5,3,4,2,5,3]
print(chisla[0])
print(chisla[1])
print(min(chisla))
print(max(chisla))
print(sum(chisla))



              считывание оценок
marks = input("Введите оценки:")
marks = marks.split()

for i in range(len(marks)):
    marks[i] = int(marks[i])

print(sum(marks) / len(marks))



             задача про космонавта про его рост
spisok1 = []
while True:
    rost =  int(input("Введите рост:"))
    if rost>= 160 and rost <= 180:
        spisok1.append(rost)
    if rost == 333:
        print(spisok1)
        break
print(min(spisok1))
print(max(spisok1))

                    пирамида
chislo1 = int(input("Введите число"))
for i in range(chislo1):
    print(" " * (chislo1-i-1) + '*' * (i*2+1))


                 пирамида2
chisla = input('Введите числа')
chisla = chisla.split()
for i in range(len(chisla)):
  print('*' * int(chisla[i]))




             калькулятор

def first_number():
  return int(input(('Введите первое число')))

def second_number():
  return int(input(('Введите второе число')))

def operator():
  return (input(('Введите оператор')))

def calculate(number1,operator,number2):
    if operator == "+":
      return number1 + number2
    elif operator == "-":
      return number1 - number2
    elif operator == "*":
      return number1 * number2
    elif operator == "/":
      if number2 != 0 :
       return number1 / number2
      else:
        print("Делить на ноль нельзя !!!!!!!!!!!!!!!")
number1 = first_number()
number2 = second_number()
oper = operator()
print(calculate(number1,oper,number2))


             пароли
def ask_password():
    password = input('Введиье пароль')
    if password == "пароль":
      print("пароли совпадают")
    else:
      print('Пароли не совпадают')
ask_password()

