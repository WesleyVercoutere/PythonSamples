import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

cts= pd.read_csv('CTS_26134.10_full.csv', sep = ';')

cts_s = cts[cts['SZ'] == 'TwistS_']
cts_z = cts[cts['SZ'] == 'TwistZ_']

cts_s_dict = {}
cts_z_dict = {}


#date_time_obj = dt.datetime.strptime(cts_s['DT'][1], '%Y-%m-%d-%H:%M:%S.%f')

cts_s_index = cts_s.index

print(cts_s_index['DT'][1])


#for i in cts_s.index:
#     pass 
#     print(cts_s['DT'][i], cts_s['avg f'][i]) 


#print(cts_s.head(3))
#print(cts_z.head(3))


#plt.plot(cts_s['avg f'])

#plt.show()
