import string, random
letters=string.ascii_letters
digits=string.digits
punctuation=string.punctuation
all=letters+digits+punctuation
print(len((letters+digits+punctuation)))
print('enter how long your password should be')
l=0
d=0
p=0
c=''
length=int(input())
for i in range(length):
    rand=random.randint(0,93)
    if all[rand] in letters:
        l+=1
        if l<=length//3 and c.count(all[rand])<2:
            c+=all[rand]
        else:
            rand=random.randint(0,93)
            while all[rand] in letters:
                rand=random.randint(0,93)
            c+=all[rand]
    elif all[rand] in digits:
        d+=1
        if l<=length//3 and c.count(all[rand])<2:
            c+=all[rand]
        else:
            rand=random.randint(0,93)
            while all[rand] in digits:
                rand=random.randint(0,93)
            c+=all[rand]
    if all[rand] in punctuation:
        p+=1
        if l<=length//3 and c.count(all[rand])<2:
            c+=all[rand]
        else:
            rand=random.randint(0,93)
            while all[rand] in punctuation:
                rand=random.randint(0,93)
            c+=all[rand]
print(c)