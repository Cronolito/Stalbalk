# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

from math import sqrt
#Regler
"""
class NameConvention:

    def __init__(self, input):
        self.new_property = input

    def create_new(self, imp):

        använd inga get setters om det inte gör något innan.
        Tabs är spaces
        Kör nu enligt PEP8
   """


class BeamSection:

    def __init__(self, name):
        self.name = name
        self.area = None
        self.cog = None
        self.moment_of_inertia = None

## Klassen skapar en I-section. indata ges i mm men lagras i SI
class ISection(BeamSection):

    def __init__(self, name, top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness):
        BeamSection.__init__(self, name)
        #TODO: Lägg in så amn inte kan mata in 0 eller negativa data som indata
        self.top_flange_width = float(top_flange_width)/1000.
        self.top_flange_thickness = float(top_flange_thickness)/1000.
        self.web_thickness = float(web_thickness)/1000.
        self.web_height = float(web_height)/1000.
        self.bottom_flange_width = float(bottom_flange_width)/1000.
        self.bottom_flange_thickness = float(bottom_flange_thickness)/1000.

        self.top_bending_stiffness = None
        self.bottom_bending_stiffness = None
        self.beam_height = None
        #
        # self.top_section_class = None
        # self.web_section_class = None
        # self.bot_section_class = None
        #
        self.calculate_beam_properties()


    ## Metoden kallar på alla undermetoder
    def calculate_beam_properties(self):
        self.calculate_beam_heigth()
        self.calculate_area()
        self.calculate_center_of_gravity()
        self.calculate_moment_of_inertia()
        self.calculate_bending_stiffness()

    ## Metoden beräknar totala balkhöjden
    def calculate_beam_heigth(self):
        self.beam_height = self.top_flange_thickness + self.web_height + self.bottom_flange_thickness

    ## Metoden beräknar arean för tvärsnittet
    def calculate_area(self):
        self.area = self.top_flange_width*self.top_flange_thickness+self.web_height*self.web_thickness+\
                    self.bottom_flange_width*self.bottom_flange_thickness
        self.area_web = self.web_height * self.web_thickness

    ## Metoden beräknar tyngdpunkten för tvärsnittet med utgångspunkt från underkant
    def calculate_center_of_gravity(self):
        if not self.area == None:
            self.cog = (self.bottom_flange_width*self.bottom_flange_thickness**2/2. + self.web_height*self.web_thickness*
                    (self.web_height/2.+self.bottom_flange_thickness)+self.top_flange_width*self.top_flange_thickness*
                    (self.bottom_flange_thickness+self.web_height+self.top_flange_thickness/2.))/self.area

    ## Metoden beräknar tröghetsmomentet för tvärsnittet med utgångspunkt från underkant
    def calculate_moment_of_inertia(self):
        if not self.cog == None:
            A_tf = self.top_flange_thickness * self.top_flange_width
            A_w = self.web_thickness * self.web_height
            A_bf = self.bottom_flange_width * self.bottom_flange_thickness

            I_bf = A_bf * self.bottom_flange_thickness**2/12. + A_bf*(self.bottom_flange_thickness/2.-self.cog)**2
            I_w = A_w * self.web_height**2/12. + A_w * (self.bottom_flange_thickness +self.web_height/2.-self.cog)**2
            I_tf = A_tf * self.top_flange_thickness**2/12. + A_tf * (self.bottom_flange_thickness +self.web_height + self.top_flange_thickness/2.-self.cog)**2
            self.moment_of_inertia = I_bf + I_w + I_tf
        else:
            raise ValueError('Can not calculate I, no centre of gravity defined')

    ## Metoen beräknar böjstyvheterna för över och underfläns
    def calculate_bending_stiffness(self):
        if not self.cog == None or not self.moment_of_inertia == None or not self.beam_height == 0:
            self.top_bending_stiffness = self.moment_of_inertia/float(self.beam_height - self.cog)
            self.bottom_bending_stiffness = self.moment_of_inertia/float(self.cog)
        else:
            raise ValueError('Cannot calculate bending stiffness, parameters missing')

    ## Metoden beräknar balksnittets tvärsnittsklass med input av moment och normalkraft i SI-enheter
    def calculate_section_class(self, M, N, f_y):
        #TODO: Fixa denna metod
        epsilon = sqrt(235e6/f_y)

        #Liv
        # Bara moment
        if N == 0:
            c_t = self.web_height/float(self.web_thickness)

        #Överfläns

    ## Metodern returnerar sektionens dimensioner i mm
    def get_dimensions(self):
        return [self.top_flange_width*1000, self.top_flange_thickness*1000, self.web_height*1000, self.web_thickness*1000, self.bottom_flange_width*1000, self.bottom_flange_thickness*1000]

    ## Metoden returnerar sektionsdata som ett dictionary
    def get_section_data(self):
        section_data = {}
        section_data['area'] = self.area
        section_data['web area'] = self.area_web
        section_data['centre of gravity'] = self.cog
        section_data['moment of inertia'] = self.moment_of_inertia
        section_data['top bending stiffness'] = self.top_bending_stiffness
        section_data['bottom bending stiffness'] = self.bottom_bending_stiffness

        return section_data


