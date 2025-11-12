def isAnagram(s: str, t: str):
    import string

    # Lowercase alphabet
    lowercase_alphabet = str(string.ascii_lowercase)
    expected_freqs = [0]*len(lowercase_alphabet)
    for c in s:
       expected_freqs[lowercase_alphabet.index(c)] += 1

    checking_freqs = [0]*len(lowercase_alphabet)
    for c in t:
        checking_freqs[lowercase_alphabet.index(c)] += 1
    
    return checking_freqs == expected_freqs

s = "b"; t = "a"
print(isAnagram(s, t))