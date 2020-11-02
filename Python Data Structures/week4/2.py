"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

"""
_file = input("Enter file:")
if len(_file) < 1 : _file = "mbox-short.txt"
handler = open(_file)
hour_count = dict()
for line in handler :
	line = line.rstrip()
	if line == "": continue
	words = line.split()
	if words[0] != "From" : continue
	time = words[5].split(":") 
	#print(time)
        #get hour  
        # dic key is value of hour
	hour_count[time[0]] = hour_count.get(time[0], 0) + 1

print(hour_count)
#tuple
_list= list()
for key,value in hour_count.items() :
	_list.append((key,value))
_list.sort()
print(_list)

for hour,count in _list :
	print (hour, count)
