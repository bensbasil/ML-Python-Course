d = input("Enter The Bit: ")
print(f'{int(d, 2)}')

a=int(input("Enter First Number "))
b=int(input("Enter Secound Number "))
c=int(input("1 add \n 2 sub \n 3 mul \n 4 div \n  "))

if c==1:
    z=int(a)+int(b)
    print(z)
elif c==2:
    z=a-b
    print(z)
elif c==3:
    z=a*b
    print(z)
    x=(a&b)
    v=(a|b)
    o=(~a)
    print(f"Binary Number :{x} OR :{v}  NOT:{o}")

""" Operators	Meaning
()	Parentheses
**	Exponent
+x, -x, ~x	Unary plus, Unary minus, Bitwise NOT
*, /, //, %	Multiplication, Division, Floor division, Modulus
+, -	Addition, Subtraction
<<, >>	Bitwise shift operators
&	Bitwise AND
^	Bitwise XOR
|	Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in	Comparisons, Identity, Membership operators
not	Logical NOT
and	Logical AND
or	Logical OR """