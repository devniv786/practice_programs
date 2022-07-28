
s1 = 'aabcdef'
s2='abbcfde'
a=[]
common=''
for i,val in enumerate(s1,start=0):
    if val==s2[i]:
        common=common+val
    elif len(common)==0:
            continue
    else:
        a.append(common)
        common=''

a.sort(key=-(len))
print(a)
