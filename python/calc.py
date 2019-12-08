# defined method
def sum(opl, opl2):
    return opl + opl2
def sub(opl, opl2):
    return opl - opl2
def mul(opl, opl2):
    return opl * opl2
def div(opl, opl2):
    return opl / opl2
    

def menu():
    print(" Menu ")
    print("[1]  - Add")
    print("[2]  - Subtract")
    print("[3]  - Multiply")
    print("[4]  - Division")
    print("[x]  - Exit")

opc = ""
while(opc != "x"):
    menu()
    opc = input("Select an option: ") 
    if(opc == "x"): 
        break # break the loop 

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if(opc == '1'):
        sum_res = sum(num1, num2)
        print("Sum =  " + str(sum_res))

    if(opc == '2'):
        sub_res = sub(num1, num2)
        print("Subtract =  " + str(sub_res))
    
    if(opc == '3'):
        mul_res = mul(num1, num2)
        print("Multiply =  " + str(mul_res))

    if(opc == '4'):
        div_res = div(num1, num2)
        print("Division =  " + str(div_res))

    input("Press Enter to go back")
