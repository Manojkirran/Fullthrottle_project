import os
from faker import Faker
from random import randrange, randint

f = Faker()

os.environ['DJANGO_SETTINGS_MODULE'] = 'Fullthrottleproject.settings'
import django
django.setup()

from webapp.models import *
#from django.contrib.auth.models import members

tzs = (
            ('America/Los_Angelesr'),
            ('India/Bangalore '),
            ('India/Chennai'),
            ('China/Beijing'),
            ('newzealand/Wellington'),
            ('America/Washington D C')
)

#################################################
## create the user and profile for every user
#################################################
def populate_profile(start, end):
    for i in range(start, end+1):
        name = f.name()
        stringint = str(i)
        uid = "WO" + str(stringint[0:2]) + name[0:2].upper() + str(stringint[2:])
        timeval =f.time()
        timeval2 = timeval[0:2] + timeval[2:]
        if int(timeval[0:2]) >= 15:
           if int(timeval[0:2]) == 23:
              timeval2 = str((int(timeval[0:2]) + 0)) + timeval[2:]
           else:
              timeval2 = str((int(timeval[0:2]) + 1)) + timeval[2:]
        else:
           timeval2 = str((int(timeval[0:2]) + 8)) + timeval[2:]           
        dateval = f.date_between(start_date='-1y', end_date='now')
        dateval2 = f.date_between(start_date='-1y', end_date='now')
        dateval3 = f.date_between(start_date='-1y', end_date='now')
        dateval5 = f.date_between(start_date='-1y', end_date='now')
        tz = tzs[randint(0,5)]
        starttime = str(dateval) + " " + str(timeval) 
        endtime = str(dateval) + " " + str(timeval2) 
        starttime1 = str(dateval3) + " " + str(timeval)
        endtime1 =  str(dateval3) + " " + str(timeval2)
        starttime2 = str(dateval5) + " " + str(timeval)
        endtime2  = str(dateval5) + " " + str(timeval2)
        starttimefinal2 = [{"Start_time:": starttime, "End_time:": endtime},
                           {"Start_time:": starttime1, "End_time:": endtime1},
                           {"Start_time:": starttime2, "End_time:": endtime2}]

        members.objects.create(Emp_id=uid, real_name=name, tz=tz, activity_periods=starttimefinal2)
        #print(uid,name,tz,starttimefinal2)
        
        
emp_start = 3200
emp_end = 3230

populate_profile(emp_start, emp_end)
