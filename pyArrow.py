# Created by Y.S.Murakami, Nov.28 2021
# Early prototype just for fun

import time

N = 10
for i in range(N):
    print(f'\rprocessing... |',end='')
    for _ in range(i):
        print('-',end='')
    print('>',end='')
    for _ in range(N-i-1):
        print(' ',end='')
    print('|',end='')
    time.sleep(1)
