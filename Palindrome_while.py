n=int(input('N: '))
l=[]
i=1
c=0
while True:
    y=True
    if str(i)==str(i)[::-1]:
        if i>=2:
            for j in range(2,i):
                if i%j==0:
                    y=False
                    break     
            if y:
                c+=1
                l.append(i)
    if c==(n):
        break
    i+=1
print(f"{n}th Prime Palindrome Number Is:",l[n-1])