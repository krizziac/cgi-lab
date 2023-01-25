#!/usr/bin/env python3

'''
Code derived from following TA demo on Jan 23, 2023 Lab
'''

import os, json
print("Content-Type: application/json")
print(os.environ)
print("")
print(json.dumps(dict(os.environ),indent=2))