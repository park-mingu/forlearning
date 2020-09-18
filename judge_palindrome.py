file = open('words.txt', 'w')
file.write("apache\ndecal\ndid\nneep\nnoon\nrefer\nriver")
with open('words.txt', 'r') as file:
    line = None
    while line != '':

        line = file.readline()
        line.strip('\n')
        y = list(line)
        print(y)
for j in y:
    is_palindrome = 0
    for i in range(len(j)//2):
        if j[i] == j[-i-1]:
            is_palindrome += 1
        else:
            break
        if(is_palindrome == len(j)//2):
            print(j)