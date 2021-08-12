import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import re
def getLinks():
    br =  webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe')#,options=options)
    br.get("http://kathadata.host/otherPages/SGGSJIKatha.html")
    content=br.page_source.encode('utf-8').strip()
    soup=bs(content,"lxml")
    bars=soup.findAll("a")
    audios={}
    for i in bars:
        audios[i.text.strip()]=i["href"]
    for i in audios:
        print(f"'{i}':'{audios[i].replace('..','http://kathadata.host').replace(' ','%20')}',")
    return audios
    
# audios=getLinks()
audios={
   'Ang 1312 - ਕਾਨੜਾ ਛੰਤ ਮਹਲਾ ੫ Part 1.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang%201312%20-%2011111%20111%201111%201%20Part%201.mp3',
    'Ang 1312 - ਕਾਨੜਾ ਛੰਤ ਮਹਲਾ ੫ Part 2.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang%201312%20-%2011111%20111%201111%201%20Part%202.mp3',
    'Ang 1312 - ਕਾਨੜੇ ਕੀ ਵਾਰ ਮਹਲਾ ੪.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang%201312%20-%2011111%2011%20111%201111%201.mp3',
    'Ang_1027_ਬਾਲਕੁ_ਮਰੈ_ਬਾਲਕ_ਕੀ_ਲੀਲਾ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_1027_11111_111_1111_11_1111_1.mp3',
    'Ang_1310_ਮਨੁ_ਗੁਰਮਤਿ_ਰਸਿ_ਗੁਨ_ਗਾਵੈਗੋ_॥_Part_1.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_1310_111_111111_111_111_111111_1_Part_1.mp3',
    'Ang_1310_ਮਨੁ_ਗੁਰਮਤਿ_ਰਸਿ_ਗੁਨ_ਗਾਵੈਗੋ_॥_Part_2.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_1310_111_111111_111_111_111111_1_Part_2.mp3',
    'Ang_1310_ਮਨੁ_ਹਰਿ_ਰੰਗਿ_ਰਾਤਾ_ਗਾਵੈਗੋ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_1310_111_111_1111_1111_111111_1.mp3',
    'Ang_1395_ਗੁਰੁ_ਅਮਰਦਾਸੁ_ਪਰਸੀਐ_ਪੁਹਮਿ_ਪਾਤਿਕ_ਬਿਨਾਸਹਿ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_1395_1111_1111111_11111_11111_11111_1111111_1.mp3',
    'Ang_487_ਕਹਾ_ਭਇਓ_ਜਉ_ਤਨੁ_ਭਇਓ_ਛਿਨੁ_ਛਿਨੁ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_487_111_111_11_111_111_1111_1111_1.mp3',
    'Ang_526_ਗੂਜਰੀ_ਸ੍ਰੀ_ਜੈਦੇਵ_ਜੀਉ_ਕਾ_ਪਦਾ_Part_1.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_526_11111_1111_11111_111_11_111_Part_1.mp3',
    'Ang_526_ਗੂਜਰੀ_ਸ੍ਰੀ_ਜੈਦੇਵ_ਜੀਉ_ਕਾ_ਪਦਾ_Part_2.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_526_11111_1111_11111_111_11_111_Part_2.mp3',
    'Ang_563_ਅੰਤਰਜਾਮੀ_ਸੋ_ਪ੍ਰਭੁ_ਪੂਰਾ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_563_11111111_11_11111_1111_1.mp3',
    'Ang_563_ਤੂ_ਵਡ_ਦਾਤਾ_ਅੰਤਰਜਾਮੀ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_563_11_11_1111_11111111_1.mp3',
    'Ang_564_565_ਵਡਹੰਸੁ_ਮਹਲਾ_੩_ਅਸਟਪਦੀਆ_Part_1.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_564_565_111111_1111_1_1111111_Part_1.mp3',
    'Ang_564_565_ਵਡਹੰਸੁ_ਮਹਲਾ_੩_ਅਸਟਪਦੀਆ_Part_2_ਜਿਹਵਾ_ਸਚੀ_ਸਚਿ_ਰਤੀ_ਤਨੁ_ਮਨੁ.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_564_565_111111_1111_1_1111111_Part_2_11111_111_111_111_111_111.mp3',
    'Ang_564_ਵਡਹੰਸੁ_ਮਹਲਾ_੫_ਘਰੁ_੨_Part_2_ਹਉ_ਭਈ_ਉਡੀਣੀ_ਕੰਤ_ਕਉ_ਅੰਮਾਲੀ_ਸੋ.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_564_111111_1111_1_111_1_Part_2_11_11_11111_111_11_111111_11.mp3',
    'Ang_565_566_ਕਾਇਆ_ਕੂੜਿ_ਵਿਗਾੜਿ_ਕਾਹੇ_ਨਾਈਐ_॥_Part_1.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_565_566_1111_1111_111111_1111_1111_1_Part_1.mp3',
    'Ang_565_566_ਕਾਇਆ_ਕੂੜਿ_ਵਿਗਾੜਿ_ਕਾਹੇ_ਨਾਈਐ_॥_Part_2_ਤਾ_ਮੈ_ਕਹਿਆ_ਕਹਣੁ.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_565_566_1111_1111_111111_1111_1111_1_Part_2_11_11_1111_1111.mp3',
    'Ang_565_566_ਕਾਇਆ_ਕੂੜਿ_ਵਿਗਾੜਿ_ਕਾਹੇ_ਨਾਈਐ_॥_Part_3_ਵਾਰੀ_ਖਸਮੁ_ਕਢਾਏ_ਕਿਰਤੁ.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_565_566_1111_1111_111111_1111_1111_1_Part_3_1111_1111_1111_11111.mp3',
    'Ang_565_566_ਕਾਇਆ_ਕੂੜਿ_ਵਿਗਾੜਿ_ਕਾਹੇ_ਨਾਈਐ_॥_Part_4_ਸਭ_ਉਪਾਈਅਨੁ_ਆਪਿ_ਆਪੇ.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_565_566_1111_1111_111111_1111_1111_1_Part_4_11_1111111_111_111.mp3',
    'Ang_565_ਮਨੂਆ_ਦਹ_ਦਿਸ_ਧਾਵਦਾ_ਓਹੁ_ਕੈਸੇ_ਹਰਿ_ਗੁਣ_ਗਾਵੈ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_565_1111_11_111_11111_111_1111_111_111_1111_1.mp3',
    'Ang_566_ਤੇਰਾ_ਵਖਤੁ_ਸੁਹਾਵਾ_ਅੰਮ੍ਰਿਤੁ_ਤੇਰੀ_ਬਾਣੀ_॥_3_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_566_1111_1111_111111_11111111_1111_1111_1_3_1.mp3',
    'Ang_567_568_ਆਪਣੇ_ਪਿਰ_ਕੈ_ਰੰਗਿ_ਰਤੀ_ਮੁਈਏ_ਸੋਭਾਵੰਤੀ_ਨਾਰੇ_॥_Part_1.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_567_568_1111_111_11_1111_111_1111_11111111_1111_1_Part_1.mp3',
    'Ang_567_568_ਆਪਣੇ_ਪਿਰ_ਕੈ_ਰੰਗਿ_ਰਤੀ_ਮੁਈਏ_ਸੋਭਾਵੰਤੀ_ਨਾਰੇ_॥_Part_2.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_567_568_1111_111_11_1111_111_1111_11111111_1111_1_Part_2.mp3',
    'Ang_567_ਤੇਰੇ_ਬੰਕੇ_ਲੋਇਣ_ਦੰਤ_ਰੀਸਾਲਾ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_567_1111_1111_1111_111_111111_1.mp3',
    'Ang_568_569_ਗੁਰਮੁਖਿ_ਸਭੁ_ਵਾਪਾਰੁ_ਭਲਾ_ਜੇ_ਸਹਜੇ_ਕੀਜੈ_ਰਾਮ_॥_Part_1.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_568_569_1111111_111_111111_111_11_1111_1111_111_1_Part_1.mp3',
    'Ang_568_569_ਗੁਰਮੁਖਿ_ਸਭੁ_ਵਾਪਾਰੁ_ਭਲਾ_ਜੇ_ਸਹਜੇ_ਕੀਜੈ_ਰਾਮ_॥_Part_2.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_568_569_1111111_111_111111_111_11_1111_1111_111_1_Part_2.mp3',
    'Ang_568_569_ਗੁਰਮੁਖਿ_ਸਭੁ_ਵਾਪਾਰੁ_ਭਲਾ_ਜੇ_ਸਹਜੇ_ਕੀਜੈ_ਰਾਮ_॥_Part_3.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_568_569_1111111_111_111111_111_11_1111_1111_111_1_Part_3.mp3',
    'Ang_568_569_ਗੁਰਮੁਖਿ_ਸਭੁ_ਵਾਪਾਰੁ_ਭਲਾ_ਜੇ_ਸਹਜੇ_ਕੀਜੈ_ਰਾਮ_॥_Part_4.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_568_569_1111111_111_111111_111_11_1111_1111_111_1_Part_4.mp3',
    'Ang_569_570_ਰਤਨ_ਪਦਾਰਥ_ਵਣਜੀਅਹਿ_ਸਤਿਗੁਰਿ_ਦੀਆ_ਬੁਝਾਈ_ਰਾਮ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_569_570_111_11111_1111111_1111111_111_11111_111_1.mp3',
    'Ang_569_ਮਨ_ਮੇਰਿਆ_ਤੂ_ਸਦਾ_ਸਚੁ_ਸਮਾਲਿ_ਜੀਉ_॥_Part_1.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_569_11_11111_11_111_111_11111_111_1_Part_1.mp3',
    'Ang_569_ਮਨ_ਮੇਰਿਆ_ਤੂ_ਸਦਾ_ਸਚੁ_ਸਮਾਲਿ_ਜੀਉ_॥_Part_2.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_569_11_11111_11_111_111_11111_111_1_Part_2.mp3',
    'Ang_585_ਸੋ_ਸਚਾ_ਸਚੁ_ਸਲਾਹੀਐ_ਜੇ_ਸਤਿਗੁਰੁ_ਦੇਇ_ਬੁਝਾਏ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_585_11_111_111_111111_11_1111111_111_11111_1.mp3',
    'Ang_596_ਮਨੁ_ਹਾਲੀ_ਕਿਰਸਾਣੀ_ਕਰਣੀ.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_596_111_1111_1111111_1111.mp3',
    'Ang_632_ਮਾਈ_ਮੈ_ਕਿਹਿ_ਬਿਧਿ_ਲਖਉ_ਗੁਸਾਈ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_632_111_11_1111_1111_111_11111_1.mp3',
    'Ang_665_ਕਾਚਾ_ਧਨੁ_ਸੰਚਹਿ_ਮੂਰਖ_ਗਾਵਾਰ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_665_1111_111_11111_1111_11111_1.mp3',
    'Ang_672_ਜਿਸਕਾ_ਤਨੁ_ਮਨੁ_ਧਨੁ_ਸਭੁ_ਤਿਸਕਾ_ਸੋਈ_ਸੁਘੜੁ_ਸੁਜਾਨੀ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_672_11111_111_111_111_111_11111_111_11111_111111_1.mp3',
    'Ang_680_ਜਾ_ਕਉ_ਹਰਿ_ਰੰਗੁ_ਲਾਗੋ_ਇਸੁ_ਜੁਗ_ਮਹਿ.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_680_11_11_111_1111_1111_111_111_111.mp3',
    'Ang_684_ਬੰਦਨਾ_ਹਰਿ_ਬੰਦਨਾ_ਗੁਣ_ਗਾਵਹੁ_ਗੋਪਾਲ_ਰਾਇ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_684_11111_111_11111_111_11111_11111_111_1.mp3',
    'Ang_694_ਪਹਿਲ_ਪੁਰੀਏ_ਪੁੰਡਰਕ_ਵਨਾ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_694_1111_11111_111111_111_1.mp3',
    'Ang_696_ਮੇਰੈ_ਹੀਅਰੈ_ਰਤਨੁ_ਨਾਮੁ_ਹਰਿ_ਬਸਿਆ.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_696_1111_11111_1111_1111_111_1111.mp3',
    'Ang_703_ਦਰਸਨ_ਪਿਆਸੀ_ਦਿਨਸੁ_ਰਾਤਿ.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_703_1111_11111_11111_1111.mp3',
    'Ang_710_ਦਇਆ_ਕਰਣੰ_ਦੁਖ_ਹਰਣੰ_ਉਚਰਣੰ_ਨਾਮ_ਕੀਰਤਨਹ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_710_111_1111_111_1111_11111_111_111111_1.mp3',
    'Ang_715_ਰੂੜੋ_ਮਨੁ_ਹਰਿ_ਰੰਗੋ_ਲੋੜੈ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_715_1111_111_111_1111_1111_1.mp3',
    'Ang_720_ਹਰਿਜਨੁ_ਰਾਮ_ਨਾਮ_ਗੁਨ_ਗਾਵੈ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_720_111111_111_111_111_1111_1.mp3',
    'Ang_758_759_ਅੰਦਰਿ_ਸਚਾ_ਨੇਹੁ_ਲਾਇਆ_ਪ੍ਰੀਤਮ_ਆਪਣੈ_॥_Part_1.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_758_759_11111_111_1111_1111_111111_1111_1_Part_1.mp3',
    'Ang_758_759_ਅੰਦਰਿ_ਸਚਾ_ਨੇਹੁ_ਲਾਇਆ_ਪ੍ਰੀਤਮ_ਆਪਣੈ_॥_Part_2.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_758_759_11111_111_1111_1111_111111_1111_1_Part_2.mp3',
    'Ang_766_ਜਿਨਿ_ਕੀਆ_ਤਿਨਿ_ਦੇਖਿਆ_ਜਗੁ_ਧੰਧੜੈ_ਲਾਇਆ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_766_1111_111_1111_11111_111_11111_1111_1.mp3',
    'Ang_791_792_ਕਿਸਹੀ_ਕੋਈ_ਕੋਇ_ਮੰਞੁ_ਨਿਮਾਣੀ_ਇਕੁ_ਤੂ_॥.mp3':'http://kathadata.host/Kathas/AdiMaharaj/Ang_791_792_11111_111_111_1111_111111_111_11_1.mp3',
}

