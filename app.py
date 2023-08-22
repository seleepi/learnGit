list = ['samsung', 'kakao', 'naver', 'sinpung']

file = open('list.txt', 'w')
for i in list:
    file.write(i)
    file.write('\n')
file.close()

file = open('list.txt', 'r')

print(file.read())

file.close()



for i in range(2, 10):
    for j in range(1, 10):
        print(i, ' x ', j, ' = ', i*j)
    print('---------------')
