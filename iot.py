from urllib import request
from time import sleep 


while True: 
        sleep(3)
        x = 5
        form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdVi3lJe21n3cK5HzjzxSWPgF210QQed4ap-cjzl0j2laWsnA/formResponse?usp=pp_url&entry.449863054={}&submit=Submit".format(x)
        
        request.urlopen(form_url)
