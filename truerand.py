#!/usr/bin/python3
#
# truerand.py
# pythonで、/dev/randomからの真性乱数を利用して乱数を発生するモジュール
#
import os
import binascii

# n byteのRAND_MAXを返す関数
# in : n バイト長
# out: nバイトのRAND_MAX
def rand_max(n):
    v=0
    for i in range (0,n):
        v=v*256+0xff
    return(v)

# n byte の真性乱数を返す関数
# in : n バイト長
# out:   n バイトの正の整数の乱数
def rand(n):
    f=open("/dev/random",'rb') # /dev/randomを開く
    randomdata=f.read(n) # nバイト読み出し
    f.close() # /dev/randomを閉じる
    randomhex=binascii.hexlify(randomdata) #１６進の文字列に変換
    randomint=int(randomhex,16) # 整数に変換
    return(randomint)

#
# n byte の精度の[0,1)の実数乱数を返す関数
# in : n バイト長
# out:   n バイトの正の整数の乱数
#
def rand_f(n):
    return(rand(n)/rand_max(n))

#
# 0〜n-1の乱数を返す関数
# in : n バイト長
# out: 0〜(n-1)の整数乱数
#
def randomint(k,n):
    return(int(rand(n)/rand_max(n)*k))

if __name__=="__main__":
    b=8
    times=20
    print(f"{b*8}bit正の真性整数乱数")
    for _ in range(times):
        print(rand(b),end=" ")

    print("")
    print("実数[0,1)の範囲の実数乱数")
    for _ in range(times):
        print(rand_f(b),end=" ")
    print("")
    print("整数0〜99の乱数")
    for _ in range(times):
        print(randomint(100,b),end=" ")
    print("")
