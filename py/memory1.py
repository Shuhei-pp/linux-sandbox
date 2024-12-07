import os
import sys
import time

data = 10000

print("データの値は", data, "です")
print("今は現在の時間は", time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime()), "です")
pid = os.fork()

if pid == 0:
    data = 20000
    print("子プロセス: data =", data)
    print("子プロセスID =", os.getpid())
    print("子プロセス: 現在の時間は", time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime()))
    exit(0)


os.wait()
print("親プロセス: data =", data)
print("親プロセスID =", os.getpid())
print("親プロセス: 現在の時間は", time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime()))
