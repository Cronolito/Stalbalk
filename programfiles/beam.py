# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2017-09-08.

from .sections import ISection
from .material import Material

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

    ## Metoden skapar ett material f�r balken
    def create_material(self, name, f_y, E):
        #TODO: b�r material kanske ligga under pl�tar ist�llet och en balk kan best� av fler pl�tar?
        self.material = Material( name, f_y, E)


