import csv
import numpy as np
import matplotlib.pyplot as plt
"""
This script first use the csv library to run through the weather data extracted by sql queries and
calculate the moving averages then visualize the data through matplotlib Library
"""


#   global_data
year_global = []
temp_global = []
#   moving_average temperature only
mov_avg_temp_global = []
#   year, moving_average temperature
mov_avg_data_global = []

#   open csv and extract data
def extract_csv(filepath='',year=[],temp=[]):
    #   open global weather data
    f = open(filepath)
    #   Extract data from csv to arrays
    for line in f.readlines():
        if(line.split(',')[0] != 'year'):
            temp1 = line.split(',')[1]
            temp1 = temp1.replace('\n','')
            year1 = line.split(',')[0]
            year1 = year1.replace("\'","")
            temp.append(temp1)
            year.append(year1)
    print("extract csv success")
extract_csv('global_data_1841-2013.csv',year_global,temp_global)

#   calculate moving averages
def moving_average(year=[],temp=[],mov_avg_data=[],mov_avg_temp=[]):
    i = 0
    avg_temp = 0
    last_num = len(year) - 9
    while i < last_num:
        avg_temp = (float(temp[i]) + float(temp[i+1]) + float(temp[i+2]) + float(temp[i+3])
        + float(temp[i+4]) + float(temp[i+5]) + float(temp[i+6]) + float(temp[i+7]) + float(temp[i+8]) + float(temp[i+9]))/9
        avg_temp = round(avg_temp, 2)
        mov_avg_temp.append(avg_temp)
        mov_avg_data.append('\"'+year[i+9]+'\"'+','+'\"'+str(avg_temp)+'\"'+','+'\n')
        i += 1
    print("calculate moving average success")
moving_average(year_global,temp_global,mov_avg_data_global,mov_avg_temp_global)

#   save the moving average to csv
def save_csv(filepath, mov_avg_data=[]):
    f = open(filepath, 'w')
    f.writelines(mov_avg_data)
    f.close()
    print("save csv success")
save_csv('moving_avg_global.csv',mov_avg_data_global)

#   city_data_Taipei
year_tpe = []
temp_tpe = []
mov_avg_temp_tpe = []
mov_avg_data_tpe =[]

extract_csv('city_data_taipei.csv',year_tpe,temp_tpe)
moving_average(year_tpe,temp_tpe,mov_avg_data_tpe,mov_avg_temp_tpe)
save_csv('moving_avg_taipei.csv',mov_avg_data_tpe)




#   plot line chart
year_int_global = []
temp_float_global = []
def string_to_int_and_float(year=[], mov_avg_temp=[],year_out=[],temp_out=[]):
    for item in year:
        if int(item) >= 1850:
            year_out.append(int(item))
    for item in mov_avg_temp:
        temp_out.append(float(item))
    print('string to int and float success')
string_to_int_and_float(year_global,mov_avg_temp_global, year_int_global, temp_float_global)

year_int_tpe = []
temp_float_tpe = []
string_to_int_and_float(year_tpe,mov_avg_temp_tpe, year_int_tpe, temp_float_tpe)
"""
plt.xticks(np.arange(min(year_int_global)-1,max(year_int_global)+7,20.0))
plt.yticks(np.arange(min(temp_float_global),max(temp_float_global)+1,0.5))
"""
fig, ax = plt.subplots()
line_global = ax.plot(year_int_global,temp_float_global)
line_tpe = ax.plot(year_int_tpe,temp_float_tpe)
"""
line_txg = ax.plot(year_int_txg,temp_float_txg)
line_khh = ax.plot(year_int_khh,temp_float_khh)
"""
"""
plt.plot(year_int_global,temp_float_global)
"""
plt.ylabel('temperature')
plt.xlabel('year')
plt.title('Global and Local Temperature Trend 1850-2013')
plt.show()
