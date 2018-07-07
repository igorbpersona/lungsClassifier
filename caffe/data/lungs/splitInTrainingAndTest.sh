#!/bin/bash
#script to split images in 20% for test and 80% for train

#loop through resizedData folders
for folderName in resizedData/*; do
	cd $folderName
	numberOfFiles="$(ls -l | grep ^- | wc -l)"

	#gets 20% of the images quantity
	testQty="$(expr $numberOfFiles \* 2 / 10)"

	i=0

	#loop to populate test folder
	echo -e "Populating test folder"
	for fileName in *; do
		let "i++"
		cp $fileName ../../test/$fileName
		if [ $i -eq $testQty ]
		then
			 break
		fi
	done
	echo -e "Done."

	i=0

	#loop to populate train folder
	echo -e "Populating train folder"
	for fileName in *; do
		let "i++"
		cp $fileName ../../train/$fileName
	done
	echo -e "Done."
	echo -e ""

	cd ../..
done
