#!/usr/bin/python3
import os
import binascii
import random

f=open("/dev/random",'rb') # /dev/randomを開く
random32bitdata=f.read(4) # ４バイト読み出し
f.close() # /dev/randomを閉じる
randomhex=binascii.hexlify(random32bitdata) #１６進の文字列に変換
randomseed=int(randomhex,16) # 整数に変換
random.seed(randomseed) # ランダムシードを初期化
for _ in range(10):
 print(random.random())
