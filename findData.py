import re
from csv import writer
import requests
import json
from multiprocessing import Pool
from datetime import datetime
import hashlib
import time
from urllib.request import urlopen
from scrapinghelp import htmlhelper
last_updated_string = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

global myjson_list
myjson_list=[]
class findData:
    def findmydata(mylistlink,check,convertmonthdate,convert_date,mycount):
        res=requests.get(check)
        print(res)
        while(res.status_code!=200):
            time.sleep(1200)
            res=requests.get(check)
            print(res)

        source=htmlhelper.returnformatedhtml(res.text)
        d={

                "Title": "",
                "Source": "https://www.justice.gov/news",
                "publishedAt": "",
                "URL": "",
                "query": "",
                "uid": "",
                "Content": ""
        }

        try:
            findtitle = htmlhelper.returnvalue(source,"<meta property=\"og:title\" content=\"","\"/>")
            if findtitle!="":
                d["Title"]=findtitle

        except:
            pass


        try:
            getdate=htmlhelper.returnvalue(source,"class=\"date-display-single\"","</div>")
            getnewdate=htmlhelper.returnvalue(getdate,"\">","</span>")
            mydate=getnewdate.replace(",","").split(' ')
            length=len(mydate)
            get_year=mydate[length-1]
            get_date=mydate[length-2]
            if get_date in convert_date and  len(get_date)<=1:
                get_org_date=convert_date[get_date]
            else:
                get_org_date=get_date

            get_month=mydate[length-3]
            if get_month in convertmonthdate:
                get_new_month=convertmonthdate[get_month]

            original_date=get_year+"-"+get_new_month+"-"+get_org_date
            if original_date!="":
                d["publishedAt"]=original_date


        except:
            pass

        try:
            d["URL"]=check
        except:
            pass
        try:

            get_content=htmlhelper.returnvalue(source,"<div class=\"field field--name-field-pr-body field--type-text-long field--label-hidden\">","</div>")


            getarr=htmlhelper.collecturl(get_content,"<p","</p>")
            mystring=""

            for tag in  getarr:
                cleanr=re.compile('<.*?>')
                cleantext=re.sub(cleanr,'',tag)
                mystring=mystring+cleantext+" "

            if  mystring!="" :

                mystring=mystring.replace('align=\"justify\">',"").replace('align=\"center\">',"").replace('align=\"right\">','')
                mystring=mystring.replace('align=\"justify\"','').replace('class=\"head\">','').replace('align=\"left\"','').replace('>','').replace('<','')
                d["Content"]=mystring
        except:
            pass

        try:
            d["uid"] = hashlib.sha256(((d["Source"] + d["Title"]).lower()).encode()).hexdigest()
        except:
            pass

        try:
            myjson_list.append(d)
            print(mycount)

        except:
            pass

        try:
            if mycount >= 19448:

                with open('justice_news_list.json', 'w', encoding="utf-8") as file:
                    json.dump(myjson_list, file, ensure_ascii=False, indent=4)

        except:
            pass














      