"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现
任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"
匹配，但是与"aa.a"和"ab*a"均不匹配
"aaa","a*a" ==> true
"""


def match(str, pattern):
    # 讨论各种终止条件，确保是终止条件，不能再匹配下去
    if not str and not pattern:
        return True
    if str and not pattern:
        return False

    if len(pattern) > 1 and pattern[1] == '*':
        if str and (str[0] == pattern[0] or pattern[0] == '.'):
            # 包含了字符串先为空的情况
            return match(str[1:], pattern) or match(str, pattern[2:])
        else:
            return match(str, pattern[2:])
    elif str and (str[0] == pattern[0] or pattern[0] == '.'):
        return match(str[1:], pattern[1:])
    else:
        return False

