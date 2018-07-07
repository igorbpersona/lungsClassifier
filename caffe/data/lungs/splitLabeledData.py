import os
import shutil


valFile   = open('val.txt', 'w')
trainFile = open('train.txt', 'w')
testFile  = open('test.txt', 'w')

#clear txt files
valFile .write("")
trainFile.write("")
testFile.write("")

valFile.close()
trainFile.close()
testFile.close()

for foldername in os.listdir('labeledData'):

	imgCount = len([name for name in os.listdir('labeledData/' + foldername)])
	trainCount = int(imgCount * 0.7)
	valCount = int(trainCount * 0.2)

	i = 0
	#open txt files
	valFile   = open('val.txt', 'a')
	trainFile = open('train.txt', 'a')
	testFile  = open('test.txt', 'a')

	#loop to populate folders
	for filename in os.listdir('labeledData/' + foldername):
		src = 'labeledData/' + foldername + '/' + filename

		#set val folder to put image in
		if i < valCount:
			valFile.write(filename + " " + foldername + "\n")
			dst = 'val/' + filename
			i += 1

		#set train folder to put image in
		elif i < trainCount:
			trainFile.write(filename + " " + foldername + "\n")
			dst = 'train/' + filename
			i += 1

		#set test folder to put image in
		else:
			testFile.write(filename + " " + foldername + "\n")
			dst = 'test/' + filename
		
		#move file
		shutil.move(src, dst)

	#close txt files
	valFile.close()
	trainFile.close()
	testFile.close()