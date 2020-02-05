n = int(input("Enter the number:"))
n += 1
def game(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz-Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num
for a in range(1, n):
    print(game(a))
