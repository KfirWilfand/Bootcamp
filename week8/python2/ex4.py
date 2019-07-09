quote = "some people drink from the fountain of knowledge, others just gargle."
VOWELS = ["a", "e", "i", "o", "u"]

my_list = [i for (i, value) in enumerate(quote) if value in VOWELS]
print(my_list)
