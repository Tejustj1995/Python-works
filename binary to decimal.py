list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    list.append(ele)
print("The original list is : " + str(list))
res = int("".join(str(x) for x in list), 2)
print("value is : " + str(res))