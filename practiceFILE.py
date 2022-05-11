l = []
bin = []

def RecycleBin(v):
    if len(bin) <= 3:
        bin.append(v)
    else:
        bin.pop(0)
        bin.append(v)

def push(val):
    l.append(val)
    print(l)

def pop():
    if len(l) == 0:
        print("Stack is Underflow")
    else:
        RecycleBin(l[-1])
        l.pop()
        print(l)

def size():
    print(len(l))

def TopValue():
    print(l[-1])

while True:
    print()
    print("Select Option: ")
    print("1 Push Value")
    print("2 Pop Value")
    print("3 Stack Data")
    print("4 Top Element")
    print("5 Number of Element")
    print("6 Recycle Bin")
    print("Any For Exit")
    choice = input()
    if int(choice) == 1:
        v = int(input("Enter the Value"))
        push(v)
    elif int(choice) == 2:
        pop()
    elif int(choice) == 3:
        print(l)
    elif int(choice) == 4:
        TopValue()
    elif int(choice) == 5:
        size()
    elif int(choice) == 6:
        print(bin)
    else:
        print("Terminated")
        print("Final Stack: ", l)
        print("Recycle Bin: ", bin)
        break
