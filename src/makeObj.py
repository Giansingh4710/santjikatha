
# f=open("./src/kathasByAng.js",'r',encoding="utf-8")
# a=f.readlines()
# print(len(a))

def getAllObjs(a):
    # in the end i just looped through the list and wrote each iteration in kathasByKeywords.js file and fixed erros manually
    lst=[]
    q=[0,0]
    for i in range(len(a)):
        if "{" in a[i]:
            bracket=a[i].strip()
            if len(bracket)==1:
                q[0]=i
        if "}" in a[i]:             
            bracket=a[i].strip()
            if len(bracket)==2:
                q[1]=i
            kathaObj="".join(a[q[0]:q[1]+1])
            lst.append(kathaObj)
    ans=lst[:-2] #last 2 are duplicates
    return ans  



f=open("./src/kathasByKeyword.js",'r',encoding="utf-8")
a=f.readlines()[1:-1] #first and last not needed
titles=[]
links=[]
topOfObj=0
for i in range(len(a)):
    if "{" in a[i]:
        title=a[i].split(":")[0]
        titles.append(title)
        topOfObj=i+1
    if "}" in a[i]:
        link=a[topOfObj:i]
        allLinksInThisTitle=[]
        theLinks=link[1:-1]
        for j in theLinks:
            allLinksInThisTitle.append(j.strip())
        links.append(allLinksInThisTitle)
print(len(titles))
print(len(links))

ansObj={}
for i in range(len(links)):
    if titles[i] not in ansObj:
        ansObj[titles[i]]={"links":links[i]}
    else:
        ansObj[titles[i]]["links"]+=links[i]
import pyperclip
pyperclip.copy(str(ansObj))
print(len(ansObj))














# def numsIn(line):
#     if "1" in line or "2" in line or"3" in line or"4" in line or"5" in line or"6" in line or"7" in line or"8" in line or"9" in line:
#         return True
#     return False

# for i in range(len(a)):
#     if numsIn(a[i]) and "[" in a[i] and ":" in a[i]:
#         angPart=a[i].split(":")[0]
#         try:
#             titlePart=a[i+2][:-1].split("title: ")[1].strip()
#             titlePart=titlePart[:-1]+": [" 
#         except:
#             titlePart=a[i+3][:-1].strip()
#             titlePart=titlePart[:-1]+": [" 
#             a[i+3]=" "
#         a[i]=titlePart
#         a[i+2]="ang: "+angPart+","

# f=open("./src/kathasByKeyword.js",'w',encoding="utf-8")
# for i in range(len(a)):
#     theNewLine=a[i]
#     if a[i][-1]!="\n":
#         theNewLine+="\n"
#     f.write(theNewLine)

    