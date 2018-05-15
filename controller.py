# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

from pubsub import pub

import model
import view

class Controller:

    def __init__(self):
        self.model = model.Beam('Balknamn')
        self.view = view.MainFrame()
        self.view.Show()

        pub.subscribe(self.pub_on_add_i_section, 'section.addI')
        pub.subscribe(self.pub_on_get_section_names, 'get_section_names')

    def pub_on_add_i_section(self, section_data):
        section_name, top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness = section_data
        self.model.add_section(section_name, top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness)


        for key in self.model.sections.keys():
            print(key)
            print('Dimensions: {}'.format(self.model.sections[key].get_dimensions()))
            print('Area: {} mm2'.format(self.model.sections[key].area*1000*1000))
            print('I: {} m4'.format(self.model.sections[key].moment_of_inertia))

    def pub_on_get_section_names(self):
        self.model.get_section_names()
