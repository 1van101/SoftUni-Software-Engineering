budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0
if destination == "Dubai":
    if season == "Winter":
        price = 45000
    else:
        price = 40000
    price *= 0.7
elif destination == "Sofia":
    if season == "Winter":
        price = 17000
    else:
        price = 12500
    price *= 1.25
else:
    if season == "Winter":
        price = 24000
    else:
        price = 20250

total_price = price * days
diff = abs(total_price - budget)
if budget >= total_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
