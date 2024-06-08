def reverse_string(s, index=0):
    if index == len(s):
        return ""
    else:
        return s[-(index + 1)] + reverse_string(s, index + 1)
s = "hello"
print("Reverse of", s, "is", reverse_string(s))
