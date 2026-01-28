# typr of error which are manageble 

try:
    x = int(input("enter any number: "))
    ans= 10/x

except ZeroDivisionError:
    print(" division by 0 is not allowed. ")


except ValueError:
    print("Invalid input")

else:
    print(f"ans is {ans}")

finally:
    print("progrma end")