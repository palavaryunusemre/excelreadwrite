import pandas as pd

path="TDMS.xls"
sheet_name1="TDMS"
sheet_name2="Sayfa1"
sheet_name3="Sayfa2"
data=pd.read_excel(path,sheet_name=sheet_name1)
df=pd.DataFrame(data)

data1=pd.read_excel(path,sheet_name=sheet_name2)
df2=pd.DataFrame(data1)

data2=pd.read_excel(path, sheet_name=sheet_name3)
df3=pd.DataFrame(data2)


#---------------------------data
fisDate=df['FİŞ TARİHİ']
fisNo=df['FİŞ NO']
tfiNo=df['TAŞINIR İŞLEM FİŞ NO']
dsc=df['DSC']
borc=df['BORÇ']
alacak=df['ALACAK']
#-----------------------data1
data1Tifno=df2['TİF No']
#------------------------data2
data2tifno=df3['Tif NO']
#--------------------------
dizi=[]
"""for i in range(len(data2tifno)):
    if (data1Tifno[i] == data2tifno[i]):
       dizi.append('true')
       i=i+1
    else:
        dizi.append('false')
        i=i+1"""
sayac=0
"""for i in data2tifno:
    if (data2tifno[i].values == data1Tifno[sayac].values):
        dizi.append('true')
    else:
        dizi.append('false')
"""


#----------------------------------------------------
fisNo=fisNo.fillna("")
fisNo=fisNo.to_numpy()
tfiNo=tfiNo.fillna("")
x=tfiNo.to_numpy()
fisDate=fisDate.to_numpy()
dsc=dsc.to_numpy()
borc=borc.to_numpy()
alacak=alacak.to_numpy()
#-----------------------------------------------------
resultTfi = pd.DataFrame()
resultNo=pd.DataFrame()
resultDate=pd.DataFrame()
resultDsc=pd.DataFrame()
resultBorc=pd.DataFrame()
resultAlacak=pd.DataFrame()
resultTfiCheck=pd.DataFrame()
#-----------------------------------------------

x=tfiNo.str.split(r"-|/")


arrTfi=[]
arrDate=[]
arrNo=[]
arrDsc=[]
arrBorc=[]
arrAlacak=[]


index=0
for i in x:
    for j in i:
        arrTfi.append(j)
        arrNo.append(fisNo[index])
        arrDate.append(fisDate[index])
        arrDsc.append(dsc[index])
        arrBorc.append(borc[index]/len(i))
        arrAlacak.append(alacak[index])
    index += 1


resultTfi['Tif NO'] = pd.DataFrame(arrTfi)
resultNo['FİŞ NO'] = pd.DataFrame(arrNo)
resultDate['FİŞ TARİHİ']=pd.DataFrame(arrDate)
resultDsc ['DSC']=pd.DataFrame(arrDsc)
resultBorc ['BORÇ']=pd.DataFrame(arrBorc)
resultAlacak['ALACAK']=pd.DataFrame(arrAlacak)
resultDf = pd.concat([resultDate,resultNo,resultTfi,resultDsc,resultBorc,resultAlacak],axis=1)  # axis=1 ile verileri yan yana olacak şekilde excelle aktardım."""


resultDf.to_excel('result.xlsx')




