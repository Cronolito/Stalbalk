# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx
from mainpanel import  MainPanel
from collections import OrderedDict
from sectiondialog import AddISectionDialog
import programfiles as pf


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='St�lbalk', size=(600, 600))

        self.panel = MainPanel(self)

        self.create_menus()

        self.beamObject = pf.beam.Beam('Balknamn')

    def create_menus(self):
        """Inneh�ller menydatan"""
        menu_data = OrderedDict()
        menu_data['File'] = (('Exit', 'Exits the program', self.on_exit),)
        menu_data['Sections'] = (('Add Section', 'Adds a section to the session', self.on_add_section), )

        #Skapa menubaren
        menu_bar = wx.MenuBar()
        for menu_label, menu_items in menu_data.iteritems():
            menu = wx.Menu()
            for label, status, event in menu_items:
                menu_item = menu.Append(-1, label, status)
                self.Bind(wx.EVT_MENU, event, menu_item)
            menu_bar.Append(menu, menu_label)
        self.SetMenuBar(menu_bar)



    #---------------------Eventfunktioner----------------------------------

    def on_exit(self, event):
        self.Close(True)


    def on_add_section(self, event):
        #h�t �r jag, skicka med och ta emot dimensioner. Skriv i sections.
        if not self.beamObject.sections:
            dialog = AddISectionDialog(self, None)

        else:
            section_dimensions = self.beamObject.sections['New'].get_dimensions()
            dialog = AddISectionDialog(self, section_dimensions)

        dialog.ShowModal()
        top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness = dialog.section_dimensions
        self.beamObject.add_section('New', top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness)
        dialog.Destroy()

        print 'Dimensions: {}'.format(self.beamObject.sections['New'].get_dimensions())
        print 'Area: {} mm2'.format(self.beamObject.sections['New'].area*1000*1000)
        print 'I: {} m4'.format(self.beamObject.sections['New'].moment_of_inertia)

