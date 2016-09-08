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

sys_info = "sysctl hw.physmem hw.ncpu"
res = os.popen(sys_info).readlines()

# sys_info_file = open('sys_info.txt','w+')
# for line in res:
    # sys_info_file.write(line)
# sys_info_file.close()

pair = res[0].split(":")
file_string = "stats_mem"+pair[1].rstrip()
pair = res[1].split(":")
file_string += "_cpu"+pair[1].rstrip()+".csv"

cmd = "sysctl vm.stats.vm"

outfile = open(file_string,'w+')
# for line in res:
    # outfile.write(line)
outfile.write('time,')
for i, st in enumerate(stats):
    if i is len(stats)-1:
        outfile.write(st+'\n')
    else:
        outfile.write(st+',')

# start the timer
beginner = time.time()

while 1 :
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
