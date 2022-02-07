from codecs import xmlcharrefreplace_errors


for x in range(151):
    print(x)

for x in range(0,151,5):
    print(x)

for x in range(1,101):
    if x%10==0:
        print ("Coding Dojo")
    elif x%5 == 0:
        print ("Coding")

sum=0
for x in range(500,000):
    if x%2 == 1:
        sum += 1
        continue
    print (sum)

for x in range(2018, -1, -4):
    print(x)

lowNum = 3
highNum = 300
mult = 3
for x in range(highNum, -lowNum, -mult):
    print(x)