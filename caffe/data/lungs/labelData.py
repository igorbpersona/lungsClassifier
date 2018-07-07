import os
from shutil import copyfile

for foldername in os.listdir('resizedData'):
	for filename in os.listdir('resizedData/' + foldername):
		#get lung class from splited filename decreased by 1
		lungClass = int(filename.split('.')[0].split('_')[-1]) - 1

		#copy file to labeledData folder
		src = 'resizedData/' + foldername + '/' + filename
		dst = 'labeledData/' + str(lungClass) + '/' + filename
		copyfile(src, dst)

		print lungClass
		#TODO: split name, by the final number copy file to folder in labeledData