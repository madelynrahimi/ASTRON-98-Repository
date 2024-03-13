def power_function(x,y): #where x is the base number and y is the number x is raised to the power of
    if y == 0:
        print (1)
    elif y > 0:
        power = 1
        for i in range(y):
            power = power * x
        print (power)
    elif y < 0:
        power = 1
        for i in range(-y):
            power = power / x
        print (power)

power_function(1,0) 
power_function(2,2)
power_function(9,-2)
