# %%
# def lengthOfLongestSubstring(s: str) -> int:
#     longest_substring = tuple()
#     prev_longest_substring = ""
#     i = 0
#     while i < len(s):
#         longest_substring += (s[i],)
#         j = i + 1
#         while j < len(s):
#             if s[j] not in longest_substring:
#                 longest_substring += (s[j],)

#             else:
#                 curr_longest_substring = "".join(longest_substring)
#                 if len(curr_longest_substring) > len(prev_longest_substring):
#                     prev_longest_substring = curr_longest_substring
#                 longest_substring = tuple()
#                 break
             
#             j += 1

#         if j == len(s):
#             i = j
#             break

#         i += 1

#     curr_longest_substring = "".join(longest_substring)
#     if len(curr_longest_substring) > len(prev_longest_substring):
#         prev_longest_substring = curr_longest_substring
    
#     return len(prev_longest_substring)
    # return prev_longest_substring

def lengthOfLongestSubstring(s: str) -> int:
    char_dict = dict()
    result_length = 0
    l = 0
    for r in range(len(s)):
        if char_dict.get(s[r]) != None:
            result_length = max(result_length, len(char_dict))
            while l < r:
                char_dict.pop(s[l])
                l += 1
                if s[l - 1] == s[r]:
                    break
        
        char_dict[s[r]] = 1
    result_length = max(result_length, len(char_dict))

    return result_length

# %%
lengthOfLongestSubstring("bbbbb")
# %%
