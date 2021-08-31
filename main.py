

from scrapinghelp import htmlhelper
import json
import pandas as pd
import requests
from Extract_Data import Extract_Data
from multiprocessing.pool import ThreadPool as Pool


if __name__ == "__main__":
      '''mylistlink=[]
      count=0
      url="https://www.justice.gov/news"
      while count<=777:

             
            with open('checkurl.txt', 'a') as f:
                  f.write(str(url))
            try:
                  res=requests.get(url)
                  print(res)

                  url="https://www.justice.gov/news"
                  

                  source=htmlhelper.returnformatedhtml(res.text)
                  geturl=htmlhelper.collecturl(source,'<div class=\"views-field views-field-title\">',"</div")

                  for ele in geturl:

                        addlink=htmlhelper.returnvalue(ele,"<a href=\"","\">")
                        if addlink!="":
                              mylistlink.append("https://www.justice.gov"+addlink)
                  count+=1
                  url=url+"?page="+str(count)
            except:
                  pass

      pro=set()
      for z in mylistlink:
            pro.add(z)
      print(len(mylistlink))

      print(len(pro))



            #https://www.justice.gov/news?page=3
      try:
            with open('readme.txt', 'x') as f:
                  f.write(str(mylistlink))
      except:
            print("file already exist")
            pass'''

      Extract_Data.crawlData()




      




















