#!/usr/bin/env python3

from math import floor
import jinja2

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

def render(env, template_name, **template_vars):
    template = env.get_template(template_name)
    return template.render(**template_vars)

if __name__=='__main__':
    with open("notes.ly", "w", encoding='utf-8') as of:
        notes = ""
        left_hand = ""
        note = -40
        for bd_val in range(0x0a, 0x3b):
            notes += "{}^\"${:02x}\" ".format(index_to_lily(note, True), bd_val)
            note += 1

        env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
        env.globals['notes'] = notes
        s = render(env, 'notes_template.ly')
        of.write(s)
