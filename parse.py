#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs

with open('input', 'r') as input_file:
    input_log = input_file.readlines()
f2 = open('out.sh', 'w')
f2.write("#!/bin/bash\n")

output = []

for i in range(0,len(input_log)):
    si_string = input_log[i].find('service_inet_')
    if si_string > -1:
        z = input_log[i][si_string:].split(';', 1)
        out_serv = z[0].strip()
        for j in range(i,len(input_log)):
            ip_string = input_log[j].find('Получили ')
            if ip_string > -1:
                out_ip = input_log[j][ip_string+16:].strip()
                output.append([out_serv,out_ip])
                break

for k in range(0,len(output)):
    f2.write('java -jar /home/dotza/tools/changeip/updater.jar ' + output[k][0] +
             ' ' + output[k][1] + '\n')
print 'done'
