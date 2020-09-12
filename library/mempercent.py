#!/usr/bin/env /usr/libexec/platform-python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, canit00 <[email protected]>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""A simple python script to determine memory utilization percentage.
"""

from __future__ import print_function
import psutil,json

def main():
    mem_percentage_used = psutil.virtual_memory().percent
    if mem_percentage_used < 85.0:
        print(json.dumps({
            "memory" : mem_percentage_used,
            "changed" : False
        }))

    elif mem_percentage_used >= 85.0:
        print(json.dumps({
            "memory" : mem_percentage_used,
            "mem_threshold" : "exceeded",
            "mem_threshold" : True,
            "changed" : False
        }))

if __name__ == '__main__':
    main()
