#this file loads the keno numbers and appends an ongoing file.
import bs4 as bs
import requests
import datetime as dt
import numpy as np
from datetime import timedelta
#create file to store keno numbers
#f_name = 'keno_nums'
#file = f_name+'.txt'

#file = open("keno_nums.xml", mode='r+a', encoding='utf-8')
def get_nums():
    start = dt.datetime(2009, 7, 1)
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
        link = 'https://www.ohiolottery.com/WinningNumbers/KenoDrawings/KenoDrawingsArchive?date=' + str(start.month) + '%2f' + str(start.day) + '%2f' + str(start.year) + '&page=' + str(page)#+ '&aliaspath=%2fWinningNumbers%2fKenoDrawings%2fKenoDrawingsArchive'
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
                #print(format_nums)
                #hopefully the text file doesn't explode ;/
                with open("keno_numbers.txt", 'a') as file:
                    file.writelines(format_nums)
                    file.close()
        except AttributeError:
            print("continuing")
            pass
        #only increment day once all pages have been recorded then reset page to 1
        if page == page_max:
           start += delta 
           page = 1
                
    return knums

n = np.array(get_nums())
print(n.size)
