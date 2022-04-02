from io import StringIO
from os import close
import numpy as np
from numpy.core import numeric
import pandas as pd
import datetime as dt
import time as t
import os.path
from requests.api import get
#globals
isMon = False
isTue = False
isWed = False
isThu = False
isFri = False
isSat = False
isSun = False
isAM = False
isPM = False
#daily lists
mean_l_mon = 0
mean_l_tue = 0
mean_l_wed = 0
mean_l_thu = 0
mean_l_fri = 0
mean_l_sat = 0
mean_l_sun = 0

med_l_mon = 0
med_l_tue = 0
med_l_wed = 0
med_l_thu = 0
med_l_fri = 0
med_l_sat = 0
med_l_sun = 0

dif_l_mon = 0
dif_l_tue = 0
dif_l_wed = 0
dif_l_thu = 0
dif_l_fri = 0
dif_l_sat = 0
dif_l_sun = 0

#calc lists
final_list_mean = []
final_list_median = []
temp_list_mean = []
temp_list_median = []
#this will be for the end of the day on a PER DAY basis as no numbers are duplicate in a single drawing
final_list_mode = []

def main():
    start = dt.datetime(2022, 3, 13)
    end = dt.datetime.now()
    delta = dt.timedelta(days=1)
    page = 0 
    page_max = 0
    count = 0

    #cur proc list 
    cur_calc = []

    while start != end:
        if os.path.exists("formatted_numbers_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
            print("File exists, opening...")
            with open("formatted_numbers_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as file:
                #read file 
                cur_calc = file.readlines() 
                #no newline chars
                cur_calc = list(filter(("\n").__ne__, cur_calc))
                #iterate through each drawing and remove the space at the end and beginning
                for i in cur_calc:
                    count = 0
                    run_total = 0
                    i = i[:-2]
                    i = i[1:]
                    #convert list to int, process calculation list
                    i = [int(j) for j in i.split(",")]

                    #temp calculation list for means/meds of the day.
                    get_mean = get_mean_for_day(i)
                    get_med = get_median_for_day(i)
                    get_dif = get_f_last(i)             
                    
                    #write to respective day file
                    if start.strftime('%a') == "Mon":
                        mean_l_mon = get_mean
                        med_l_mon = get_med
                        dif_l_mon = get_dif
                        if os.path.exists("MondayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("MondayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as mean:
                                mean.writelines(str(mean_l_mon) + ",") 
                        else:
                            with open("MondayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as mean:
                                mean.writelines(str(mean_l_mon) + ",")
                        if os.path.exists("MondayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("MondayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as med:
                                med.writelines(str(med_l_mon) + ",")
                        else:
                            with open("MondayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as med:
                                med.writelines(str(med_l_mon) + ",")
                        if os.path.exists("Mondaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):    
                            with open("Mondaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as diff:
                                diff.writelines(str(dif_l_mon) + ",")
                        else:
                            with open("Mondaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as diff:
                                diff.writelines(str(dif_l_mon) + ",")
                    elif start.strftime('%a') == "Tue":
                        mean_l_tue = get_mean
                        med_l_tue = get_med
                        dif_l_tue = get_dif
                        if os.path.exists("TuesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("TuesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as mean:
                                mean.writelines(str(mean_l_tue) + ",") 
                        else:
                            with open("TuesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as mean:
                                mean.writelines(str(mean_l_tue) + ",")
                        if os.path.exists("TuesdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("TuesdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as med:
                                med.writelines(str(med_l_tue) + ",")
                        else:
                            with open("TuesdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as med:
                                med.writelines(str(med_l_tue) + ",")
                        if os.path.exists("Tuesdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):    
                            with open("Tuesdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as diff:
                                diff.writelines(str(dif_l_tue) + ",")
                        else:
                            with open("Tuesdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as diff:
                                diff.writelines(str(dif_l_tue) + ",")
                    elif start.strftime('%a') == "Wed":
                        mean_l_wed = get_mean
                        med_l_wed = get_med
                        dif_l_wed = get_dif
                        if os.path.exists("WednesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("WednesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as mean:
                                mean.writelines(str(mean_l_wed) + ",") 
                        else:
                            with open("WednesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as mean:
                                mean.writelines(str(mean_l_wed) + ",")
                        if os.path.exists("WednesdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("WednesdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as med:
                                med.writelines(str(med_l_wed) + ",")
                        else:
                            with open("WednesdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as med:
                                med.writelines(str(med_l_wed) + ",")
                        if os.path.exists("Wednesdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):    
                            with open("Wednesdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as diff:
                                diff.writelines(str(dif_l_wed) + ",")
                        else:
                            with open("Wednesdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as diff:
                                diff.writelines(str(dif_l_wed) + ",")
                    elif start.strftime('%a') == "Thu":
                        mean_l_thu = get_mean
                        med_l_thu = get_med
                        dif_l_thu = get_dif
                        if os.path.exists("ThursdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("ThursdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as mean:
                                mean.writelines(str(mean_l_thu) + ",") 
                        else:
                            with open("ThursdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as mean:
                                mean.writelines(str(mean_l_thu) + ",")
                        if os.path.exists("ThursdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("ThursdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as med:
                                med.writelines(str(med_l_thu) + ",")
                        else:
                            with open("ThursdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as med:
                                med.writelines(str(med_l_thu) + ",")
                        if os.path.exists("Thursdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):    
                            with open("Thursdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as diff:
                                diff.writelines(str(dif_l_thu) + ",")
                        else:
                            with open("Thursdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as diff:
                                diff.writelines(str(dif_l_thu) + ",")
                    elif start.strftime('%a') == "Fri":
                        mean_l_fri = get_mean
                        med_l_fri = get_med
                        dif_l_fri = get_dif
                        if os.path.exists("FridayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("FridayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as mean:
                                mean.writelines(str(mean_l_fri) + ",") 
                        else:
                            with open("FridayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as mean:
                                mean.writelines(str(mean_l_fri) + ",")
                        if os.path.exists("FridayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("FridayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as med:
                                med.writelines(str(med_l_fri) + ",")
                        else:
                            with open("FridayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as med:
                                med.writelines(str(med_l_fri) + ",")
                        if os.path.exists("Fridaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):    
                            with open("Fridaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as diff:
                                diff.writelines(str(dif_l_fri) + ",")
                        else:
                            with open("Fridaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as diff:
                                diff.writelines(str(dif_l_fri) + ",")
                    elif start.strftime('%a') == "Sat":
                        mean_l_sat = get_mean
                        med_l_sat = get_med
                        dif_l_sat = get_dif
                        if os.path.exists("SaturdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("SaturdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as mean:
                                mean.writelines(str(mean_l_sat) + ",") 
                        else:
                            with open("SaturdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as mean:
                                mean.writelines(str(mean_l_sat) + ",")
                        if os.path.exists("SaturdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("SaturdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as med:
                                med.writelines(str(med_l_sat) + ",")
                        else:
                            with open("SaturdayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as med:
                                med.writelines(str(med_l_sat) + ",")
                        if os.path.exists("Saturdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):    
                            with open("Saturdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as diff:
                                diff.writelines(str(dif_l_sat) + ",")
                        else:
                            with open("Saturdaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as diff:
                                diff.writelines(str(dif_l_sat) + ",")
                    elif start.strftime('%a') == "Sun":
                        mean_l_sun = get_mean
                        med_l_sun = get_med
                        dif_l_sun = get_dif
                        if os.path.exists("SundayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("SundayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as mean:
                                mean.writelines(str(mean_l_sun) + ",") 
                        else:
                            with open("SundayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as mean:
                                mean.writelines(str(mean_l_sun) + ",")
                        if os.path.exists("SundayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("SundayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as med:
                                med.writelines(str(med_l_sun) + ",")
                        else:
                            with open("SundayMedians_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as med:
                                med.writelines(str(med_l_sun) + ",")
                        if os.path.exists("Sundaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):    
                            with open("Sundaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as diff:
                                diff.writelines(str(dif_l_sun) + ",")
                        else:
                            with open("Sundaydif_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as diff:
                                diff.writelines(str(dif_l_sun) + ",")    
            start += delta
        else:
            print("File doesn't exist")
            start += delta
            break    
    return "Finished"
           
#simple math...mean median mode...etc
def get_mean_for_day(size):
    list_mean = size
    r_avg = 0
    count = 0
    for i in range(0, len(list_mean)):
        r_avg = round(r_avg, None) + list_mean[i]
        count += 1
        #every 20 numbers is a complete draw
        if count % 20 == 0 and i != 0:
            r_avg /= 20           
    return int(r_avg)

def get_mode_for_day(size):
    return

def get_median_for_day(size):
    med_size = size
    result = med_size[9] + med_size[10]
    med_avg = round(result / 2, None)
    return med_avg

def get_f_last(size):
    list_diff = size
    dif = list_diff[19] - list_diff[0]
    return dif

test = main()
print(test)