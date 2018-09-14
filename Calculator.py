#introduction

print("Welcome to the Basic Calculator")
print("="*50)

#Generates user input
def program():

    num1 = input("Please enter your first number: ")
    num2 = input("Please enter your second number: ")
    
    #validation

    function = ""
    while function != "+" and function != "-" and function != "x" and function != "/":
        function = input("Please enter what function you want to follow (+,-,x,/): ")
        if function != "+" and function != "-" and function != "x" and function != "/":
            print("This is an invalid function. Please enter again")

    #if for addition

    if function == "+":
        add = int(num1) + int(num2)
        print("The sum of",num1,"and",num2,"is:",add)

    #if for subtract

    elif function == "-":
        subtract = int(num1) - int(num2)
        print(num1,"subtract",num2,"is:",subtract)

    #if for multiply

    elif function == "x":
        multiply = int(num1) * int(num2)
        print(num1,"multiplied by",num2,"is:",multiply)

    #else for divide

    else:
        divide = int(num1) / int(num2)
        print(num1,"divided by",num2,"is:",divide)

x = 0
while x == 0:
    print("="*50)
    program()
