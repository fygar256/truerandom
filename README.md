info.py

円周率πは無限大の情報量を持ち、全ての情報を含んでいます。

このプログラムは円周率を発生させ、文字にデコードし、円周率に含まれる情報を取り出します。

意中の人の電話番号も、もちろん円周率の中に含まれているので、πを持っているだけで、「意中の人の電話番号の情報を持っている」と言えます。但し、πの中のどこからどこまでかは分からないため、「意中の人の電話番号を知っている」とは言えません。

πを持っているだけで、と書きましたが、持っているπの桁数が有限ならば、その中に意中の人の電話番号がない可能性があるので、その場合、意中の人の電話番号を持っているとは言えません。

このプログラムのデコード方法は、i=" 0123456789.,abcdefghijklmnopqrstuvwxyz"という文字列を使い、十進数で２桁ずつ区切って100で割り、iの長さを掛けて、iに当てはめるというものです。

取り出せる情報はデコード方法によって変わります。πは上質の乱数列なので、殆どが無駄な情報で、実用的とは言えませんが、無限に続ければ多分期待した文字列は出てくるので、辛抱強く待ち続けましょう。但し、多分その前に地球が滅亡してしまうでしょう。

このプログラムのような単純なデコード方法で、円周率の中から任意の情報を引き出すことができるかどうかは、可能、不可能、2つの説があります。

πの発生はガウス・ルジャンドル法に依ります。

何もかも知ってをるなり竈猫　富安風生

意中の人の電話番号は、竈猫に聞いたら分かりますが、猫はナンバーを喋れないので、猫語のデコードが必要です。πは竈猫です。

```info.py
!/usr/bin/python3
import sys
k, a, b, a1, b1 = 2, 4, 1, 12, 4
i=" 0123456789.,abcdefghijklmnopqrstuvwxyz"
f=0
while(True):
  # Next approximation
  p, q, k = kk, 2k+1, k+1
  a, b, a1, b1 = a1, b1, pa+qa1, pb+qb1
  # Print common digits
  d = a / b
  d1 = a1 / b1
  n1=-1
  while(d == d1):
    if n1==-1:
        pass
    else:
        n=int((int(n1)10+int(d))/100len(i))
        print(i[n],end='')
    n1=d
    sys.stdout.flush()
    a, a1 = 10(a%b), 10(a1%b1)
    d, d1 = a/b, a1/b1
```

完全乱数からはこのデコード方法で任意の情報を取り出せるので、

以下のプログラムを持っているだけで、「意中の人の電話番号を取り出すことのできるプログラムを持っている」と言えます。但し、現存のコンピュータは今の所有限なので、チューリングマシンが必要です。

```phoneno.py
!/usr/bin/python3
import os
import binascii
def main():
    f=open("/dev/random",'rb') # /dev/randomを開く
    while(1):
        randomdata=f.read(1) # 1バイトの完全乱数の読み出し
        randomhex=binascii.hexlify(randomdata) #１６進の文字列に変換
        randomint=int(randomhex,16) # 整数に変換
        i='0123456789 '
        n=randomint/255*len(i)
        print(i[n],end='')
    f.close() # /dev/randomを閉じる
    return
if name=='main':
    main()
    exit(0)
```
