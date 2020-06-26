# -*- coding: cp1252 -*-

# class SectionChecks:
#
#     def __init__(self):
#         self.normalforce = 0
#     def section_checks(self):
#         pass

##Funktionen beräknar och returnerar normalkapaciteten för en sektion med indata av sektionsobjekt samt materialobjekt
def normal_force_capacity(section, material):

    return section.area * material.f_y / material.gamma_m0


##Funktionen beräknar och returnerar tvärkraftskapaciteten i huvudriktningen för en sektion med indata av sektionsobjekt samt materialobjekt
def shear_capacity(section, material):
    pass


##Funktionen beräknar och returnerar momentkapaciteten i huvudriktningen för en sektion med indata av sektionsobjekt samt materialobjekt
def moment_capacity(section, material):
    pass

