import os, sys
import time

# define the granularity for sampling
interval = 1

# get the vm stat from the system
# list of stats needs to collect:
stats = [
'v_inactive_count',
'v_inactive_target',
'v_active_count',
'v_free_count',
'v_free_min',
'v_free_target',
'v_free_reserved',
'v_pdpages',
'v_pdwakeups',
'v_vnodepgsout',
'v_vnodepgsin',
'v_vnodeout',
'v_vnodein',
'v_swappgsout',
'v_swappgsin']

cmd = "sysctl vm.stats.vm"

outfile = open('stats.csv','w+')
outfile.write('time,')
for i, st in enumerate(stats):
    if i is len(stats)-1:
        outfile.write(st+'\n')
    else:
        outfile.write(st+',')

# start the timer
beginner = time.time()

for idx in range(5):
    checker = time.time()
    res = os.popen(cmd).readlines()
    outfile.write("%.3f"%(checker-beginner)+',')
    for i, st in enumerate(stats):
        reslist = [my_str for my_str in res if st in my_str]
        pair = reslist[0].split(":")
        if i is len(stats)-1:
            outfile.write(pair[1].rstrip()+'\n')
        else:
            outfile.write(pair[1].rstrip()+',')
    time.sleep(interval)
outfile.close()

print "finished writting file."
