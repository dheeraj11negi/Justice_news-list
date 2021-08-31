from scrapinghelp import htmlhelper
import json
import pandas as pd
import requests
from findData import findData
from multiprocessing.pool import ThreadPool as Pool

class Extract_Data:
    def crawlData():
        with open('readme.txt') as f:
            lines = f.readlines()

        x=lines[0]

        convertmonthdate = {
            'January': '01',
            'February': '02',
            'March': '03',
            'April': '04',
            'May': '05',
            'Jun': '06',
            'July': '07',
            'August': '08',
            'September': '09',
            'October': '10',
            'November': '11',
            'December': '12'
        }

        convert_date={
            "1":"01",
            "2":"02",
            "3":"03",
            "4":"04",
            "5":"05",
            '6':"06",
            "7":"07",
            "8":"08",
            "9":"09"
        }

        mylistlink=htmlhelper.collecturl(x,"'","',")

        my_set= set()
        for i in mylistlink:
            my_set.add(i)

        print(len(my_set))

        mycount=0
       
        pool_size = 100
        pool = Pool(pool_size)
        for check in  mylistlink:
            pool.apply_async(findData.findmydata,(mylistlink,check,convertmonthdate,convert_date,mycount))
            mycount+=1
        pool.close()
        pool.join()
         
        
