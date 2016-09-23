import datetime
def recurringTask(firstDate, k, daysOfTheWeek, n):
    
    days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
    days_rev = dict((v,k) for k,v in days.iteritems())

    day=int(firstDate[:2])
    month=int(firstDate[3:5])
    year=int(firstDate[6:])

    count_week=1
    count=n
    current_day=datetime.date(year,month,day).weekday()+1
    current_date=firstDate
    repeating_days=[]
    repeating_days_dist=[]
    result=[]

    for i in daysOfTheWeek:
        repeating_days.append(days_rev[i])

    repeating_days.sort();

    if len(repeating_days)==1:
        repeating_days_dist.append(7)
    else:
        for i in range(1,len(repeating_days)):
            repeating_days_dist.append(repeating_days[i] - repeating_days[i-1])
        repeating_days_dist.append(7-sum(repeating_days_dist))

    dist_point = repeating_days.index(current_day)

    result.append(current_date)
    count -= 1

    day=int(firstDate[:2])
    month=int(firstDate[3:5])
    year=int(firstDate[6:])
    current_date=datetime.date(year,month,day)

    if count>0:
        while count>0:
            if count_week == len(repeating_days_dist):
                a = (k-1)*7 + repeating_days_dist[dist_point]
                current_date += datetime.timedelta(days=a)
                if dist_point == len(repeating_days_dist)-1 :
                    dist_point=0
                else:
                    dist_point += 1
                count_week=1
                result.append(current_date.strftime("%d/%m/%Y"))
            else:
                a = repeating_days_dist[dist_point]
                current_date += datetime.timedelta(days=a)
                if dist_point == len(repeating_days_dist)-1 :
                    dist_point=0
                else:
                    dist_point += 1
                count_week += 1
                result.append(current_date.strftime("%d/%m/%Y"))

            count -= 1
            
    return result
