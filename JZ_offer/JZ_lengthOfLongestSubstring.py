def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    if len(s) <= 1:
        return len(s)
    i, j = 0, 0
    while j < len(s):
        curr_length = 0
        while j < len(s) and s[j] not in s[i:j]:
            curr_length += 1
            j += 1
        if curr_length > max_length:
            max_length = curr_length
        if j < len(s):
            ind = i + list(s[i:j]).index(s[j]) + 1
            i = ind
            j = ind
    return max_length


print(lengthOfLongestSubstring('abcabcde'))