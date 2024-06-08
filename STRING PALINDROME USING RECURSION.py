def is_palindrome(s, index=0):
    if index >= len(s) // 2:
        return True
    if s[index] != s[-(index + 1)]:
        return False
    return is_palindrome(s, index + 1)
s = "madam"
print(s, "is a palindrome" if is_palindrome(s) else "is not a palindrome")
