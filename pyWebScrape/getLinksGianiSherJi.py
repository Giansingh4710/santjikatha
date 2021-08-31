import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import re
def getLinks():
    br =  webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe')#,options=options)
    br.get("http://kathadata.host/otherPages/gianiSherSinghJi/SGGSJIKatha.html")
    content=br.page_source.encode('utf-8').strip()
    soup=bs(content,"lxml")
    bars=soup.findAll("a")
    audios={}
    for i in bars:
        audios[i.text.strip()]=i["href"]
    for i in audios:
        print(f"'{i}':'{audios[i].replace('..','http://kathadata.host').replace(' ','%20')}',")
    return audios
    
audios=getLinks()


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
