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
        pub.subscribe(self.pub_on_get_section, 'section.get_data')

    def pub_on_add_i_section(self, section_data):
        section_name, top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness = section_data
        self.model.add_section(section_name, top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness)

    def pub_on_get_section(self, section_name):
        self.model.get_section_data(section_name)
