input1 = input()

try:
    val = int(input1)
except ValueError:
   print()
   input1 = input()

input2 = input()
try:
    val = int(input2)
except ValueError:
   print()
   input2 = input()



print("choose operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input()
if choice == '1':
    addition = int(input1) + int(input2)
    print("Sum is",addition)
elif choice == '2':
    subtraction = int(input1) - int(input2)
    print("Subtraction is",subtraction)
elif choice == '3':
    multiplication = int(input1) * int(input2)
    print("multiplication is",multiplication)
elif choice == '4':
    division = int(input1) / int(input2)
    print("division is",division)
elif choice == '5':
    remainder = int(input1) % int(input2)
    print ("remainder is", remainder)
else:
    print("Please choose from the given choices")
