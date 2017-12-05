#-*- coding: utf-8 -*-

# midi segment feature
f_t = open('Midi_Traditional_Fea.txt','r')
f_n = open('Midi_DAE_Fea.txt','r')

n=0
list1=[]
for i in f_t.readlines():
    n+=1
    s1=i.strip()
    list1.append(s1)
f_t.close()

m=0
list2=[]
for j in f_n.readlines():
    m+=1
    s2=j.strip()
    list2.append(s2)
f_n.close()
 
fin_fea=open('Midi_fin_fea.txt','w')
for i in range(n):
    s=list1[i]+' '+list2[i]
    fin_fea.write(s+'\n')
    print(s)
fin_fea.close()
