# %%
def myAtoi(s: str) -> int:
    # remove whitespace
    s = s.strip()
    sign = set(["-", "+"])
    result = []
    for i, c in enumerate(s):
        if (c in sign and i != 0) or (c not in sign and not c.isnumeric()):
            break
        result.append(c)

    if len(result) == 0:
        return 0
    
    final_result = 0
    if result[0] in sign:
        for i in range(1, len(result)):
            digit = int(result[i])
            final_result = final_result * 10 + digit
    else:
        for i in range(len(result)):
            digit = int(result[i])
            final_result = final_result * 10 + digit

    final_result = (final_result if result[0] == "+" else -final_result) if not result[0].isnumeric() else final_result
    final_result = max(final_result, -2**31)
    final_result = min(final_result, 2**31 - 1)

    return final_result

# %%
inputs = "   -00000042"
myAtoi(inputs)
# %%
