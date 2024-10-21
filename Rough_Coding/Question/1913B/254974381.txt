for _ in range(int(input())):
    s = input()
    cnt = [0, 0]
    for i in range(len(s)):
        cnt[int(s[i])] += 1
    for i in range(len(s) + 1):
        if (i == len(s) or cnt[1 - int(s[i])] == 0):
            print(len(s) - i)
            break
        cnt[1 - int(s[i])] -= 1