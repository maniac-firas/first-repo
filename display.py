def display(s):
    lu = [chr(x) for x in range(32, 127)]
    r = [""]*len(s)
    for a in range(len(s)):
        t = r
        for l in lu:
            t[a] = l
            print("".join(t))
            if t[a] == s[a]:
                r = t
                break
    for i in range(10): print("".join(r))

display('Mariappan is the Goat!!')
