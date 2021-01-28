def main():
    s = input("Enter string").strip()

    if isPalindrome(s):
        print(s, "is a Palindrome")
    else:
        print(s, " is not a Palindrome")

def isPalindrome(s):
    low = 0 #index of first character in the string
    high = len(s) - 1 #index of last character in the string

    while low < high:
        if s[low] != s[high]: #means string is not a palindrome
            return False
        low += 1
        high -= 1
    return True

main()