import numpy as np
import ctypes
import time
from PIL import Image

ITERATION_COUNT = 10

lib = ctypes.CDLL('./lib.dll')

lib.getDepth.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_float))
lib.getDepthShape.restype = ctypes.POINTER(ctypes.c_int)

tmp_shape = lib.getDepthShape()

print("Getting started..", end="\n")

for n in range(ITERATION_COUNT):
    tmp_arr = lib.getDepth()

    arr = []
    # DATA TRANSFORMING
    for i in range(tmp_shape[0]):
        row = []
        for j in range(tmp_shape[1]):
            row.append(tmp_arr[i][j])
        arr.append(row)

    max_val = 0.0
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            if float(max_val) < float(arr[x, y]):
                max_val = float(arr[x, y])

    koeff = 255 / round(max_val, 2)

    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            arr[x, y] = int(float(arr[x, y]) * koeff)

    arr = arr.astype(np.int8)

    im = Image.fromarray(arr, mode="L")
    im.save(f"./output/img_{n}.png")

    print(f"Image number {n + 1} has been saved", end="\n")

    time.sleep(0.2)
