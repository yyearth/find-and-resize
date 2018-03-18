#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: youyang time:2018/3/16 17:23 

import os
from glob import glob
import cv2
import numpy as np
from shutil import rmtree
import time
from processing import process_img, show_and_hold

num = 0

# print(os.getcwd())
# print(os.listdir(os.getcwd()))
targ_path = os.getcwd() + '/first blood'

print('Please wait...')
time.clock()

if os.path.isdir(targ_path):
    rmtree(targ_path, True)
    os.makedirs(targ_path)
else:
    os.makedirs(targ_path)

dir_list = os.listdir(os.getcwd())
# print(dir_list)
for c_dir in dir_list:
    # print(c_dir)
    if os.path.isdir(c_dir) and '.' not in c_dir and '_' not in c_dir \
            and 'Include' not in c_dir and 'lib2to3' not in c_dir:

        # print(c_dir)
        target = targ_path + '/yy_' + c_dir
        # print(target)
        os.makedirs(target)
        for fn in glob(c_dir + '/*.png'):
            # print(fn)
            new = process_img(fn)
            f = fn.split('\\')
            # print(f)
            cv2.imwrite('first blood/yy_' + c_dir + '/yy_' + f[1], new)
            # print(target + '/yy_' + f[1])
            num += 1
            print(str(num) + ': ' + c_dir + '/yy_' + f[1])

            # show_and_hold('img', new)

end = time.clock()
print('>>>>>>>>Done! %d pics finished in %.2f secs!<<<<<<<<' % (int(num), end))

s = input('>>>> yy 2018.03.16  https://github.com/yyearth <<<<')

# cv2.waitKey() # can not use for pyinstaller

