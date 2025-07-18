# Level 2

#Ejercicio_1
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"The number of odds are {odds}. The number of evens are {evens}."

#Ejercicio_1
def factorial(n):
    return math.factorial(n)


#Ejercicio_2
def is_empty(param):
    return not bool(param)


#Ejercicio_3
def calculate_mean(lst):
    return mean(lst)
def calculate_median(lst):
    return median(lst)
def calculate_mode(lst):
    return Counter(lst).most_common(1)[0][0]
def calculate_range(lst):
    return max(lst) - min(lst)
def calculate_variance(lst):
    return variance(lst)
def calculate_std(lst):
    return stdev(lst)

