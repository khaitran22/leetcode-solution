# %%
def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    
    longest_prefix = strs[0]
    for i in range(1, len(strs)):
        current_str = strs[i]
        short_str, long_str = (longest_prefix, current_str) if len(longest_prefix) < len(current_str) else (current_str, longest_prefix)
        dissimilar = False
        j = 0
        while j < len(short_str):
            if short_str[j] != long_str[j]:
                dissimilar = True
                break
            
            if longest_prefix == "":
                return ""
            
            j += 1
    
        longest_prefix = longest_prefix[:j] if dissimilar else longest_prefix[:len(short_str)]
    return longest_prefix


strs = ["dog","racecar","car"]
longestCommonPrefix(strs)
# %%
