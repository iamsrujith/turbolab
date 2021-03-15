word=input()
li=list(word)
n=12
count=0
for i in li:
    count+=1
    if count<=12:
        print(i, end='')
