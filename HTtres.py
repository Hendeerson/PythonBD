print("********************Password Match********************")
#Ejercicio 1

password = "contraseña"
contraseña = input("Please enter the password: ")
if password == contraseña.lower():
    print("There is coincidence") 
else:
    print("There is no coincidence")
    
#EndExcercise1
print("*******************************************************")

print("****************Splitting Grourp***********************")
#Ejercicio 2

gender= input("Please enter your gender (Masculino/Femenino): ")
name = input("What is your name? ")

if gender == "Masculino":
    if name.lower() < "m":
        group = "A"
    else:
        group ="B"
else:
    if name.lower() >"n":
        group = "A"
    else:
        group = "B"
print("Your group is: " + group)                        

#EndExcercise2
print("*******************************************************")