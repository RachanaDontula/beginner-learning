f = open('demo.txt','r')  # read mode

print(f.read())

f1 = open('demo.png', 'rb')  # binary mode
# we but b for images, coz, image will be in binary numbers.

f2 = open('mypic.jpg','wb')
for i in f1:
    f2.write(i)

"""
r- read mode
w- write mode
f.read
f.write
f.readline
b- binary
rb- read binary
wb- write binary
"""