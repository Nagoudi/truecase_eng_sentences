import argparse
import glob
import os
import json
import time
import logging
import random
import re
import truecase






infile="Results_ST/mt_msaea_eng.txt"
out_file="Results_ST/MT_msaea_eng.txt"
f_in=open(infile, 'r')
f_out=open(out_file, 'w')





for line in f_in:
    cpt_line=truecase.get_true_case(line)
    f_out.write("{}\n".format(cpt_line))


f_in.close()
f_out.close()




