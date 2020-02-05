str1 = input("enter:")
def Text(text):
    ans = ''
    inp = list('abcdefghijklmnopqrstuvwxyz')
    for i in text:
        if i.isalpha():
            ans += str(inp.index(i.lower()) + 1) + ' '
    return ans[0:len(ans) - 1]


print(Text(str1))
