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


##Funktionen beräknar och returnerar tvärkraftskapacitetn för en sektion med indata av sektionsobjekt samt materialobjekt
def shear_capacity(section, material):
    pass

def moment_capacity(sectiom, material):
    pass
