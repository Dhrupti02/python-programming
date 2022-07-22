''' Simple calculator that will let user enter the numbers and opertors to perform the arithmetic operations. '''


n = 1
print("Welcome to use the Simple Calculator!")

def add(N1, N2):
    add = N1 + N2
    print("Result",N1,'+',N2,":",add)

def sub(N1, N2):
    sub = N1 - N2
    print("Result",N1,'-',N2,":",sub)

def mul(N1, N2):
    mul = N1 * N2
    print("Result",N1,'*',N2,":",mul)

def div(N1, N2):
    try:
        div = N1 / N2
    except ZeroDivisionError:
        print("Enter your second number which cannot be zero: 0.0")
        print("Enter your second number which cannot be zero: 0.")
        print("Enter your second number which cannot be zero:  7")
        mod = N1 / 7
        print("Result",N1,'/',7.0,":",mod)
    else:
        print("Result",N1,'/',N2,":",div)

def mod(N1, N2):
    try:
        mod = N1 % N2
    except ZeroDivisionError:
        print("Enter your second number which cannot be zero: 0.0")
        print("Enter your second number which cannot be zero: 0.")
        print("Enter your second number which cannot be zero:  7")
        mod = N1 % 7
        print("Result",N1,'%',7.0,":",mod)
    else:
        print("Result",N1,'%',N2,":",mod)

def pow(N1, N2):
    pow = N1 ** N2
    print("Result",N1,'+',N2,":",pow)

while True:
    print(n,"=========================================================.") 
    n+=1
    N1 = float(input("Enter your first number: "))
    op = input("Enter your operator (@ to stop): ")
    N2 = float(input("Enter your second number: "))

    if op == '+':
        add(N1, N2)
    
    elif op == '-':
        sub(N1, N2)
    
    elif op == '*':
        mul(N1, N2)
    
    elif op == '/':
        div(N1, N2)

    elif op == '%':
        mod(N1, N2)

    elif op == '**':
        pow(N1, N2)

    elif op == '@':
        print("Thank you for using the calculator!")
        break

    else:
        print("Sorry,", op, "is not a valid operator!")
print (n,"============================================================")
n+=1