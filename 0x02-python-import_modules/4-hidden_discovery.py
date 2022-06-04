#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    myList = dir(hidden_4)
    for elem in myList:
        if ord(elem[0]) in range(ord('a'), ord('z') + 1):
            print(elem)
