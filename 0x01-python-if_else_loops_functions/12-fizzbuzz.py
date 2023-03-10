#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        ans = ""
        if i % 3 == 0:
            ans += "Fizz"
        if i % 5 == 0:
            ans += "Buzz"
        print(ans or i, end=" ")
