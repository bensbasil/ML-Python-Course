my_string=input("Enter String: ")
rev_string=my_string[::-1]

if my_string == rev_string:
    print(f"palindromes.")
    print(f"{my_string} secound {rev_string}")

rev=[]
for x in range(len(my_string)-1,-1,-1):
    #print(my_string[x])
    rev.append(my_string[x])

print(rev)