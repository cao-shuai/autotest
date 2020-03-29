#!/usr/bin/env python
#coding: utf-8

import os
import random

class QuickSort(object):

    def sort(self, camparble):
        print("befor sort camparble")
        print(camparble)
        values=self.__sort__(camparble)
        print("sort later")
        print(values)

    def __sort__(self, camparble):
        if(len(camparble) < 2):
              return camparble
        mind= len(camparble)//2
        mindvalue= camparble[mind]

        left=[]
        right=[]
        camparble.remove(mindvalue)
        for item in camparble:
                if item >= mindvalue:
                    right.append(item)
                else:
                    left.append(item)
        return self.__sort__(left)+[mindvalue]+self.__sort__(right)
                    


if __name__=='__main__':
    quicksort = QuickSort()
    arrs = [random.randrange(1,100) for _ in range(50)]
    quicksort.sort(arrs)
