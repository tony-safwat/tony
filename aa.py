def biger(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("num1 is the bigger")
    elif num2>num1 and num2>num3:
        print("num2 is the bigger")
    elif num3>num1 and num3>num2:
        print("num3 is the bigger")

biger(int(input("num1: ")),int(input("num2: ")),int(input("num3: ")))
