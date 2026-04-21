def isHappy(n):
    if n == 1:
        return True

    def get_sqrt_sum(n):
        temp_n = n
        sum = 0
        while temp_n > 0:
            curr_digit = temp_n % 10
            sum += curr_digit**2
            temp_n = int((temp_n - curr_digit) / 10)
        return sum
    
    slow = get_sqrt_sum(n)
    fast = get_sqrt_sum(get_sqrt_sum(n))
    if slow == fast and slow == 1:
        return True
    while slow != fast:
        slow = get_sqrt_sum(slow)
        fast = get_sqrt_sum(get_sqrt_sum(fast))
        if slow == 1 or fast == 1:
            return True
    return False

num = 10
print(isHappy(num))