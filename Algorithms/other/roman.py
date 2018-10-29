"""
Decimal to Roman Numeral converter.
Time Complexity: O(n)
Space COmplexity: constant
"""

def romanise(n):
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    dec = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_num = ""
    i = 0
    flag = True
    while( flag and i < len(rom)):
        div = dec[i]
        rom_num += (n // div) * rom[i]
        n = n % div
        i += 1
        if(n == 0):
            flag == False
    return rom_num

#testing
print(romanise(983))
