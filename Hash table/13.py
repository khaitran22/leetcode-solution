# %%
def romanToInt(x: str):
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if x in symbols:
        return symbols[x]
    
    result = 0
    prev_val = 0
    for i in range(len(s)-1, -1, -1):
        value_at_i = symbols[x[i]]
        result = result + (value_at_i if value_at_i >= prev_val else -value_at_i)
        prev_val = value_at_i
    return result
    
s = "MCMXCIV"
romanToInt(s)
# %%
