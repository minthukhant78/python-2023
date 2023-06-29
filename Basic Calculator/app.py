number1 = int(input ('Enter First number : '))
number2 = int(input ('Enter Second number : '))
operator = input ('Enter Operator : ')

if operator == '+':
    print(number1+number2)
elif operator == '-':
    print(number1-number2)
elif operator == '*':
    print(number1*number2)
elif operator == '/':
    print(abs(number1/number1))
else :
    print('Invalid operator')