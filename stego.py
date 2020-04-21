#!/usr/bin python3
import argparse
from PIL import Image
import stepic
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--decode','-d',help='extract hidden message from image')
parser.add_argument('--encode','-e',help='include hidden message to image')

args = parser.parse_args()

if len(sys.argv) >= 2:
	if(sys.argv[1] in ["-d","--decode"]):
		img = Image.open(args.decode)
		msg = stepic.decode(img)
		print('Success')
		print(msg)
	elif(sys.argv[1] in ["-e","--encode"]):
		msg = input("input hidden message : ")
		img = Image.open(args.encode)
		res = stepic.encode(img,msg.encode())
		res.save(args.encode)
		print('Completed !')
else:
	parser.print_help()