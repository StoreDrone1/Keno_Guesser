import numpy as np
import os.path
import time as t
import datetime as dt
from io import StringIO
import re
from statistics import mode
#this gets the modes of all mean results per day, adds them per day to each day file and also upkeeps a master list 
#of all known modes
def main():
    start = dt.datetime(2022, 2, 23)
    end = dt.datetime.now()
    delta = dt.timedelta(days=1)
    #curcalc = []
    proccalc = []
    m_mon = []
    m_tue = []
    m_wed = []
    m_thu = []
    m_fri = []
    m_sat = []
    m_sun = []
    
    while start != end:    
        if start.strftime('%a') == "Mon":
            if os.path.exists("MondayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                with open("MondayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as read:
                    proccalc = read.readlines()

                    for i in proccalc:
                        i = i[:-1]
                        #fix list to write formatted data correctly Fixed
                        i = [int(j) for j in i.split(",")]
                        i = mode(i)

                        if os.path.exists("MondayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("MondayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as mmode:
                                mmode.writelines(str(i))
                        else:
                            with open("MondayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as mmode:
                                mmode.writelines(str(i))
                        m_mon.append(i)
                                                  
        elif start.strftime('%a') == "Tue":
            if os.path.exists("TuesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                with open("TuesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as read:
                    proccalc = read.readlines()

                    for i in proccalc:
                        i = i[:-1]
                        i = [int(j) for j in i.split(",")]
                        i = mode(i)

                        if os.path.exists("TuesdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("TuesdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as tmode:
                                tmode.writelines(str(i))
                        else:
                            with open("TuesdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as tmode:
                                tmode.writelines(str(i))
                        m_tue.append(i)

        elif start.strftime('%a') == "Wed":
            if os.path.exists("WednesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                with open("WednesdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as read:
                    proccalc = read.readlines()

                    for i in proccalc:
                        i = i[:-1]
                        #fix list to write formatted data correctly
                        i = [int(j) for j in i.split(",")]
                        i = mode(i)

                        if os.path.exists("WednesdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("WednesdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as wmode:
                                wmode.writelines(str(i))
                        else:
                            with open("WednesdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as wmode:
                                wmode.writelines(str(i))
                        m_wed.append(i)

        elif start.strftime('%a') == "Thu":
            if os.path.exists("ThursdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                with open("ThursdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as read:
                    proccalc = read.readlines()

                    for i in proccalc:
                        i = i[:-1]
                        #fix list to write formatted data correctly
                        i = [int(j) for j in i.split(",")]
                        i = mode(i)

                        if os.path.exists("ThursdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("ThursdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as thmode:
                                thmode.writelines(str(i))
                        else:
                            with open("ThursdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as thmode:
                                thmode.writelines(str(i))
                        m_thu.append(i)

        elif start.strftime('%a') == "Fri":
            if os.path.exists("FridayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                with open("FridayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as read:
                    proccalc = read.readlines()

                    for i in proccalc:
                        i = i[:-1]
                        #fix list to write formatted data correctly
                        i = [int(j) for j in i.split(",")]
                        i = mode(i)

                        if os.path.exists("FridayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("FridayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as fmode:
                                fmode.writelines(str(i))
                        else:
                            with open("FridayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as fmode:
                                fmode.writelines(str(i))    
                        m_fri.append(i)

        elif start.strftime('%a') == "Sat":
            if os.path.exists("SaturdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                with open("SaturdayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as read:
                    proccalc = read.readlines()

                    for i in proccalc:
                        i = i[:-1]
                        #fix list to write formatted data correctly
                        i = [int(j) for j in i.split(",")]
                        i = mode(i)

                        if os.path.exists("SaturdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("SaturdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as samode:
                                samode.writelines(str(i))
                        else:
                            with open("SaturdayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as samode:
                                samode.writelines(str(i)) 
                        m_sat.append(i)

        elif start.strftime('%a') == "Sun":
            if os.path.exists("SundayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                with open("SundayMeans_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "r") as read:
                    proccalc = read.readlines()

                    for i in proccalc:
                        i = i[:-1]
                        #fix list to write formatted data correctly
                        i = [int(j) for j in i.split(",")]
                        i = mode(i)

                        if os.path.exists("SundayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt"):
                            with open("SundayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "a") as sumode:
                                sumode.writelines(str(i))
                        else:
                            with open("SundayModes_" + str(start.month) + "_" + str(start.day) + "_" + str(start.year) + ".txt", "w") as sumode:
                                sumode.writelines(str(i))
                        m_sun.append(i)                
        start += delta
        '''if start == end:   
            print("writing master files..")    
            with open("Mon_master.txt", "w") as mon:
                mon.writelines(str(m_mon))
            with open("Tue_master.txt", "w") as tue:
                tue.writelines(str(m_tue))
            with open("Wed_master.txt", "w") as wed:
                wed.writelines(str(m_wed))
            with open("Thur_master.txt", "w") as thu:
                thu.writelines(str(m_thu))
            with open("Fri_master.txt", "w") as fri:
                fri.writelines(str(m_fri))
            with open("Sat_master.txt", "w") as sat:
                sat.writelines(str(m_sat))
            with open("Sun_master.txt", "w") as sun:
                sun.writelines(str(m_sun))''' 
        return print("Finished")
sure = main()
print("Finished...")