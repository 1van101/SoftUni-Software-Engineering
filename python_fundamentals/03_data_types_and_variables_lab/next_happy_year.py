year = int(input())
while True:
    year += 1
    year_to_str = str(year)
    if len(year_to_str) == len(set(year_to_str)):
        print(year)
        break