#Level_2

#Ejercicio_1
total = 0
for i in range(101):
    total += i
print("The sum of all numbers is", total)


#Ejercicio_2
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("The sum of all evens is", sum_even)
print("And the sum of all odds is", sum_odd)



