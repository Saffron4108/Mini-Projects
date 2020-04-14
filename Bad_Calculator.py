TYPE = input("What type of sum are you doing? (Addition, subtraction, multiplication, division: ")
NUM1 = int(input("ENter the first number: "))
NUM2 = int(input("Enter the second number:"))


if TYPE == 'a':
    print(NUM1 + NUM2)
elif TYPE == 's':
    print(NUM1 - NUM2)
elif TYPE == 'm':
    print(NUM1 * NUM2)
elif TYPE == 'd':
    print(NUM1 / NUM2)
