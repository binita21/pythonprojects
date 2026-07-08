# Arithmetic Operators
a,b = map(int,input("Enter value of a and b :\n").split())
operator = input("Enter operator (+,-,/,*,//,%,**) :\n")
# Addition
def calculator():
    if operator == '+':
        sum = a+b
        print(f"{a}+{b}={sum}") 
    elif operator == '-':
        subtraction = a-b
        print(f"{a}-{b}={subtraction}") 
    elif operator == '/':
        division = a/b
        print(f"{a}/{b}={division}") 
    elif operator == '*':
        multiplication=a*b
        print(f"{a}*{b}={multiplication}") 
    elif operator == '//':
        floor_division = a//b
        print(f"{a}//{b}={floor_division}") 
    elif operator == '%':
        modulo = a%b
        print(f"{a}%{b}={modulo}") 
    elif operator == '**':
        exponential = a**b
        print(f"{a}**{b}={exponential}") 
    else:
        print("Invalid Operator!!")
calculator()
