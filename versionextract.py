import re

regex = r'''(\d+\.\d+\.\d+\-\d+)'''

regex_short1 = r'''(\d+\.\d+\-\d+)'''

regex_short2 = r'''(\d+\-\d+)'''


f = open('in.csv')

line = f.readline()
while line:
    subs = re.split(regex, line)
    if (len(subs) < 2):
        subs = re.split(regex_short1, line)
    if (len(subs) < 2):
        subs = re.split(regex_short2, line)



    if (len(subs) == 2):
        print(f"{line[:-1]},  {subs[0][:-1]}, {subs[1]}")
    elif (len(subs) == 3):
        print(f"{line[:-1]},  {subs[0][:-1]},  {subs[1]}{subs[2][:-1]}")
    else:
        print(f"{line[:-1]},  {subs[0][:-1]}, ???")
    line = f.readline()






