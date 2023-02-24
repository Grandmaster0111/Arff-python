
import random
def lo(x):
    for i in range(4):
        o=random.randint(1,9)
        x.append(str(o))
    return x

def savfil(name,*b):
    n=len(b[0])
    with open('usef.arff','w') as f:
        f.writelines(['@relation ', name,'\n'])
        with open('usef.arff','a') as m:
            m.writelines(['\n@attribute ',b[0][0],' {'])
            for i in range(n):
                m.writelines(['\n@attribute ',b[0][i],' {']) 
                m.writelines([b[i+1][0]])
                for j in range(1,len(b[i+1])):
                    m.writelines([',',b[i+1][j]])
                m.writelines(['}'])  
            m.writelines(['\n','\n@data\n'])
def no(*a):
    n=len(a)
    new=[]
    s=random.choice(a[0])
    new.append(s)
    for i in range(1,n):
        new.append(',')
        s=random.choice(a[i])
        new.append(s)
    with open('usef.arff','a') as f:
        for i in range(len(new)):
            f.write(new[i])
        f.write('\n')
    return new
name='cares'
n0 = ['n1','n2','n3','n4','n5']
n1=['a','b','c']
n2=[]
n3=[]
n4=['TRUE','FALSE']
n5=['YES','NO']
lo(n2)
lo(n3)
savfil(name,n0,n1,n2,n3,n4,n5)
for i in range(10):
    no(n1,n2,n3,n4,n5)

