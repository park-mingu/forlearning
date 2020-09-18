keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x = {key: value for key, value in x.items() if key !='delta' if value != 30}

print(x)