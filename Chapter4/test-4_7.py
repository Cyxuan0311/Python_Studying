# 创建一个3~30内可以被3整除的列表
# 1.创建一个空列表
list = []
for i in range(3,31):
    if i % 3 == 0:
        list.append(i)
print(list)
