def copy_string(s1, s2, index=0):
    if index == len(s1):
        return
    s2[index] = s1[index]
    copy_string(s1, s2, index + 1)
s1 = "hello"
s2 = [""] * len(s1)
copy_string(s1, s2)
print("".join(s2))  
