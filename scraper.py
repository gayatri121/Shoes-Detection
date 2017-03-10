#import urllib
#from urllib import request
#from requests import get
#file = open('C:\\Users\\Gayatri\\Documents\\Research', 'wb')
#response = get('http://www.interempresas.net/FotosArtProductos/P39704.jpg')
#print (response)
#file.write(response)
#file.close()
#a=request.urlretrieve('http://www.interempresas.net/FotosArtProductos/P39704.jpg','C:\\Users\\Gayatri\\Downloads')

import urllib.request

def download_web_image(url,image_name):
    
    
    urllib.request.urlretrieve(url,image_name)

#img_url = 'http://www.interempresas.net/FotosArtProductos/P39704.jpg'
lines = [line.rstrip('\n') for line in open('Image_url.txt','r')]
print(lines[0])
count=0
for items in lines:
    print(count)
    count=count+1
    try:
        download_web_image(items,'Image_url\\0A'+str(count)+'.jpg')
    except:
        count=count-1
       
    #break
#print(count)