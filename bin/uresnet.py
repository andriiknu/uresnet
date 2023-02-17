#!/usr/bin/python
import os
import sys
URESNET_DIR = os.path.dirname(os.path.abspath(__file__))
URESNET_DIR = os.path.dirname(URESNET_DIR)
print(URESNET_DIR)
sys.path.insert(0, URESNET_DIR)
sys.path.insert(1, "/home/andrii/master/uresnet_pytorch/uresnet")
sys.path.insert(0, "/home/andrii/master/uresnet_pytorch/uresnet/iotools")
sys.path.insert(1, "/home/andrii/master/uresnet_pytorch/uresnet/models")
from uresnet.flags import URESNET_FLAGS

def main():
    # import  pdb
    # pdb.set_trace()
    flags = URESNET_FLAGS()
    flags.parse_args()

if __name__ == '__main__':
    main()
