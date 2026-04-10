# %%
import math
def reverse(x: int) -> int:
    if x >= 2**31 or x < -2**31:
        return 0
    
    neg = False if x > 0 else True
    temp_x = abs(x)
    final_result = 0
    while temp_x > 0:
        digit = temp_x % 10
        final_result = final_result * 10 + digit
        temp_x = int((temp_x - digit) / 10)

    if final_result >= 2**31 or final_result < -2**31:
        return 0

    return final_result if not neg else -final_result

x = -123
reverse(x)

# %%
import math
int(math.log10(999))
# %%
