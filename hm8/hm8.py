import datetime



users = {
    "Liana": datetime.datetime(2004, 3, 16),
    "Tomas": datetime.datetime(2001, 3, 13),
    "Robert" : datetime.datetime(1999, 3, 17)
    }



def get_birthdays_per_week(u):
    weekday = {
    "Monday":[],
     "Tuesday":[],
     "Wednesday":[],
     "Thursday":[],
     "Friday":[]
    }
    today = datetime.datetime.now().day
    mon = datetime.datetime.now().month
    difference = (datetime.datetime.now() + datetime.timedelta(days=7)).day
    for name, bd in users.items():
        if bd.month == mon:
            if today<=bd.day<=difference:
                dayofweek = bd.strftime('%A')
                if dayofweek in weekday:
                    weekday[dayofweek].append(name)
                else:
                    weekday["Monday"].append(name)
    res = ""
    for key, val in weekday.items():
        if len(val)>=1:
            names = ", ".join(val)
            res+= f"{key}: {names}\n"
    print(res)
            

if __name__== "__main__":
    get_birthdays_per_week(users)