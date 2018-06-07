# -*- coding: cp1252 -*-


# @author David Karlsson.
# @date 2017-09-08.

class Material:

    def __init__(self, name, f_y, E):
        self.name = name
        self.f_y = f_y
        self.E = E
        self.gamma_m0 = 1.0

        #TODO: Fy ska vara funktion av t.
