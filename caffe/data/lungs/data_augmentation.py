import cv2
import imutils
import math
import numpy as np
import os

from PIL import Image


def augmentation(path, operations):
	print "aumentando base.."

	files = [os.path.join(path, f) for f in os.listdir(path)
		if f.endswith('.png') and os.path.isfile(os.path.join(path, f))]
	print path

	names = []
	images = []
	for f in files:
		nam = f.split('/')[-1]

		image_pil = Image.open(f)
		image = np.array(image_pil)

#		cv2.imshow('', image)
#		cv2.imshow('rp', imutils.rotate(image, 90))
#		cv2.imshow('rm', imutils.rotate(image, -90))
#		cv2.imshow('fh', cv2.flip(image, 0))
#		cv2.imshow('fv', cv2.flip(image, 1))
#		cv2.imshow('fb', cv2.flip(image, -1))

		images.append(image)
		names.append(nam)

	if operations == 1:
		for im in range(len(images)):
			image = images[im].copy()
			name = names[im]

			# rotate_plus90
			cv2.imwrite(path+'/rp90_'+str(name), imutils.rotate(image, 90))


	if operations == 2:
		for im in range(len(images)):
			image = images[im].copy()
			name = names[im]

			# rotate_plus90
			cv2.imwrite(path+'/rp90_'+str(name), imutils.rotate(image, 90))
			# flip_both
			cv2.imwrite(path+'/fb_'+str(name), cv2.flip(image, -1))

	if operations == 3:
		for im in range(len(images)):
			image = images[im].copy()
			name = names[im]

			# rotate_plus90
			cv2.imwrite(path+'/rp90_'+str(name), imutils.rotate(image, 90))
			# rotate_minus90
			cv2.imwrite(path+'/rm90_'+str(name), imutils.rotate(image, -90))
			# flip_both
			cv2.imwrite(path+'/fb_'+str(name), cv2.flip(image, -1))

	if operations == 4:
		for im in range(len(images)):
			image = images[im].copy()
			name = names[im]

			# rotate_plus90
			cv2.imwrite(path+'/rp90_'+str(name), imutils.rotate(image, 90))
			# rotate_minus90
			cv2.imwrite(path+'/rm90_'+str(name), imutils.rotate(image, -90))
			# flip_horizontal
			cv2.imwrite(path+'/fh_'+str(name), cv2.flip(image, 0))
			# flip_vertical
			cv2.imwrite(path+'/fv_'+str(name), cv2.flip(image, 1))

	if operations >= 5:
		for im in range(len(images)):
			image = images[im].copy()
			name = names[im]

			# rotate_plus90
			cv2.imwrite(path+'/rp90_'+str(name), imutils.rotate(image, 90))
			# rotate_minus90
			cv2.imwrite(path+'/rm90_'+str(name), imutils.rotate(image, -90))
			# flip_horizontal
			cv2.imwrite(path+'/fh_'+str(name), cv2.flip(image, 0))
			# flip_vertical
			cv2.imwrite(path+'/fv_'+str(name), cv2.flip(image, 1))
			# flip_both
			cv2.imwrite(path+'/fb_'+str(name), cv2.flip(image, -1))


def main():

	folder = "../lung_blocks_DA/"

	# number of arq in each folder
	num = np.zeros(5)
	for i in range(1, 6):
		ret = os.popen("ls"+' '+ folder+"train/"+str(i)+"/*.png | wc -l")
		aux = ret.read()
		ret.close()
		num[i-1] = int(aux) #.split('\n')[0]

	# class with the major number of samples
	idx = np.argsort(-num)
	max = idx[0]

	# verify wich one have to be resampled
	augm = np.zeros(5)
	for i in xrange(num.shape[0]):
		if max != i:
			div = round(num[max] / num[i], 1)
			# division must be greater or equals 2
			# lesser than 2 means that the amount of samples is almost the same
			# of the amount of the class with the major number
			if div >= 2:
				# amount of operations
				augm[i] = math.floor(div-1)

	for i in xrange(augm.shape[0]):
		if augm[i] > 0:
			augmentation(folder+"train/"+str(i+1), augm[i])


if __name__ == "__main__":

	main()

