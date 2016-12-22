#!python3
import sys
import argparse

def createParser ():
  parser = argparse.ArgumentParser()

  parser.add_argument("-s", "--size", type=int, required=True, help="size in megabytes (if -g, then gigabytes)")
  parser.add_argument("-f", "--file", required=True, help="file name")
  parser.add_argument("-g", "--gigabytes", action='store_const', const=True, default=False)

  return parser

parser = createParser()
ns = parser.parse_args()

if (ns.size < 1) or (ns.size > 9999999):
  print("Invalid parameter! Allowed only the numbers 1 to 9999999")
  sys.exit(1)

size = ns.size
if ns.gigabytes:
  size = size * 1024

f=open(ns.file, "w")
f.seek(1024 * 1024 * size)
f.write("\0")
