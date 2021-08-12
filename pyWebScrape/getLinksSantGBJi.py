#For khata of sant Giani Gurbachan Singh ji
import requests,re
from bs4 import BeautifulSoup as bs


#only links with titles is returned, no folder inside of folder
def onlyLinks(url):
    res=requests.get(url)
    soup=bs(res.text, "lxml")
    khatas=soup.find_all("table",cellpadding=4)
    khatas=khatas[4:-2]
    folderWithLinks={}
    for file in khatas:
        try:
            title=file.find("font",size="2",color="0069c6").text
        except AttributeError:
            print("No Good. But we caught it!!")#It got the ALL the text from the drop down menu and those don't have a 'color=0069c6' attribute
            continue
        newUrl="http://www.gurmatveechar.com/"+file.find("a").get("href")
        if "mp3" in newUrl.lower():
            if title not in folderWithLinks:
                folderWithLinks[title]=[newUrl]
            else:
                folderWithLinks[title].append(newUrl)
        else:
            newFolderWithLinks=onlyLinks(newUrl)
            folderWithLinks.update(newFolderWithLinks) 
    return folderWithLinks

def santJiKhataInOrder(url):
    angs=re.compile(r"(Ang(-||\s)([0-9]{1,4})(\+[0-9]{1,4})?)")
    kathas=onlyLinks(url)
    theAngs={}
    for title in kathas:
        b=angs.search(title)
        ang1=b.group(3) #the third group gives the ang1
        ang2=b.group(4) #the slice remove the '+' sign
        if ang2: #if ang2 is not equal to 'None' then 
            ang2=ang2[1:]
        for angNum in [ang1, ang2]:
            if angNum: #if angNum is a number and not None
                newAdd={'title':title,'link':kathas[title]}
                if angNum not in theAngs:
                    theAngs[angNum]=[newAdd]
                else:
                    theAngs[angNum].append(newAdd)
    return theAngs
url="http://www.gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F01_Puratan_Katha%2FSant_Gurbachan_Singh_%28Bhindran_wale%29%2FGuru_Granth_Sahib_Larivaar_Katha"
# newUrl="https://gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F01_Puratan_Katha%2FSant_Gurbachan_Singh_%28Bhindran_wale%29%2FGuru_Granth_Sahib_Larivaar_Katha%2FVolume_08_Ang_0660-0761"
allKathas=santJiKhataInOrder(url)

f=open("./sikhStuff/santjikatha/pyWebScrape/kathas.js",'w')
f.write("export const katha=\n")
f.write(str(allKathas))
f.close()





