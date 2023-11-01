#!/usr/bin/python3
for i in range(0, 89):
    front = i/10
    end = i % 10
    if front > end or front == end:
        continue
    print("{:02d}, ".format(i), end="")
print("89")
