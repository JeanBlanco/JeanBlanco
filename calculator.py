print("### Basic calculator ###")
print("### Jean Blanco")
import os
while True:
    menu = """
    Main Menu
    1. ADD
    2. SUBTRACT
    3. MULTIPLY
    4. DIVIDE
    5. EXPONENTIATION
    """
    print(menu)
    Cal = int(input(" Type the desired option: "))
    if Cal == 1:
        add = float(input(" Enter the first operator: "))
        add2 = float(input(" Enter the second operator"))
        result = add + add2
        print(result)
        res = input("¿do you want to continue? ¿yes/no?")
        if res.capitalize() == "No":
            os.system("cls")
            break
        else:
            os.system("cls")

    if Cal == 2:
        sub = float(input(" Enter the first operator: "))
        sub2 = float(input(" Enter the second operator: "))
        resu = sub - sub2
        print(resu)
        res = input("¿do you want to continue? ¿yes/no?")
        if res.capitalize() == "No":
            os.system("cls")
            break
        else:
            os.system("cls")

    elif Cal == 3:
        mult = float(input(" Enter the first operator: "))
        mul = float(input(" Enter the second operator: "))
        re = mult * mul
        print(re)
        res = input("¿do you want to continue? ¿yes/no?")
        if res.capitalize() == "No":
            os.system("cls")
            break
        else:
            os.system("cls")

    elif Cal == 4:
        div = float(input(" Enter the first operator: "))
        divi = float(input(" Enter the second operator: "))
        if divi != 0:
            print(div/divi)
        else:
            print("The number is indeterminete")
        res = input("¿do you want to continue? ¿yes/no?")
        if res.capitalize() == "No":
            os.system("cls")
            break
        else:
            os.system("cls")

    elif Cal == 5:
        expo = float(input(" Enter the first operator: "))
        exp = float(input(" Enter the second operator: "))
        rst = pow(expo, exp)
        print(rst)
        print("The number is indeterminete")
        res = input("¿do you want to continue? ¿yes/no?")
        if res.capitalize() == "No":
            os.system("cls")
            break
        else:
            os.system("cls")
    
    else:
        print("The option is not valid")
        res = input("¿do you want to continue? ¿yes/no?")
        if res.capitalize() == "No":
            os.system("cls")
            break
        else:
            os.system("cls")







