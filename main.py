import pandas as pd

path=".xls"
sheet_name1="TDMS"
sheet_name2="Sayfa1"
data=pd.read_excel(path,sheet_name=sheet_name1)
df=pd.DataFrame(data)

fisDate=df['fistarihi']
fisNo=df['fisno']
tfiNo=df['tasinirislemno']
dsc=df['dsc']
borc=df['borc']
alacak=df['alacak']
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
#-----------------------------------------------


x=tfiNo.str.split('-')


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
        arrBorc.append(borc[index])
        arrAlacak.append(alacak[index])
    index+=1




resultTfi['Tif NO'] = pd.DataFrame(arrTfi)
resultNo['FİŞ NO'] = pd.DataFrame(arrNo)
resultDate['FİŞ TARİHİ']=pd.DataFrame(arrDate)
resultDsc ['DSC']=pd.DataFrame(arrDsc)
resultBorc ['BORÇ']=pd.DataFrame(arrBorc)
resultAlacak['ALACAK']=pd.DataFrame(arrAlacak)
resultDf = pd.concat([resultDate,resultNo,resultTfi,resultDsc,resultBorc,resultAlacak],axis=1)  # axis=1 ile verileri yan yana olacak şekilde excelle aktardım."""


resultDf.to_excel('result.xlsx')




