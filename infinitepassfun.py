def fun(dt, *a):
    #checking dt is "int" or not
    if dt == "int":
        sum = 0
        for x in a:
            #int() is used to convert string to integer, we can use eval() as it evalute the string
            sum = sum + int(x)
        print(sum)
       #checking dt is "str" or not
    if dt == "str":
        b = " "
        for x in a:
            b = b + x + " "
        print(b)
def main():
    data_type = input("Enter int for integer and str for string")
    #here you can assume n number of inputs
    a = input("Enter the value")
    b = input("Enter the value")
    c = input("Enter the value")
    #passing values to function fun with the data type and values or object.
    fun(data_type, a, b, c)
if __name__ == '__main__':
    main()
