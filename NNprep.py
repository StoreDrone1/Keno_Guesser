#use linear regression to find the best guesses for keno
#fimport imp
from cmath import sqrt
from copy import copy
from email import header
from posixpath import split
from re import sub
import pandas as pd
import glob as gl
import numpy as np
import matplotlib as plt
import time as t
from statistics import geometric_mean, stdev, variance, harmonic_mean, pvariance
from math import sqrt
#import Load_NN_Data as nndata


#use glob to package all the files relevant to the days / type of operation into a single list for 
#our dataframe
#means
mon_mean_files = gl.glob('MondayMeans*.txt')
mon_mean_files.sort()
tue_mean_files = gl.glob('TuesdayMeans*.txt')
tue_mean_files.sort()
wed_mean_files = gl.glob('WednesdayMeans*.txt')
wed_mean_files.sort()
thu_mean_files = gl.glob('ThursdayMeans*.txt')
thu_mean_files.sort()
fri_mean_files = gl.glob('FridayMeans*.txt')
fri_mean_files.sort()
sat_mean_files = gl.glob('SaturdayMeans*.txt')
sat_mean_files.sort()
sun_mean_files = gl.glob('SundayMeans*.txt')
sun_mean_files.sort()
#medians
mon_med_files = gl.glob('MondayMedians*.txt')
mon_med_files.sort()
tue_med_files = gl.glob('TuesdayMedians*.txt')
tue_med_files.sort()
wed_med_files = gl.glob('WednesdayMedians*.txt')
wed_med_files.sort()
thu_med_files = gl.glob('ThursdayMedians*.txt')
thu_med_files.sort()
fri_med_files = gl.glob('FridayMedians*.txt')
fri_med_files.sort()
sat_med_files = gl.glob('SaturdayMedians*.txt')
sat_med_files.sort()
sun_med_files = gl.glob('SundayMedians*.txt')
sun_med_files.sort()
'''#differences
mon_dif_files = gl.glob('Mondaydif*.txt')
mon_dif_files.sort()
tue_dif_files = gl.glob('Tuesdaydif*.txt')
tue_dif_files.sort()
wed_dif_files = gl.glob('Wednesdaydif*.txt')
wed_dif_files.sort()
thu_dif_files = gl.glob('Thursdaydif*.txt')
thu_dif_files.sort()
fri_dif_files = gl.glob('Fridaydif*.txt')
fri_dif_files.sort()
sat_dif_files = gl.glob('Saturdaydif*.txt')
sat_dif_files.sort()
sun_dif_files = gl.glob('Sundaydif*.txt')
sun_dif_files.sort()'''
print("read data means..")
#populate the dataframe
#mean
mdatamean = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in mon_mean_files), axis=1)
mon = np.array(mdatamean, dtype=int)
tdatamean = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in tue_mean_files), axis=1)
tue = np.array(tdatamean, dtype=int)
wdatamean = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in wed_mean_files), axis=1)
wed = np.array(wdatamean, dtype=int)
thdatamean = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in thu_mean_files), axis=1)
thu = np.array(thdatamean, dtype=int)
fdatamean = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in fri_mean_files), axis=1)
fri = np.array(fdatamean, dtype=int)    
sadatamean = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in sat_mean_files), axis=1)
sat = np.array(sadatamean, dtype=int)
sudatamean = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in sun_mean_files), axis=1)
sun = np.array(sudatamean, dtype=int)
print("Loaded mean data")
#medians
mdatamed = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in mon_med_files), axis=1)
monmed = np.array(mdatamed, dtype=int)
tdatamed = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in tue_med_files), axis=1)
tuemed = np.array(tdatamed, dtype=int)
wdatamed = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in wed_med_files), axis=1)
wedmed = np.array(wdatamed, dtype=int)
thdatamed = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in thu_med_files), axis=1)
thumed = np.array(thdatamed, dtype=int)
fdatamed = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in fri_med_files), axis=1)
frimed = np.array(fdatamed, dtype=int)    
sadatamed = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in sat_med_files), axis=1)
satmed = np.array(sadatamed, dtype=int)
sudatamed = pd.concat((pd.read_csv(file, delimiter=',', header=None) for file in sun_med_files), axis=1)
sunmed = np.array(sudatamed, dtype=int)
print("Loaded median data")
print("Calculating...")

