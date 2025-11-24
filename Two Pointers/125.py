def isPalindrome(s: str):
    s = s.lower()
    s = "".join(s.split(" "))
    s = "".join([c for c in list(s) if c.isalnum()])

    if len(s) <= 1:
        return True

    l, r = 0, len(s)-1
    while r > l:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = "."
print(isPalindrome(s))
