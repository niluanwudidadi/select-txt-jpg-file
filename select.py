# -*- encoding:utf-8 -*-
#! /usr/bin/env python

import glob
import numpy as np
import shutil

#---------------------------------------read txt dir ,return txt file list, used for find jpg according to empty txt file-----------------------------------------------------
def read_txt_file(dir_name):
	len_of_dir = len(dir_name) + 3
	dir = './' + dir_name + '/' + '*.txt'
	txts=glob.glob(dir)
	txt_list = []
	for i in range(0,len(txts)):
	    temp = txts[i]
	    txt_list.append(temp[len_of_dir:])
	return txt_list

#---------------------------------------read jpg dir, return jpg file list----------------------------------------------------------------
def read_file(dir_name):

	# dir_name = '红盖白提环(1907)'
	# dir_name = '红盖红提环(197)'
	len_of_dir = len(dir_name) + 3
	# print len_of_dir
	dir = './' + dir_name + '/' + '*.jpg'
	imgs=glob.glob(dir)
	img_list = []
	# print type(imgs)
	for i in range(0,len(imgs)):
	    temp = imgs[i]
	    img_list.append(temp[len_of_dir:])
	# print img_list
	return img_list


#-------------------------------------random select file, return luck_list-------------------------------------------------------------------
def random_select(img_list, ratio = 10):
	num_of_img = len(img_list)
	print "num_of_img:", num_of_img
	luck = np.random.randint(0, num_of_img, size = int(num_of_img / ratio))
	list_luck = []
	for i in xrange(0,len(luck)):
		list_luck.append(img_list[luck[i]])
	list_luck = list(set(list_luck))
	print "num_of_test:", len(list_luck)
	return list_luck

def copy_img_to_file(dir_name, luck_list, test_img_dir, train_img_dir):
	
	train_list = list(set(img_list)^set(luck_list))
	print "num_of_train:", len(train_list)

#---------------------------------copy test_img to test_img_dir-----------------------------------------------------------	
	for item in luck_list:
		copy_img_name = './' + dir_name + '/' + item
		test_img_name = './' + test_img_dir + '/' + item
		# print "test:", copy_img_name
		shutil.copyfile(copy_img_name, test_img_name)

#---------------------------------copy train_img to train_img_dir---------------------------------------------------------
	for item in train_list:
		copy_img_name = './' + dir_name + '/' + item
		train_img_name = './' + train_img_dir + '/' + item
		# print "train:", copy_img_name
		shutil.copyfile(copy_img_name, train_img_name)

def copy_txt_to_file(txt_dir_name, test_img_list, train_img_list, test_txt_dir, train_txt_dir):
	
	# train_list = list(set(img_list)^set(luck_list))
	# print "num_of_train:", len(train_list)

#---------------------------------copy test_txt to test_txt_dir-----------------------------------------------------------	
	for item in test_img_list:
		copy_txt_name = './' + txt_dir_name + '/' + item[:-4] + '.txt'
		test_txt_name = './' + test_txt_dir + '/' + item[:-4] + '.txt'
		# print "test:", copy_txt_name, "====", test_txt_name
		shutil.copyfile(copy_txt_name, test_txt_name)

#---------------------------------copy train_txt to train_txt_dir---------------------------------------------------------
	for item in train_img_list:
		copy_txt_name = './' + txt_dir_name + '/' + item[:-4] + '.txt'
		train_txt_name = './' + train_txt_dir + '/' + item[:-4] + '.txt'
		# print "train:", copy_txt_name, "====", train_txt_name
		shutil.copyfile(copy_txt_name, train_txt_name)

def move_empty_jpg_to_file(jpg_dir, empty_txt_list, empty_jpg_dir):
	#---------------------------------move empty_jpg to empty_jpg_dir-----------------------------------------------------------	
	for item in empty_txt_list:
		move_jpg_name = './' + jpg_dir + '/' + item[:-4] + '.jpg'
		empty_jpg_name = './' + empty_jpg_dir + '/' + item[:-4] + '.jpg'
		# print "move:", move_jpg_name, "====", empty_jpg_name
		shutil.move(move_jpg_name, empty_jpg_name)

if __name__ == '__main__':
	ratio = 10
	# dir_name = 'blue_cap_blue_ring(101)'
	# dir_name = 'golden_cap(117)'
	# dir_name = 'golden_cap_golden_ring(1606)'
	# dir_name = 'red_cap(73)'
	# dir_name = 'red_cap_red_ring(197)'
	# dir_name = 'red_cap_white_ring(1907)'
	# test_img_dir = 'test_jpg'
	# train_img_dir = 'train_jpg'

#----------------------------------------------random select train_set and test_set, then copy to test_img_dir and train_img_dir---------------------------------	
	# img_list = read_file(dir_name)
	# luck_list = random_select(img_list, ratio)
	# copy_img_to_file(dir_name, luck_list, test_img_dir, train_img_dir)
	


#----------------------------------------------copy the txt file according to jpg file---------------------------------------------------------
	# txt_dir_name = 'txt_all'
	# test_txt_dir = 'test_txt'
	# train_txt_dir = 'train_txt'

	# test_img_list = read_file(test_img_dir)
	# train_img_list = read_file(train_img_dir)
	# print "len of test img:", len(test_img_list)
	# print "len of train img:", len(train_img_list)
	# copy_txt_to_file(txt_dir_name, test_img_list, train_img_list, test_txt_dir, train_txt_dir)

#---------------------------------------------according empty txt file to move jpg----------------------------------------------------------------
	empty_jpg_dir = 'empty_jpg'
	empty_txt_dir = 'empty_txt'
	jpg_dir = 'jpg'
	empty_txt_list = read_txt_file(empty_txt_dir)
	print "len of empty txt:", len(empty_txt_list)
	move_empty_jpg_to_file(jpg_dir, empty_txt_list, empty_jpg_dir)
	# print len(ret_list)
	# for item in ret_list:
	# 	if item in luck_list:
	# 	   print "fuck the ", item