def getAngNums(file):
    angRe=re.compile(r"(Ang(_||\s)([0-9]{1,4})((\_||\s)[0-9]{1,4})?)")
    b=angRe.search(file)
    ang1,ang2=(b.group(3),b.group(4))
    if ang2: #if ang2 is not None then
        return [int(ang1),int(ang2[1:])]
    return [int(ang1)]


def getObjForJs(files): #files is a dict
    finalObj={}#format is that keys will be the AngNum and value is the kathas for that ang
    for file in files:
        angNums=getAngNums(file)
        for angNum in angNums:
            theIndexToSlice=""
            if "Part" in file:
                theIndexToSlice=file.index("Part")
            else:
                theIndexToSlice=file.index(".mp3")

            if angNum not in finalObj:
                finalObj[angNum]=[{"title":file[:theIndexToSlice],'links':[files[file]]}]
            else: #ang already in obj

                broken=0 #this will be 1 if the for loop below breaks
                for katha in finalObj[angNum]:
                    if katha['title']==file[:theIndexToSlice]:
                        katha["links"].append(files[file])
                        broken+=1
                        break
                if not broken:
                    finalObj[angNum].append({"title":file[:theIndexToSlice],'links':[files[file]]})

    f=open("./pyWebScrape/kathasFromkathaData.js",'w',encoding="utf-8")
    f.write("const a={")
    for i in finalObj:
        f.write(f'"{i}":{finalObj[i]},\n')
    f.write("}")
    f.close()


getObjForJs(audios)
