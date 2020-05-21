txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
    t.sort(reverse=True)
print("its me t",t)
res = list()
for length, word in t:
    res.append(word)
print(res)





















name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle :
	line = line.rstrip()
	if line == "": continue
	words = line.split()
	if words[0] != "From" : continue
	time = words[5].split(":")
	counts[time[0]] = counts.get(time[0], 0) + 1

list = list()

for key,value in counts.items() :
	list.append((key,value))
list.sort()

for hour,count in list :
	print (hour, count)








"""
text = "X-DSPAM-Confidence:    0.8475"
aa = text.find ('0')
#search for empty starting from value of aa =>0
bb = text.find ('', aa)
outis=text[bb:]

outis=float(outis)
print("out is",outis )


===============================
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
agg=0
c=0
for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    c+=1
    aa = line.find ('0')
    num=line[aa:]
    num=float(num)
    agg=agg+num
    #print(num)
    
    
res=agg/c    
#print("Done")
print("Average spam confidence:",res)
========================

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
totallst=list()
for line in fh:
    line=line.rstrip()
    lst=line.split(' ')
    for word in lst:
        if word not in totallst:
            totallst.append(word)
    #print(lst)
    
totallst.sort()
print( totallst)

=======================
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read()
c=dict()

senders = dict()
for line in handle:
    if not line.startswith("From:"):continue
    line = line.split()
    line = line[1]
    senders[line] = senders.get(line, 0) +1

bigcount = None
bigword = None
for word,sender in senders.items():
    if bigcount == None or sender > bigcount:
        bigword = word 
        bigcount = sender 

print (bigword, bigcount)
"""


