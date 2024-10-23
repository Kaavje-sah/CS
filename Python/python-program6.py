even_product = 1
odd_product = 1
i = 1
while i<=10:
    if i % 2 == 0:
        even_product *= i
    else:
        odd_product *= i
    i+=1
print(f"Product of even numbers: {even_product}")
print(f"Product of odd numbers: {odd_product}")