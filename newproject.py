def palindrom(s):
    return s == s[::-1]

    s = "malayalam"
    ans = palindrom(s)

    if ans:
        print("true")
    else:
        print("false")
 