print("enter first number")
n1 = input()
print("symbol")
sym = input()
print("enter 2nd number")
n2 = input()
add = (int(n1)+int(n2))
sub = (int(n1)-int(n2))
mul = (int(n1)*int(n2))
div = (int(n1)/int(n2))

#print("addition"),print(add)
#print("subtraction"),print(sub)
#print("multiplication"),print(mul)
#print("division"),print(div)
if sym==("-"):
    print(sub)
    print("answer")
if sym==("+"):
   print(add)
   print("answer")
if sym==("×"):
   print(mul)
   print("answer")
if sym==("÷"):
   print(div)
   print("answer")