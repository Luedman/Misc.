import math
import numpy as np
import scipy.misc as smp

def rn_generator(gen_numbers, seed = 1, a = 1664625, b = 1013912228, m = math.pow(2,32)):

    result =[]

    def next_rand(seed):
        seed = (a*seed + b) % m
        return seed

    for x in range(0,gen_numbers + 1):
        seed = next_rand(seed)
        if seed in result:
            i = result.index(seed)
        result.extend([seed])

    pic_dims = int(math.sqrt(gen_numbers)) + 1

    return result, pic_dims, m

result, pic_dims, m    = rn_generator(100000)
pic_data               = np.zeros((pic_dims,pic_dims,3), dtype=np.uint8 )

for y in range(1,pic_dims):
    for x in range(1,pic_dims):
        if result[y*x]/m < 0.5:
            pic_data[x,y] = [254,254,254]

img = smp.toimage(pic_data)
img.show()
