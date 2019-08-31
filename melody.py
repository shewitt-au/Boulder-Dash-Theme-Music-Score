#!/usr/bin/env python3

from math import log, floor

bd_sid_values = [
0xdc, 0x02, 0x0a, 0x03,  0x3a, 0x03, 0x6c, 0x03,  0xa0, 0x03, 0xd2, 0x03,  0x12, 0x04, 0x4c, 0x04,
0x92, 0x04, 0xd6, 0x04,  0x20, 0x05, 0x6e, 0x05,  0xb8, 0x05, 0x14, 0x06,  0x74, 0x06, 0xd8, 0x06,
0x40, 0x07, 0xa4, 0x07,  0x24, 0x08, 0x98, 0x08,  0x24, 0x09, 0xac, 0x09,  0x40, 0x0a, 0xdc, 0x0a,
0x70, 0x0b, 0x28, 0x0c,  0xe8, 0x0c, 0xb0, 0x0d,  0x80, 0x0e, 0x48, 0x0f,  0x48, 0x10, 0x30, 0x11,
0x48, 0x12, 0x58, 0x13,  0x80, 0x14, 0xb8, 0x15,  0xe0, 0x16, 0x50, 0x18,  0xd0, 0x19, 0x60, 0x1b,
0x00, 0x1d, 0x90, 0x1e,  0x90, 0x20, 0x60, 0x22,  0x90, 0x24, 0xb0, 0x26,  0x00, 0x29, 0x70, 0x2b,
0xc0, 0x2d]

def chunks():
	i = iter(bd_sid_values)
	try:
		while True:
			yield next(i)+next(i)*256
	except StopIteration:
		return

def note_to_sid(n):
	return bd_sid_values[n*2]+bd_sid_values[n*2+1]*256

names_sharp=['a{}','a{}♯','b{}','c{}','c{}♯','d{}','d{}♯','e{}','f{}','f{}♯','g{}','g{}♯']
names_flat=['a{}','b{}♭','b{}','c{}','d{}♭','d{}','e{}♭','e{}','f{}','g{}♭','g{}','a♭{}']

def index_to_name(i, sharp):
	octave = floor((i-3)/12)+5
	names = names_sharp if sharp else names_flat
	return names[i%12].format(octave)

bd_music = [
0x16, 0x22, 0x1d, 0x26,  0x22, 0x29, 0x25, 0x2e,  0x14, 0x24, 0x1f, 0x27,  0x20, 0x29, 0x27, 0x30,
0x12, 0x2a, 0x12, 0x2c,  0x1e, 0x2e, 0x12, 0x31,  0x20, 0x2c, 0x33, 0x37,  0x21, 0x2d, 0x31, 0x35,
0x16, 0x22, 0x16, 0x2e,  0x16, 0x1d, 0x16, 0x24,  0x14, 0x20, 0x14, 0x30,  0x14, 0x24, 0x14, 0x20,
0x16, 0x22, 0x16, 0x2e,  0x16, 0x1d, 0x16, 0x24,  0x1e, 0x2a, 0x1e, 0x3a,  0x1e, 0x2e, 0x1e, 0x2a,
0x14, 0x20, 0x14, 0x2c,  0x14, 0x1b, 0x14, 0x22,  0x1c, 0x28, 0x1c, 0x38,  0x1c, 0x2c, 0x1c, 0x28,
0x11, 0x1d, 0x29, 0x2d,  0x11, 0x1f, 0x29, 0x2e,  0x0f, 0x27, 0x0f, 0x27,  0x16, 0x33, 0x16, 0x27,
0x16, 0x2e, 0x16, 0x2e,  0x16, 0x2e, 0x16, 0x2e,  0x22, 0x2e, 0x22, 0x2e,  0x16, 0x2e, 0x16, 0x2e,
0x14, 0x2e, 0x14, 0x2e,  0x14, 0x2e, 0x14, 0x2e,  0x20, 0x2e, 0x20, 0x2e,  0x14, 0x2e, 0x14, 0x2e,
0x16, 0x2e, 0x32, 0x2e,  0x16, 0x2e, 0x33, 0x2e,  0x22, 0x2e, 0x32, 0x2e,  0x16, 0x2e, 0x33, 0x2e,
0x14, 0x2e, 0x32, 0x2e,  0x14, 0x2e, 0x33, 0x2e,  0x20, 0x2c, 0x30, 0x2c,  0x14, 0x2c, 0x31, 0x2c,
0x16, 0x2e, 0x16, 0x3a,  0x16, 0x2e, 0x35, 0x38,  0x22, 0x2e, 0x22, 0x37,  0x16, 0x2e, 0x31, 0x35,
0x14, 0x2c, 0x14, 0x38,  0x14, 0x2c, 0x14, 0x38,  0x20, 0x2c, 0x20, 0x33,  0x14, 0x2c, 0x14, 0x38,
0x16, 0x2e, 0x32, 0x2e,  0x16, 0x2e, 0x33, 0x2e,  0x22, 0x2e, 0x32, 0x2e,  0x16, 0x2e, 0x33, 0x2e,
0x14, 0x2e, 0x32, 0x2e,  0x14, 0x2e, 0x33, 0x2e,  0x20, 0x2c, 0x30, 0x2c,  0x14, 0x2c, 0x31, 0x2c,
0x2e, 0x32, 0x29, 0x2e,  0x26, 0x29, 0x22, 0x26,  0x2c, 0x30, 0x27, 0x2c,  0x24, 0x27, 0x14, 0x20,
0x35, 0x32, 0x32, 0x2e,  0x2e, 0x29, 0x29, 0x26,  0x27, 0x30, 0x24, 0x2c,  0x20, 0x27, 0x14, 0x20]

def voice1():
	i = iter(bd_music)
	try:
		while True:
			next(i)
			yield next(i)-10
	except StopIteration:
		return

def voice2():
	i = iter(bd_music)
	try:
		while True:
			yield next(i)-10
			next(i)
	except StopIteration:
		return

pal_const =  (256**3)/985248
ntsc_const = (256**3)/1022727
a4 = 435.97705078124994
base = 2**(1/12)

def reg_to_freq_pal(reg):
	return reg/pal_const

def reg_to_freq_ntsc(reg):
	return reg/ntsc_const

def freq_to_note(f):
	return log(f/a4, base)

v1 = ""
for n in voice1():
	sid = note_to_sid(n)
	f = reg_to_freq_pal(sid)
	i = round(freq_to_note(f))
	v1 += index_to_name(i, True)+" "

v2 = ""
for n in voice2():
	sid = note_to_sid(n)
	f = reg_to_freq_pal(sid)
	i = round(freq_to_note(f))
	v2 += index_to_name(i, True)+" "

print("Voice 1")
print("-------")
print(v1)
print()
print("Voice 2")
print("-------")
print(v2)
