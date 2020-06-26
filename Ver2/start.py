# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2020-06-26

from numpy import arange

##Mainobjektet
class Beam:

    def __init__(self):
        self.main_sections = {}
        self.segment_size = 0.1
        self.beam_definition = [] #[[0, L1, Lmax],[0name, L1name, Lmaxname]]

    def add_i_section(self, name, top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness):
        if not name in self.main_sections:
            self.main_sections[name] = [top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness]

    def generate_sections(self):
        if len (self.beam_definition) !=0:

            for x in arange(0, self.beam_definition[0][-1]+self.segment_size, self.segment_size):
                print(x)

