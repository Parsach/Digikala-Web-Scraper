from pySmartDL import SmartDL
import re
import os
links=open('img_url.text','r')
count=0
directory='download'
x=input('Do You Want Download All images?(Y,N)')
if x=='Y' or x=='y':
    for link in links.readlines():
        check_pruduct=re.search(r'(dkp-.*)',str(link))
        if check_pruduct != None :
            print(check_pruduct.group(1))
            directory=check_pruduct.group(1)
            
    
        else:
            count+=1
            url ='%s'%link
            dest = "C:\\digi\\%s\\"%directory # or '~/Downloads/' on linux
            obj = SmartDL(url, dest)
            obj.start()
            print(count)
        
        
            



print('finish')
