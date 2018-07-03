'''
File Name:    main.py
Description:  主函数，调用其他方法
Author:       jwj
Date:         2018/1/7
'''
__author__ = 'jwj'

from NovelList import *

if __name__ == '__main__':
    url = 'http://www.quanshuwang.com/list/1_%s.html'
    for page in range(1, 2):                         # range范围可修改
        novelsObjList = getNovelsInfo(url % page)
        novelsObjList = get_Chapters_Url(novelsObjList)
        # write2csv(novelsObjList)
        allChaptersUrl(novelsObjList)