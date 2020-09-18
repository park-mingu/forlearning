# x = '51900;83000;158000;367500;250000;59200;128500;1304000'
# y = x.split(';')
# index = 0
# for i in y:
#     i = int(i)
#     y[index] = i
#     index = index+1
# reversed(y)
# print(y)

x = map(int, input().split(';'))
y = list(x)
y.sort(reverse=True)
z = [0,0,0,0,0,0,0,0]
index = 0
for i in y:
    # '{0:>9,}'.format(i)
    # format(i, ',')
    # print('%9s' % format(i, ','))
    z[index] = format(i, ',')
    index += 1
print(z)
