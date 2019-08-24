#!/usr/bin/env python3

from math import log, floor
import jinja2

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

a4 = 435.97705078124994
base = 2**(1/12)

names_sharp = ['a{}',  'a{}♯', 'b{}', 'c{}',  'c{}♯', 'd{}',
			   'd{}♯', 'e{}',  'f{}', 'f{}♯', 'g{}',  'g{}♯']
names_flat  = ['a{}',  'b{}♭', 'b{}', 'c{}',  'd{}♭', 'd{}',
			   'e{}♭', 'e{}',  'f{}', 'g{}♭', 'g{}',  'a♭{}']

# https://www.liveabout.com/pitch-notation-and-octave-naming-2701389
def index_to_name(i, sharp):
	octave = floor((i-3)/12)+5
	names = names_sharp if sharp else names_flat
	return names[i%12].format(octave)

lilynames_sharp = ['a', 'as', 'b', 'c', 'cs', 'd', 'ds', 'e','f', 'fs', 'g', 'gs']
lilynames_flat  = ['a', 'bf', 'b', 'c', 'df', 'd', 'ef', 'e','f', 'gf', 'g', 'af']

def index_to_lily(i, sharp):
	names = lilynames_sharp if sharp else lilynames_flat
	octave = floor((i-3)/12)+2
	if octave<0:
		octave = ','*-octave
	else:
		octave = "'"*octave
	return names[i%12]+octave

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
	return reg/ntsc_const

def freq_to_reg_ntsc(f):
	return int(f*ntsc_const+0.5)

def note_to_freq(n):
	return a4*base**n

def freq_to_note(f):
	return log(f/a4, base)

def render(env, template_name, **template_vars):
    template = env.get_template(template_name)
    return template.render(**template_vars)

names = ['a', 'a♯', 'b', 'c', 'c♯', 'd', 'd♯', 'e', 'f', 'f♯', 'g', 'g♯']

class Spectrum(object):
	def __init__(self):
		self.notes = [0]*12

	def add(self, n):
		self.notes[n%12] += 1

	def __str__(self):
		s = ""
		for i in range(0, 12):
			s += names[i].ljust(2)+" : "+str(self.notes[i])+"\n"
		return s

class Keys(object):
	def __init__(self):
		maj = [0, 2, 2, 1, 2, 2, 2]
		self.keys = {}
		for t in range(0, 12):
			s = []
			last = t
			for i in maj:
				s.append((last+i)%12)
				last += i
			self.keys[t] = s

	def notes_in(self, k):
		return [n for n in range(0, 12) if n in self.keys[k]]

	def notes_not_in(self, k):
		return [n for n in range(0, 12) if n not in self.keys[k]]

if __name__=='__main__':
	with open("test.ly", "w", encoding='utf-8') as of:
		s = Spectrum()

		v1 = ""
		for n in voice1():
			sid = note_to_sid(n)
			f = reg_to_freq_pal(sid)
			i = round(freq_to_note(f))
			s.add(i)
			v1 += index_to_lily(i, False)+"8 "
		v2 = ""
		for n in voice2():
			sid = note_to_sid(n)
			f = reg_to_freq_pal(sid)
			i = round(freq_to_note(f))
			s.add(i)
			v2 += index_to_lily(i, False)+"8 "

		keys = Keys()
		for k in range(0, 12):
			acc = 0
			for nkn in keys.notes_not_in(k):
				acc += s.notes[nkn]
			print(names[k].ljust(2)+" : "+str(acc))

		env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
		env.globals['voice1'] = v1
		env.globals['voice2'] = v2
		env.globals['key'] = r"\key f \minor"
		s = render(env, 'bd.ly')
		of.write(s)
