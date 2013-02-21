import os, re, string

def run_once(n,inf_name):
	numthread=n
	inputfilename=inf_name
	source_sdname='sd.c'

	inputdatarawname=os.path.splitext(os.path.basename(inputfilename))[0]
	print "\nThread num %d. \t Data file %s. Rawname %s\n"%(numthread,inputfilename,inputdatarawname)

	numthread_w=r'#define NTHREADS '+str(numthread)
	print numthread_w

	find_nthreads=re.compile('#define NTHREADS .*')
	source_code_fin=open(source_sdname,'r')
	m=re.sub(find_nthreads,numthread_w,source_code_fin.read())
	source_code_fin.close()
	source_code_fout=open('sd.c','w')
	source_code_fout.write(m)
	source_code_fout.close()

	os.system('make clean')
	os.system('make')

	outputfilename_serial=inputdatarawname+'_s.nbrs'
	outputfilename_parallel=inputdatarawname+'_p.nbrs'

	outputfilename_serial_reorder=inputdatarawname+'_rs.nbrs'
	outputfilename_parallel_reorder=inputdatarawname+'_rp.nbrs'

	logfilename_serial=inputdatarawname+'_s.log'
	logfilename_parallel=inputdatarawname+'_p.log'

	difffilename=inputdatarawname+'_diff.nbrs'

	arglist=' -nnbrs=20 -minsim=.3 '+inputfilename

	os.system('touch '+logfilename_serial)
	os.system('touch '+logfilename_parallel)

	cmd_s='\n./sd_serial '+arglist+' '+outputfilename_serial +' > '+logfilename_serial
	cmd_p='\n./sd '+arglist+' '+outputfilename_parallel+' > '+logfilename_parallel

	print cmd_s
	os.system(cmd_s)
	os.system('cat '+logfilename_serial)

	print cmd_p
	os.system(cmd_p)
	os.system('cat '+logfilename_parallel)


	os.system('touch '+outputfilename_serial_reorder)
	os.system('touch '+outputfilename_parallel_reorder)

	cmd_sort_s='sort -n -k 1 -k 2 '+outputfilename_serial+ '> '+outputfilename_serial_reorder
	cmd_sort_p='sort -n -k 1 -k 2 '+outputfilename_parallel+ '> '+outputfilename_parallel_reorder

	print cmd_sort_s
	os.system(cmd_sort_s)


	print cmd_sort_p
	os.system(cmd_sort_p)

	cmd_diff='diff '+outputfilename_serial_reorder+' '+ outputfilename_parallel_reorder+'> '+difffilename
	print cmd_diff
	os.system(cmd_diff)

	print ('head -n 20 '+difffilename)
	os.system('head -n 20 '+difffilename)

datapath='/home/xuxxx625/p/ahw2/hw2_data/'
numthread=8
filelist=os.listdir(datapath)
matfilelist=[file for file in filelist if file.endswith(".mat")]
print matfilelist

for f in matfilelist:
	print "\n==============================================\n",f
	run_once(numthread, datapath+f)

