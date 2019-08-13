#!/usr/bin/env python3

from math import log

f0 = 440
a = 2**(1/12)

# http://www.cbmitapages.it/c64/sid1eng.htm
# https://codebase64.org/doku.php?id=base:how_to_calculate_your_own_sid_frequency_table
# https://csdb.dk/forums/?roomid=11&topicid=124823&firstpost=2

pal_const =  (256**3)/985248
ntsc_const = (256**3)/1022727

def reg_to_freq_pal(reg):
	return reg/pal_const

def freq_to_reg_pal(f):
	return int(f*pal_const+0.5)

def reg_to_freq_ntsc(reg):
	return reg/ntsv_const

def freq_to_reg_ntsc(f):
	return int(f*ntsc_const+0.5)

def note_to_freq(n):
	return f0*a**n

def freq_to_note(f):
	return log(f/f0, a)

if __name__=='__main__':
	print(hex(freq_to_reg_pal(440)))
