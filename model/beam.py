# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2017-09-08.

from .sections import ISection
from .material import Material
from pubsub import pub


## Klassen  �r huvudobjektet beskriver en balk och ska inneh�lla ett material samt minst en sektion och l�ngddata
class Beam:

    def __init__(self, name):
        self.name = str(name)
        self.length = None
        self.sections = {}
        self.material = None

    ## L�gg till en sektion tll balken
    def add_section(self, name, top_flange_width, top_flange_thickness, web_thickness, web_height, bottom_flange_width, bottom_flange_thickness):
        # TODO: Sektionerna b�r ha en l�ngdm�tning som b�r vara keys
        self.sections[str(name)] = ISection(name, top_flange_width, top_flange_thickness, web_thickness, web_height, bottom_flange_width, bottom_flange_thickness)
        #Skicka meddelande om att ny sektion har lagts till
        section_names = list(self.sections.keys())
        pub.sendMessage('new_section_added', section_names=section_names)

    ## Metoden skapar ett material f�r balken
    def create_material(self, name, f_y, E):
        #TODO: b�r material kanske ligga under pl�tar ist�llet och en balk kan best� av fler pl�tar?
        self.material = Material( name, f_y, E)

    ## Metoden returnerat ett sektionsobjekt som har sektionsnamnet
    def get_section_data(self, section_name):
        #Skicka meddelande med sektionsdatan
        try:
            data = self.sections[section_name].get_section_data()
            pub.sendMessage('section.data', section_data=data)
        except:
            raise KeyError('No such section exists')
