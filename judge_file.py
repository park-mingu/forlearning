file = open('words.txt', 'w')
file.write("Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.")
file = open('words.txt', 'r')
x = file.read()
y = x.split()
for i in y:
    z = i.strip(',.')
    if 'c' in z:
        print(z)


