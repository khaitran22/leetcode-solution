# %%
def intToRoman(num: int) -> str:
    symbols = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    if num in symbols:
        return symbols[num]

    result = ""
    power = 1
    while num > 0:
        lower = 10**(power-1)
        upper = 10**power
        digit = num % 10
        num = int((num - digit) / 10)

        if digit == 4 or digit == 9:
            rom_str = symbols[lower] + (symbols[5*lower] if digit == 4 else symbols[upper])
        else:
            rom_str = digit * symbols[lower] if digit < 5 else symbols[5*lower] + (digit - 5) * symbols[lower]
        
        result = rom_str + result
        power += 1
    
    return result

# %%
num = 3749
intToRoman(num)
# %%
