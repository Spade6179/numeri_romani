import sys

orderedNumerals = [
    (1000,	"M"),
    (900,	"CM"),
    (500,	"D"),
    (400,	"CD"),
    (100,	"C"),
    (90,	"XC"),
    (50,	"L"),
    (40,	"XL"),
    (10,	"X"),
    (9,	    "IX"),
    (5, 	"V"),
    (4,	    "IV"),
    (1, 	"I"),
]

def numeri_romani(i):
    i = int(i)
    if i < 1 or i > 3999:
        raise ValueError()

    roman_numeral = []

    for arabic, roman in orderedNumerals:
        while i // arabic > 0:
            roman_numeral.append(roman)
            i -= arabic

    return "".join(roman_numeral)
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(numeri_romani(sys.argv[1]))