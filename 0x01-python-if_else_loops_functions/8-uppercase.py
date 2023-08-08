#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if c >= 97 and c <= 122:
            i = chr(c - 32)
        print(f"{i}", end="")
    print()        
