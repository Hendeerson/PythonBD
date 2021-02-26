#Triangle
print("**************Triangulo Rectangulo**************")
print("¿What is the height of the triangle?")
height = int(input())
for i in range(height):
    for j in range(i+1):
        print("*", end ="")
    print("")
print("*************************************************")
#End Triangle
     
#Prime Number
print("---------------Prime Number----------------------")
number=int(input("Enter a number: "))
def evaluar_primo(number):
    count=0
    result=True
    for i in range(1,number+1):
        if (number%i==0):
            count+=1
        if (count>2):
                result=False
                break
    return result
if (evaluar_primo(number)==True):
    print("The number is prime")
else:
    print("The number is not prime")   
print("--------------------------------------------------")
#End Prime Number