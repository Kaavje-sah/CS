for i in range(5):
        print(''.join(str(j) for j in range(1, 5 - i + 1)) + ' ' * (2 * i) + ''.join(str(j) for j in range(5 - i, 0, -1)))