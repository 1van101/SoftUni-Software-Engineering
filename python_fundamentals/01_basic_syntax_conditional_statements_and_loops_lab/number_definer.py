n = float(input())
number = ""
if n == 0:
    number = "zero"
elif n > 0:
    number = "positive"
    if 0 < n < 1:
        number = "small positive"
    elif n > 1_000_000:
        number = "large positive"
else:
    number = "negative"
    if 0 > n > -1:
        number = "small negative"
    elif n < - 1_000_000:
        number = "large negative"
print(number)
