#!/usr/bin/env python3

from math import log

f0 = 440
a = 2**(1/12)

def note_to_freq(n):
	return f0*a**n

def freq_to_note(f):
	return log(f/f0, a)

if __name__=='__main__':
	print(freq_to_note(440))
	print(freq_to_note(note_to_freq(2)))
