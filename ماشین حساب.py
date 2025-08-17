
import tkinter as tk


def gam(x, y):
    return x + y


def tafrigh(x, y):
    return x - y


def zarb(x, y):
    return x * y


def taghsim(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choise = input('enter choise(1,2,3,4):')
    if choise in ('1''2''3''4'):
        try:
            nam1 = float(input('enter namber one '))
            nam2 = float(input('enter namber tow'))
        except ValueError:
            print('ورودی اشتباع است دوبارع تلاش کنید:')
            continue
        if choise == '1':
            print(nam1, '+', nam2, '=', gam(nam1, nam2))
        elif choise == '2':
            print(nam1, '-', nam2,'=', tafrigh(nam1, nam2))
        elif choise == '3':
            print(nam1, '*', nam2, '=', zarb(nam1, nam2))
        elif choise == '4':
            print(nam1, '/', nam2, '=', taghsim(nam1, nam2))
    nexcolection = input('ایا قصد ادامه دادن داریدes/no)')
    if nexcolection == 'no':
        break
    elif nexcolection == 'yes':
        print('ورودی جدید را وارد کنید')
    else:
        print('وردی اشتباه است دوباره تلاش کن کسکش')
