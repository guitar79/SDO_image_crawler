# Print software information
# print('Source : https://github.com/seungwonpark/SunSpotTracker')
# Based on python 2.7.12 by Seungwon Park
# change to python 3.6 by guitar79@gs.hs.kr

# get data from https://sdo.gsfc.nasa.gov/assets/img/browse/
# file name structure : 20170228_231038_1024_MHII.jpg
# conda install beautifulsoup

import os
from datetime import datetime
import SDO_utility

# some variables for downloading (site, file, perid and time gap, etc.)
site = 'https://sdo.gsfc.nasa.gov/assets/img/browse/'
   
add_log = True
if add_log == True :
    log_file = './log/SDO_image_list_to_filelist.log'
    err_log_file = './log/SDO_image_list_to_filelist.log'
    
from dateutil.relativedelta import relativedelta
p_start_date = datetime(2012, 1, 1) #convert startdate to date type
p_end_date = datetime(2019, 12, 31)

date_No = 0
date1 = p_start_date
date2 = p_start_date
dates = []
while date2 < p_end_date : 
    date_No += 1
    date2 = date1 + relativedelta(days=1)
    date1_strf = date1.strftime('%Y%m%d')
    date = (date1_strf, date_No)
    dates.append(date)
    date1 = date2

save_dir_name = '../SDO_filelists/'
if not os.path.exists('{0}'.format(save_dir_name)):
    os.makedirs('{0}'.format(save_dir_name))
    print ('*'*80)
    print ('{0} is created'.format(save_dir_name))
else :
    print ('*'*80)
    print ('{0} is exist'.format(save_dir_name))
        
for date in dates:
    SDO_utility.SDO_image_list_to_filelist_1day(save_dir_name, date)
    