import random
while(True):
    num1 =input("Enter Number betweeen 1-10 : ")
    x=random.randint(1,5)
    if x==int(num1):
        print(f"you are won{x}")
    else:
        print(f"Failed {x}")
