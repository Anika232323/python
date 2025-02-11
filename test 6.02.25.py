def longest_common_suffix(strings):
    if not strings:
        return ""

    min_len = min(len(s) for s in strings)
    suffix = ""

    for i in range(1, min_len + 1):
        chars = [s[-i] for s in strings]
        if len(set(chars)) == 1:
            suffix = chars[0] + suffix
        else:
            break

    return suffix

strings = input().split()
print("Longest common suffix:", longest_common_suffix(strings))
