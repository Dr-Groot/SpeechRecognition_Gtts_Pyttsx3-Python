# Converting Number Into Words

```python
# getting number from the user
n = int(input("Enter the number"))

# reversing the number
rnum = 0
while n != 0:
    digit = n % 10
    rnum= rnum *10 + digit
    n = n//10

# converting number to text and storing it in st variable
l = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

# empty string for storing the new word
st = ""

# storing the word in st by checking each number by list l.
while rnum != 0:
    digit = rnum % 10
    st = st + l[digit] + " "
    rnum = rnum // 10

print("Number in words: ", st)
```
