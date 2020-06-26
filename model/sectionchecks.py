# -*- coding: cp1252 -*-

# class SectionChecks:
#
#     def __init__(self):
#         self.normalforce = 0
#     def section_checks(self):
#         pass

##Funktionen ber�knar och returnerar normalkapaciteten f�r en sektion med indata av sektionsobjekt samt materialobjekt
def normal_force_capacity(section, material):

    return section.area * material.f_y / material.gamma_m0


##Funktionen ber�knar och returnerar tv�rkraftskapaciteten i huvudriktningen f�r en sektion med indata av sektionsobjekt samt materialobjekt
def shear_capacity(section, material):
    pass


##Funktionen ber�knar och returnerar momentkapaciteten i huvudriktningen f�r en sektion med indata av sektionsobjekt samt materialobjekt
def moment_capacity(section, material):
    pass

