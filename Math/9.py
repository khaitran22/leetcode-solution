# %%
def isPalindrome(x: int) -> bool:
    # if x < 0:
    #     return False
    
    # if x >= 0 and x < 10:
    #     return True
    
    # new_x = x
    # reverse_x = 0
    # while new_x > 0:
    #     last_digit = new_x % 10
    #     reverse_x = reverse_x * 10 + last_digit
    #     new_x = int((new_x - last_digit) / 10)

    # return reverse_x == x
    stores = []
    while x > 0:
        last_digit = x % 10
        stores.insert(0, last_digit)
        x = int((x - last_digit) / 10)
    
    
    
isPalindrome(-100)
# %%
