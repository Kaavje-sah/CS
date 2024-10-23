# Write a program to check whether the no inputted is a n armstrong no.
# My code
no = 1
while no<1000000:
    sum1 = 0
    temp = no
    no_of_digits=len(str(no))
    while temp > 0:
        digit = temp % 10
        sum1 = sum1 + digit ** no_of_digits
        if no == sum1:
            print("%d is an Armstrong number" % no)
        temp //= 10
    no+=1
# code by AI?
def is_armstrong_number(num):
    no_of_digits = len(str(num))
    sum1 = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum1 += digit ** no_of_digits
        temp //= 10
    return num == sum1

if __name__ == "__main__":
    for num in range(1, 1000000):
        if is_armstrong_number(num):
            print(f"{num} is an Armstrong number")