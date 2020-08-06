import re

regex = r'''(\d+\.\d+\.\d+\-\d+)'''

#print(re.findall(regex, str)[0])  # prints ['1.4.2.4']

f = open('in.csv')

line = f.readline()
while line:
    subs = re.split(regex, line)
    if (len(subs) == 2):
        print(f"{line[:-1]},  {subs[0][:-1]}, {subs[1]}")
    elif (len(subs) == 3):
        print(f"{line[:-1]},  {subs[0][:-1]},  {subs[1]}{subs[2][:-1]}")
    line = f.readline()






