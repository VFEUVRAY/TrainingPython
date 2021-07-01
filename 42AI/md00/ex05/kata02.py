import datetime

values = (3, 30, 2019, 9, 25)

today = datetime.datetime(values[2], values[3], values[4], values[0], values[1])
print (str(today.month) , '/' , today.day , '/',  today.year , ' ' , today.hour , ':' , today.minute, sep='')
print ("%d/%d/%d %d:%d" % (today.month, today.day, today.year, today.hour, today.minute))
print ("(%04d)" % 223)