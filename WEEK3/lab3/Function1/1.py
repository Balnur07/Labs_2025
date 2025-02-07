def grams_to_ounces(GRAMS):
    OUNCES = 28.3495231 * GRAMS
    return OUNCES

GRAMS = float(input("grams: "))
print(grams_to_ounces(GRAMS))

