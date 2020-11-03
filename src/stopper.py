f = open('save1.txt', 'r')
contents = f.read()
f.close()

if int(contents):
    f = open('save1.txt', 'a+')
    f.truncate(0)
    f.close()
    exit(0)

else:
    f = open('save1.txt', 'a+')
    f.truncate(0)
    f.close()
    print('Something went wrong!')
    input()
    exit(0)