#5 best average spread to use
mon38 = 0
mon39 = 0
mon40 = 0
mon41 = 0
mon42 = 0
#store the frequency of each average
m38list = []
m39list = []
m40list = []
m41list = []
m42list = []
#keep track of the standard deviation 
m38deviation = 0
m39deviation = 0
m40deviation = 0
m41deviation = 0
m42deviation = 0
#tue
tue38 = 0
tue39 = 0
tue40 = 0
tue41 = 0
tue42 = 0

t38list = []
t39list = []
t40list = []
t41list = []
t42list = []
 
t38deviation = 0
t39deviation = 0
t40deviation = 0
t41deviation = 0
t42deviation = 0

#wed

wed38 = 0
wed39 = 0
wed40 = 0
wed41 = 0
wed42 = 0

w38list = []
w39list = []
w40list = []
w41list = []
w42list = []
 
w38deviation = 0
w39deviation = 0
w40deviation = 0
w41deviation = 0
w42deviation = 0
#thur

thu38 = 0
thu39 = 0
thu40 = 0
thu41 = 0
thu42 = 0

th38list = []
th39list = []
th40list = []
th41list = []
th42list = []
 
th38deviation = 0
th39deviation = 0
th40deviation = 0
th41deviation = 0
th42deviation = 0
#friday
fri38 = 0
fri39 = 0
fri40 = 0
fri41 = 0
fri42 = 0

f38list = []
f39list = []
f40list = []
f41list = []
f42list = []

f38deviation = 0
f39deviation = 0
f40deviation = 0
f41deviation = 0
f42deviation = 0
#sat
sat38 = 0
sat39 = 0
sat40 = 0
sat41 = 0
sat42 = 0

s38list = []
s39list = []
s40list = []
s41list = []
s42list = []
 
s38deviation = 0
s39deviation = 0
s40deviation = 0
s41deviation = 0
s42deviation = 0

#sun
sun38 = 0
sun39 = 0
sun40 = 0
sun41 = 0
sun42 = 0

su38list = []
su39list = []
su40list = []
su41list = []
su42list = []

su38deviation = 0
su39deviation = 0
su40deviation = 0
su41deviation = 0
su42deviation = 0

ahigh = 0
alow = 0

mmed = []
tmed = []
wmed = []
thmed = []
fmed = []
samed = []
sumed = []

#helper function to calc stdev
def varmon(data, ddof):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

print("process day specific data...")
for i in range(0, mon.size-1):
    if mon[0, i] == 38:
        mon38 += 1
    elif mon[0, i] == 39:
        mon39 += 1
    elif mon[0, i] == 40:
        mon40 += 1
    elif mon[0, i] == 41:
        mon41 += 1
    elif mon[0, i] == 42:
        mon42 += 1
    elif mon[0, i] <= 43:
        ahigh += 1
    elif mon[0, i] >= 37:
        alow += 1
for i in range(0, tue.size-1):
    if tue[0, i] == 38:
        tue38 += 1
    elif tue[0, i] == 39:
        tue39 += 1
    elif tue[0, i] == 40:
        tue40 += 1
    elif tue[0, i] == 41:
        tue41 += 1
    elif tue[0, i] == 42:
        tue42 += 1
    elif tue[0, i] <= 43:
        ahigh += 1
    elif tue[0, i] >= 37:
        alow += 1
for i in range(0, wed.size-1):
    if wed[0, i] == 38:
        wed38 += 1
    elif wed[0, i] == 39:
        wed39 += 1
    elif wed[0, i] == 40:
        wed40 += 1
    elif wed[0, i] == 41:
        wed41 += 1
    elif wed[0, i] == 42:
        wed42 += 1
    elif wed[0, i] <= 43:
        ahigh += 1
    elif wed[0, i] >= 37:
        alow += 1
#thursday
for i in range(0, thu.size-1):
    if thu[0, i] == 38:
        thu38 += 1
    elif thu[0, i] == 39:
        thu39 += 1
    elif thu[0, i] == 40:
        thu40 += 1
    elif thu[0, i] == 41:
        thu41 += 1
    elif thu[0, i] == 42:
        thu42 += 1
    elif thu[0, i] <= 43:
        ahigh += 1
    elif thu[0, i] >= 37:
        alow += 1
