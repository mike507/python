import os
import glob

pyprogs = [p for p in glob.glob('*.py') ]
currdir = os.getcwd()
print('[' + os.getcwd() + ']')
os.system("echo %s %s > tmp.txt" % ("Result of python programms from ", currdir))

for program in pyprogs:
    print('\t', program)
    #os.system("python %s >> tmp.txt" % program)