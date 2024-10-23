import random
sum_bat = 0
sum_bowl = 0

def odd_eff(n,decision,sum_bat,sum_bowl):
    i = n + random.randint(1,10)
    if decision == 'even' and i%2==0:
        a = input("Enter bat for batting and bowl for bowling")
        if a == 'bat':
            for i in range(0,10**10):
                number = int(input("Enter a number"))
                if number == random.randint(1,10):
                    return sum_bat
                else:
                    sum_bat += number
                    print(sum_bat, "in batting")
        else:
            for i in range(0,10**10):
                number = int(input("Enter a number"))
                if number == random.randint(1,10):
                    return sum_bowl
                else:
                    sum_bowl += number
                    print(sum_bowl, "in bowling")
    elif decision == 'odd' and i%2!=0:
        a = input("Enter bat for batting and bowl for bowling")
        if a == 'bat':
            for i in range(0,10**10):
                number = int(input("Enter a number"))
                if number == random.randint(1,10):
                    return sum_bat
                else:
                    sum_bat += number
                    print(sum_bat, "in batting")

        else:
            for i in range(0,10**10):
                number = int(input("Enter a number"))
                if number == random.randint(1,10):
                    return sum_bowl
                else:
                    sum_bowl += number
                    print(sum_bowl, "in bowling")


    else:
        a = random.randint(0,1)
        if a == 0:
            for i in range(0,10**10):
                number = int(input("Enter a number"))
                if number == random.randint(1,10):
                    return sum_bat
                else:
                    sum_bat += number
                    print(sum_bat, "in batting")


        else:
            for i in range(0,10**10):
                number = int(input("Enter a number"))
                if number == random.randint(1,10):
                    return sum_bowl
                else:
                    sum_bowl += number
                    print(sum_bowl, "in bowling")


odd_eff(int(input("Enter value from 1 to 10")), input("Odd or even"), 0,0)