#fri
for i in range(0, fri.size-1):
    if fri[0, i] == 38:
        fri38 += 1
    elif fri[0, i] == 39:
        fri39 += 1
    elif fri[0, i] == 40:
        fri40 += 1
    elif fri[0, i] == 41:
        fri41 += 1
    elif fri[0, i] == 42:
        fri42 += 1
    elif fri[0, i] <= 43:
        ahigh += 1
    elif fri[0, i] >= 37:
        alow += 1
for i in range(0, sat.size-1):
    if sat[0, i] == 38:
        sat38 += 1
    elif sat[0, i] == 39:
        sat39 += 1
    elif sat[0, i] == 40:
        sat40 += 1
    elif sat[0, i] == 41:
        sat41 += 1
    elif sat[0, i] == 42:
        sat42 += 1
    elif sat[0, i] >= 37:
        alow += 1
    elif sat[0, i] <= 43:
        ahigh += 1
#sun
for i in range(0, sun.size-1):
    if sun[0, i] == 38:
        sun38 += 1
    elif sun[0, i] == 39:
        sun39 += 1
    elif sun[0, i] == 40:
        sun40 += 1
    elif sun[0, i] == 41:
        sun41 += 1
    elif sun[0, i] == 42:
        sun42 += 1
    elif sun[0, i] >= 37:
        alow += 1
    elif sun[0, i] <= 43:
        ahigh += 1
        
#mon meds
for i in range(0, monmed.size-1):
    mmed.append(i)
for i in range(0, tuemed.size-1):
    tmed.append(i)
for i in range(0, wedmed.size-1):
    wmed.append(i)
for i in range(0, thumed.size-1):
    thmed.append(i)
for i in range(0, frimed.size-1):
    fmed.append(i)
for i in range(0, satmed.size-1):
    samed.append(i)
for i in range(0, sunmed.size-1):
    sumed.append(i)
#m38
hm38 = [mon38, tue38, wed38, thu38, fri38, sat38, sun38]
m = harmonic_mean(hm38)
var = varmon(hm38, m)
print("m38 m = {}".format(m))
print("variance of m38 = {}".format(int(var * -1)))
dev38 = stdev(hm38, m)
#m39
hm39 = [mon39, tue39, wed39, thu39, fri39, sat39, sun39]
m = harmonic_mean(hm39)
var = varmon(hm39, m)
print("m39 m = {}".format(m))
print("variance of m39 = {}".format(int(var * -1)))
dev39 = stdev(hm39, m)
#40
hm40 = [mon40, tue40, wed40, thu40, fri40, sat40, sun40]
m = harmonic_mean(hm40)
var = varmon(hm40, m)
print("m40 m = {}".format(m))
print("variance of m40 = {}".format(int(var * -1)))
dev40 = stdev(hm40, m)
#41
hm41 = [mon41, tue41, wed41, thu41, fri41, sat41, sun41]
m = harmonic_mean(hm41)
var = varmon(hm41, m)
print("m41 m = {}".format(m))
print("variance of m41 = {}".format(int(var * -1)))
dev41 = stdev(hm41, m)
#42
hm42 = [mon42, tue42, wed42, thu42, fri42, sat42, sun42]
m = harmonic_mean(hm42)
var = varmon(hm42, m)
print("m42 m = {}".format(m))
print("variance of m42 = {}".format(int(var * -1)))
dev42 = stdev(hm42, m)

t.sleep(4)
print("Deviations...")
print("m 38 deviation = {}".format(int(dev38)))
print("m 39 deviation = {}".format(int(dev39)))
print("m 40 deviation = {}".format(int(dev40)))
print("m 41 deviation = {}".format(int(dev41)))
print("m 42 deviation = {}".format(int(dev42)))
print("Percentages...")

