# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import time
import argparse
from diskannpy import Metric, Parameters, DiskANNFloatIndex

# parser = argparse.ArgumentParser()
# parser.add_argument('data_path', type=str, help='Path to the input base set of vectors.')
# parser.add_argument('save_path', type=str, help='Path to the built index.')
# parser.add_argument('R', type=int, help='Graph degree.')
# parser.add_argument('L', type=int, help='Index build complexity.')
# parser.add_argument('B', type=float, help='Memory budget in GB for the final index.')
# parser.add_argument('M', type=float, help='Memory budget in GB for the index construction.')
# parser.add_argument('T', type=int, help='Number of threads for index construction.')

data_path = '/home/ubuntu/LEQAT/data/sift1M/base.fbin'
save_path = '/home/ubuntu/index/diskann'
R=32
L=125
B=0.03
M=3
T=8

# args = parser.parse_args()

start = time.time()
index = DiskANNFloatIndex(Metric.L2)
print("start build")
index.build(data_path, save_path, R, L, B, M, T)
end = time.time()

print("Indexing Time: " + str(end - start) + " seconds")