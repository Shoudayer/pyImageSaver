from bs4 import BeautifulSoup as bs
import requests
import sys

class pyImageSaver():
    
    def __init__(self,baseUrl=''):
        self.baseUrl=baseUrl
   
    def getUniqueSrc(self,samples):
        srcs=list()
        for img in samples:
            imgsrc=img['src']
            if(self.isInternal(imgsrc)):
                imgsrc=self.concat(imgsrc)
            if imgsrc not in srcs:
                srcs.append(imgsrc)  
        return srcs

    def concat(self,internalLink):
        if(self.baseUrl[-1]=='/'):
            baseUrl=self.baseUrl[:-1]
        else:
            baseUrl=self.baseUrl
            
        if(internalLink[0]=='/'):
            return(baseUrl+internalLink)
        else:
            return(baseUrl+'/'+internalLink)
        
    def isInternal(self,src):
        if("http://" in src or "https://" in src):
            return False
        else:
            return True
        
    def getFileName(self,url):
        if(url[-1]=='/'):
            url=url[:-1]
        return(url.split('/')[-1])    

    def saveImg(self,url,name="picture.png"):
        if('/' not in name):
            with open(name, 'wb') as handle:
                    response = requests.get(url, stream=True)
                    if not response.ok:
                        print (response)
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)
                        
    def getBaseUrl(self,url):
        baseurl=''
        if('http://'in url or 'https://' in url):
            for e in url.split('/')[:3]:
                baseurl+=e+'/'
        else:
            for e in url.split('/')[:1]:
                baseurl+=e+'/'
        return baseurl

    def crawlImgs(self,url,classFilter=''):
        if(self.baseUrl==''):
            self.baseUrl = self.getBaseUrl(url)
        page = requests.get(url,headers={'user-agent': 'Mozilla/5.0'})
        soup = bs(page.content,"html5lib")
        samples = soup.find_all("img")
        return (self.getUniqueSrc(samples=samples))
    
    def saveImgsWName(self,imgsList):
        for img in imgsList:
            print('saving :'+self.getFileName(img))
            self.saveImg(img,self.getFileName(img))

    def saveImgsWNumber(self,imgsList,baseurl):
        i = 0
        for img in imgsList:
            i+=1
            print('saving : '+'%04d'%i+'.png')
            saveImg(img,'%04d'%i+'.png')
            
            

if __name__ == "__main__":
    url=''
    pimas=pyImageSaver()
    if(len(sys.argv)<2 or sys.argv[1]==''):
        url=input('No url passed, please specify your url : ')
    elif('.' in  sys.argv[1] and sys.argv[1]!=''):
        url=str(sys.argv[1])
        print(str(url)+" received ")
    elif(';' in sys.argv[1]):
        urls=sys.argv[1].split(';')
        print('list received : '+str(urls))
        for url in urls:
            pimas.saveImg(url=url,name=pimas.getFileName(url))
    else:
        print("Wrong url")
    
    if('.' in url):
        imgs=pimas.crawlImgs(url)
        pimas.saveImgsWName(imgsList=imgs)
        
        
        
        
        
