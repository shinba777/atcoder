def solve():
    s = input()
    ans = ""
    for i in range(len(s)-1):
        ans += s[i] + "o"
    print(ans+s[len(s)-1])

solve()