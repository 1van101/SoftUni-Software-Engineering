text = input().split()
even_words = [x for x in text if len(x) % 2 == 0]
print("\n".join(even_words))