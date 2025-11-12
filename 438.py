def findAnagrams(s, p):
    import string

    # Lowercase alphabet
    lowercase_alphabet = str(string.ascii_lowercase)
    expected_freqs = [0]*len(lowercase_alphabet)
    alphabet_idx = {c: idx for idx, c in enumerate(lowercase_alphabet)}
    for c in p:
       expected_freqs[alphabet_idx[c]] += 1


    result = []
    
    if len(s) < len(p):
        return result
    
    for i in range(len(s)-len(p)+1):
        curr_sub_str = s[i:i+len(p)]
        checking_freqs = [0]*len(lowercase_alphabet)
        for c in curr_sub_str:
            checking_freqs[alphabet_idx[c]] += 1
        if expected_freqs == checking_freqs:
            result.append(i)
    
    return result

s = "cbaebabacd"; p = "abc"
# s = "abab"; p = "ab"
result = findAnagrams(s, p)
print(result)