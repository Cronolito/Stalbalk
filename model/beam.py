# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2017-09-08.

from .sections import ISection
from .material import Material
from pubsub import pub


## Klassen  är huvudobjektet beskriver en balk och ska innehålla ett material samt minst en sektion och längddata
class Beam:

    def __init__(self, name):
        self.name = str(name)
        self.length = None
        self.sections = {}
        self.material = None

    ## Lägg till en sektion tll balken
    def add_section(self, name, top_flange_width, top_flange_thickness, web_thickness, web_height, bottom_flange_width, bottom_flange_thickness):
        # TODO: Sektionerna bör ha en längdmätning som bör vara keys
        self.sections[str(name)] = ISection(name, top_flange_width, top_flange_thickness, web_thickness, web_height, bottom_flange_width, bottom_flange_thickness)
        #Skicka meddelande om att ny sektion har lagts till
        section_names = list(self.sections.keys())
        pub.sendMessage('new_section_added', section_names=section_names)

    ## Metoden skapar ett material för balken
    def create_material(self, name, f_y, E):
        #TODO: bör material kanske ligga under plåtar istället och en balk kan bestå av fler plåtar?
        self.material = Material( name, f_y, E)
