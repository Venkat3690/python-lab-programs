a= input('Enter your sentence: ')
a=a.lower()
n=len(a)
flag=0
for i in range(n) :
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        print("vowel {} found at index {}".format(a[i],i))
        flag+=1
if(flag==0):
    print("vowels not found in the sentence")
