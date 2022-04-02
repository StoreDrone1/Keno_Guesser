#this file loads the keno numbers and appends an ongoing file.
from typing import final
import bs4 as bs
import requests
import datetime as dt
import numpy as np
from datetime import timedelta

def get_nums():
    #last known date (2021, 2, 22)
    #change date everytime you run to update the master files
    start = dt.datetime(2022, 3, 13)
    end = dt.datetime.now()
    delta = dt.timedelta(days=1)
    knums = []
    page_max = 0
    page = 0
    while start <= end:
        #next page
        page += 1
        #based on year range gives us the max pages of drawings for that day
        if start.year == 2009:
            page_max = 12
        elif start.year > 2009 & start.year <= 2019:
            page_max = 16
        else:
            page_max = 18    
        #create link to webpage and concat the date / page values
        link = 'https://www.ohiolottery.com/WinningNumbers/KenoDrawings/KenoDrawingsArchive?date=' + str(start.month) + '%2f' + str(start.day) + '%2f' + str(start.year) + '&page=' + str(page)
        #get response from lottery website
        r = requests.get(link)

        #soup to gather the text data
        soup = bs.BeautifulSoup(r.text, 'xml')

        #find tables we want
        table = soup.find('table', { 'class' : 'keno_drawings' })    
        
        try:
            #fill the list with all table data
            for row in table.findAll('tr')[1:]:
                nums = row.findAll('td')
                #crude, but removes everything we dont need from the list
                format_nums = str(nums).translate({ord(i): None for i in '[]</td>clasboerfu=",'})
                knums.append(format_nums)
                with open("keno_numbers_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", 'a') as lottery_file:
                    lottery_file.write(format_nums + '\n')
        except AttributeError as err:
            print("Error result - {0}".format(AttributeError))
            pass
        #only increment day once all pages have been recorded then reset page to 1
        if page == page_max:
           start += delta 
           page = 1
                
    return knums

print("getting keno numbers...")
k_results = get_nums()
print("finished getting numbers")