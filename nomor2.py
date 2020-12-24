def print_n(n):
    string = str(n)+" "
    if n%3 == 0:
        string += "Fizz"
    if n%5 == 0:
        string += "Buzz"
    print(string)

if __name__ == "__main__":
    for n in range(1,101):
        print_n(n)