def sorting_cheeses(**kwargs):
    result = ""

    for cheese, qty in sorted(kwargs.items(), key= lambda x: (-len(x[1]), x[0])):
        result += cheese + "\n"
        result += '\n'.join([str(x) for x in sorted(qty, reverse= True)]) + "\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
