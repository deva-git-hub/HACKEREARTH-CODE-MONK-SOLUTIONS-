# Monk and Sorting Algorithm - python 3 solution

import io, os, sys

input = io.BytesIO(os.read(0, \
         os.fstat(0).st_size)).readline

n = int(input().decode())
arr = list(map(int,input().decode().split()))
mx = max(arr) 
den = 1

while mx // den:
    arr.sort(key = lambda x: (x // den) % 100000 )
    den *= 100000
    sys.stdout.write(
        " ".join(map(str, arr)) + "\n"
    )
   