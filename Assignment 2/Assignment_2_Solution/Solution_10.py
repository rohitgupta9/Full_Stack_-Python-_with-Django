import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
# Here %H are used 24 hours
# And %I are used 12 hours
print (now.strftime("%d-%m-%Y and %H:%M %p"))
print (now.strftime("%d-%m-%Y and %I:%M %p"))