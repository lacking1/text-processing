#-*- coding: utf-8 -*-

# wav segment feature
import os

def mergeTwofiles(file1, file2):
    os.chdir('C:\\Python35\\projects\\allWavFeaFile\\1400_50d_DAE')

    f_t = open(file1,'r')
    
    n=0
    list1=[]
    for i in f_t.readlines():
        n+=1
        s1=i.strip()
        list1.append(s1)
    f_t.close()

    os.chdir('C:\\Python35\\projects\\allWavFeaFile\\1400Traditional')
    f_n = open(file2,'r')
    m=0
    list2=[]
    for j in f_n.readlines():
        m+=1
        s2=j.strip()
        list2.append(s2)
    f_n.close()

    os.chdir('C:\\Python35\\projects\\Wav_finalFea')
    fin_fea=open(file1,'w')
    for i in range(n):
        s=list1[i]+' '+list2[i]
        fin_fea.write(s+'\n')
        print(s)
    fin_fea.close()

nameList = open('wavnameList.txt','r')
numWav = 0
for ii in nameList.readlines():
    wavname_dae = ii.strip()
    print (wavname_dae)
    
    wavname_dae = wavname_dae + '.txt'
    #重跑一下基线写系统，改一下输出wav的名字为1,2,3，。。。
    #然后把DAE跑的特征和1,2,3放入同一个文件夹下
    numWav += 1
    wavname_trad = str(numWav) + '.txt'
    print (wavname_trad)
    mergeTwofiles(wavname_dae,wavname_trad)

nameList.close()
