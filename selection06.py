#selection06.py

a = int(input("첫째 정수 입력:"))
b = int(input("둘째 정수 입력:"))
op = input("연산자 입력:")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else :
    print("unknown operator")
    
