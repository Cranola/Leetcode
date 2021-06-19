# 思想是记录当前最大长度的同时，不断更新子串的起始位置
def find_longest_substring(s):
    if len(s) <= 1:
        return len(s)

    start = 0
    curr_length = 0
    max_length = 0
    record = {}
    for i in range(len(s)):
        if s[i] in record and record[s[i]] > start:
            start = record[s[i]] + 1

        curr_length = i - start + 1
        record[s[i]] = i

        if max_length < curr_length:
            max_length = curr_length
    return max_length


res = find_longest_substring('mabcafrab')
print(res)