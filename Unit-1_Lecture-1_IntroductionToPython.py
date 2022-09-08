import random
x = int(input("Enter your number : "))
g = random.randint(1, x)
number_of_reps = 0
while round(g*g,1) != x :
    g = (g + x/g)/2
    number_of_reps = number_of_reps + 1
print("square root of "+ str(x) +" is approx " +str(g)+" after "+str(number_of_reps) +" tries")
