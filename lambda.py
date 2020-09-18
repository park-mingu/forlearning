files = input().split()

print(list(map(lambda x: "{0:03d}.{1}".format(int(x.split('.')[0]), x.split('.')[1]), files)))
