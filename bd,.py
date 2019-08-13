#!/usr/bin/env python3

from math import log

f0 = 440
a = 2**(1/12)

# http://www.cbmitapages.it/c64/sid1eng.htm
# https://codebase64.org/doku.php?id=base:how_to_calculate_your_own_sid_frequency_table

def reg_to_freq_pal(reg):
	return (reg*985250)/16777216

def freq_to_reg_pal(f):
	return int((f*16777216)/985250)

def reg_to_freq_ntsc(reg):
	return (reg*1022730)/16777216

def freq_to_reg_ntsc(f):
	return int((f*16777216)/1022730)

def note_to_freq(n):
	return f0*a**n

def freq_to_note(f):
	return log(f/f0, a)

if __name__=='__main__':
	print(hex(freq_to_reg_pal(440)))
	print(hex(freq_to_reg_ntsc(440)))
