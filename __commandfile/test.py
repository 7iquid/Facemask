from datetime import datetime

from calendar import monthrange



val = 94.8188898563385

dt_object2 = datetime.fromtimestamp(val)

# ddate = str(datetime.now().date())
# ddate =	datetime('12/1/1')
# print(dt_object2 )




def allDays(y, m):
    return ['{:04d}-{:02d}-{:02d}'.format(y, m, d) for d in range(1, monthrange(y, m)[1] + 1)]	

# print(allDays(2022,1))  
print(itermonthdates(2021,12))  