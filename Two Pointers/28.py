def strStr(haystack, needle):
    """
    Problem #28
    Personal solution, 100% runtime, 96.84% memory
    """
    if len(needle) > len(haystack):
        return -1

    first_char_n = needle[0]
    len_haystack = len(haystack)
    len_needle = len(needle)
    for start in range(len(haystack)):
        if haystack[start] == first_char_n and (len_haystack-start) >= len_needle:
            matching = True
            end = 1
            ending_pos = min(len_haystack-start, len_needle)
            while end < ending_pos:
                if haystack[start+end] != needle[end]:
                    matching = False
                    break
                else:
                    end += 1
            if matching:
                return start
    return -1


def search(pat, txt):
    res = []
    n = len(txt)
    m = len(pat)

    for i in range(n - m + 1):
        j = 0

        # compare pattern with substring
        # starting at index i
        while j < m and txt[i + j] == pat[j]:
            j += 1

        # if full pattern matched
        if j == m:
            res.append(i)

    return res


haystack = "sadbut"
needle = "sad"
print(strStr(haystack, needle))
