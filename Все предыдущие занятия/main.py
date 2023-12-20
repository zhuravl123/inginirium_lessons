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
        print("Делить на ноль нельзя !!!")
number1 = first_number()
number2 = second_number()
oper = operator()
print(calculate(number1,oper,number2))

