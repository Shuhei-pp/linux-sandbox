#!/bin/bash

# 繰り返す（./mainっていう処理を一つのcpuで引数の数だけ行う）
for i in `seq 1 $1`
do
   taskset -c 0 ./main $1 &
done