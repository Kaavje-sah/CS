n = int(input("Enter the value of n"))
print()
def triangle_simple_pattern(n):
    for i in range(0, n+1):
        print('* ' * i)

triangle_simple_pattern(n)
print()
def triangle_number_simple_pattern(n):
    for i in range(n+1):
        print(f'{i} ' * i)
triangle_number_simple_pattern(n)
print()
def triangle_number_step_pattern(n):
    for i in range(1, n+1):
        print(' '.join(map(str, range(1, i + 1))))
triangle_number_step_pattern(n)
print()
def triangle_number_inverted_pattern(n):
    for i in range(n,0,-1):
        print(f"{n+1-i} " * i)
triangle_number_inverted_pattern(n)
print()