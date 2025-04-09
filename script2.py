import string, random
all=string.ascii_letters+string.digits+string.punctuation
def generateletters():
    task=True
    g=True
    letters=string.ascii_letters
    l=int(input())
    result=''
    e=''
    while task==True:
    
        exclude=input('what letter do you want to exclude(one letter at a time)(qq-to finish)')
        
        if exclude in letters:
            letters=letters.replace(exclude,'')
        elif exclude=='qq':
            task=False
        if exclude in e:
            print('this letter is already excluded')
            continue
        e+=exclude
        result=random.sample(letters,l)


                     
    return result
def generatedigits():
    task=True
    digits=string.digits
    l=int(input())
    result=''
    e=''
    g=True
    while task==True:
    
        exclude=input('what number do you want to exclude(one number at a time)(qq-to finish)')
        
        if exclude in digits:
            digits=digits.replace(exclude,'')
        elif exclude=='qq':
            task=False
        if exclude in e:
            print('this number is already excluded')
            continue
        e+=exclude
        result=random.sample(digits,l)  
                
    return result
password=generateletters()+generatedigits()
print(len(password))
print(password)
