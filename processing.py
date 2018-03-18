#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: youyang time:2018/3/16 16:18 

import numpy as np
import cv2
from glob import glob

blank = 5


def show_and_hold(winname, img):
    cv2.imshow(winname, img)
    cv2.waitKey()


def process_img(fn):
    img = cv2.imread(fn)
    # print(img.shape)
    if img is None:
        # raise Exception('load img fail')
        return
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_gray = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # img_gray = cv2.Canny(img_gray, 100, 300)
    img_gray, contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = max(contours[1:], key=lambda cur: cv2.arcLength(cur, True))
    # print(cnt)
    # cnt = contours[1]
    # print(len(contours))
    img = cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
    x, y, w, h = cv2.boundingRect(cnt)
    # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    # print(x, y, w, h)

    side = w if w > h else h
    # print(blank + (side // 2))
    center = (x + w // 2, y + h // 2)
    # print('center:', center)
    start = center[0] - (blank + (side // 2)), center[1] - (blank + (side // 2))
    stop = center[0] + (blank + (side // 2)), center[1] + (blank + (side // 2))

    # cv2.rectangle(img, start, stop, (0, 255, 0), 2)

    if h > w:
        cut = img_gray[start[1]:stop[1], start[0]:stop[0]]
    else:
        cut = img_gray[start[0]:stop[0], start[1]:stop[1]]
    # print(start[1], stop[1], start[0], stop[0])
    # print(start[0], stop[0], start[1], stop[1])
    resized = cv2.resize(cut, (28, 28))
    # print(resized.shape)

    return resized


if __name__ == '__main__':
    fn = '43_00015.png'
    fn2 = '41_00006.png'
    p = process_img(fn2)
    cv2.imshow('img', p)
    cv2.waitKey()
