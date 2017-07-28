s = input("Enter a number: ")
try:
    number = float(s)
    answer = number * number
    print(number, "*", number, "=", answer)
except:
    number = 0
    print('Something wrong!')
