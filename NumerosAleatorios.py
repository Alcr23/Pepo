from pickle import APPEND
import random
import string

col1 = []
col2 = []
col3 = []
col4 = []


for i in range(100):
    col1.append(random.randint(0, 500))
    col3.append(random.randint(0, 500))
    col4.append(random.randint(0, 500))
    

doc = open("p5.txt", 'w')
for j in range(len(col1)):
    cl1 = ('{} ' .format(col1[j]))
    doc.write(cl1)
    randlowercase = chr(random.randint(ord('a'), ord('z')))
    col2 = ('{} '.format(randlowercase))
    doc.write(col2)
    #randuppercase = chr(random.randint(ord('A'), ord('Z')))
    #doc.write('{} '.format(randuppercase))
    res = ('{} {}\n' .format(col3[j], col4[j]))
    doc.write(res)
doc.close()