print("-----Percentage of 38s'-----")
print("percentage of m = {}%".format((mon38 / mon.size) * 100))
print("percentage of t = {}%".format((tue38 / tue.size) * 100))
print("percentage of w = {}%".format((wed38 / wed.size) * 100))
print("percentage of th = {}%".format((thu38 / thu.size) * 100))
print("percentage of f = {}%".format((fri38 / fri.size) * 100))
print("percentage of sat = {}%".format((sat38 / sat.size) * 100))
print("percentage of sun = {}%".format((sun38 / sun.size) * 100))
print("-----Percentage of 39s'-----")
print("percentage of m = {}%".format((mon39 / mon.size) * 100))
print("percentage of t = {}%".format((tue39 / tue.size) * 100))
print("percentage of w = {}%".format((wed39 / wed.size) * 100))
print("percentage of th = {}%".format((thu39 / thu.size) * 100))
print("percentage of f = {}%".format((fri39 / fri.size) * 100))
print("percentage of sat = {}%".format((sat39 / sat.size) * 100))
print("percentage of sun = {}%".format((sun39 / sun.size) * 100))
print("-----Percentage of 40s'-----")
print("percentage of m = {}%".format((mon40 / mon.size) * 100))
print("percentage of t = {}%".format((tue40 / tue.size) * 100))
print("percentage of w = {}%".format((wed40 / wed.size) * 100))
print("percentage of th = {}%".format((thu40 / thu.size) * 100))
print("percentage of s f = {}%".format((fri40 / fri.size) * 100))
print("percentage of s sat = {}%".format((sat40 / sat.size) * 100))
print("percentage of s sun = {}%".format((sun40 / sun.size) * 100))
print("-----Percentage of 41s'-----")
print("percentage of m = {}%".format((mon41 / mon.size) * 100))
print("percentage of t = {}%".format((tue41 / tue.size) * 100))
print("percentage of w = {}%".format((wed41 / wed.size) * 100))
print("percentage of th = {}%".format((thu41 / thu.size) * 100))
print("percentage of f = {}%".format((fri41 / fri.size) * 100))
print("percentage of sat = {}%".format((sat41 / sat.size) * 100))
print("percentage of sun = {}%".format((sun41 / sun.size) * 100))
print("-----Percentage of 42s'-----")
print("percentage of m = {}%".format((mon42 / mon.size) * 100))
print("percentage of t = {}%".format((tue42 / tue.size) * 100))
print("percentage of w = {}%".format((wed42 / wed.size) * 100))
print("percentage of th = {}%".format((thu42 / thu.size) * 100))
print("percentage of f = {}%".format((fri42 / fri.size) * 100))
print("percentage of sat = {}%".format((sat42 / sat.size) * 100))
print("percentage of sun = {}%".format((sun42 / sun.size) * 100))

print("Total of lower than 37's = {}".format(int(alow)))
print("Total of higher than 43's = {}".format(int(ahigh)))

print("Finished")
'''
print("dataframe modes")
datamode = pd.concat((pd.read_csv(file) for file in mon_mode_files), ignore_index=True)
datamode = pd.concat((pd.read_csv(file) for file in tue_mode_files), ignore_index=True)
datamode = pd.concat((pd.read_csv(file) for file in wed_mode_files), ignore_index=True)
datamode = pd.concat((pd.read_csv(file) for file in thu_mode_files), ignore_index=True)
datamode = pd.concat((pd.read_csv(file) for file in fri_mode_files), ignore_index=True)
datamode = pd.concat((pd.read_csv(file) for file in sat_mode_files), ignore_index=True)
datamode = pd.concat((pd.read_csv(file) for file in sun_mode_files), ignore_index=True) 
print("dataframe medians")
datamed = pd.concat((pd.read_csv(file) for file in mon_med_files), ignore_index=True)
datamed = pd.concat((pd.read_csv(file) for file in tue_med_files), ignore_index=True)
datamed = pd.concat((pd.read_csv(file) for file in wed_med_files), ignore_index=True)
datamed = pd.concat((pd.read_csv(file) for file in thu_med_files), ignore_index=True)
datamed = pd.concat((pd.read_csv(file) for file in fri_med_files), ignore_index=True)
datamed = pd.concat((pd.read_csv(file) for file in sat_med_files), ignore_index=True)
datamed = pd.concat((pd.read_csv(file) for file in sun_med_files), ignore_index=True)
print("diffs")
datadif = pd.concat((pd.read_csv(file) for file in mon_dif_files), ignore_index=True)
datadif = pd.concat((pd.read_csv(file) for file in tue_dif_files), ignore_index=True)
datadif = pd.concat((pd.read_csv(file) for file in wed_dif_files), ignore_index=True)
datadif = pd.concat((pd.read_csv(file) for file in thu_dif_files), ignore_index=True)
datadif = pd.concat((pd.read_csv(file) for file in fri_dif_files), ignore_index=True)
datadif = pd.concat((pd.read_csv(file) for file in sat_dif_files), ignore_index=True)
datadif = pd.concat((pd.read_csv(file) for file in sun_dif_files), ignore_index=True)
print("head of diff")'''




