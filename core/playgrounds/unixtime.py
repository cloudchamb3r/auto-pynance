from time import time 
from datetime import datetime

print(int(time()))


# 분 단위로 끊기
epoch_now = 60 * (int(time()) // 60) 
print(epoch_now)

print(datetime.fromtimestamp(epoch_now))

epoch_milis_now = epoch_now * 1000
