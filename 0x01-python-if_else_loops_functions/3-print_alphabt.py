#!/usr/bin/python3
for letter in range(97,123):
    new = chr(letter)
    if letter == 101 or letter == 113:
        continue
    print("{}".format(new), end="")
