# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx
from .mainpanel import  MainPanel
from collections import OrderedDict
from .sectiondialog import AddISectionDialog
import programfiles as pf


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Stålbalk', size=(600, 600))

        self.panel = MainPanel(self)

        self.create_menus()

        self.beamObject = pf.beam.Beam('Balknamn')

    def create_menus(self):
        """Innehåller menydatan"""
        menu_data = OrderedDict()
        menu_data['Arkiv'] = (('Avsluta', 'Avslutar programmet', self.on_exit),)
        menu_data['Profil'] = (('Importera sektion', 'Importerar standardprofiler från bibliotek', self.on_import_section),
                               ('Lägg till I-profil', 'Lägger till en ny I-sektion', self.on_add_Isection),
                               ('Modifiera sektion', 'Modifiera en tillagd sektion', self.on_modify_section),)
        menu_data['Last'] = (('Importera tvärkraft', 'Importerar tvärkraftskurva från textfil', self.on_import_shear),
                             ('Importera böjmoment', 'Importerar momentkurva från textfil', self.on_import_moment),)

        #Skapa menubaren
        menu_bar = wx.MenuBar()
        for menu_label, menu_items in menu_data.items():
            menu = wx.Menu()
            for label, status, event in menu_items:
                menu_item = menu.Append(-1, label, status)
                self.Bind(wx.EVT_MENU, event, menu_item)
            menu_bar.Append(menu, menu_label)
        self.SetMenuBar(menu_bar)



    #---------------------Eventfunktioner----------------------------------

    def on_exit(self, event):
        self.Close(True)


    def on_add_Isection(self, event):
        dialog = AddISectionDialog(self, None, 'ISektion')
        if dialog.ShowModal() == wx.ID_OK:
            section_name, top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness = dialog.output
            self.beamObject.add_section(section_name, top_flange_width, top_flange_thickness, web_height, web_thickness, bottom_flange_width, bottom_flange_thickness)
        dialog.Destroy()

        #provisorisk data
        print('Sections')
        for key in self.beamObject.sections.keys():
            print(key)
            print('Dimensions: {}'.format(self.beamObject.sections[key].get_dimensions()))
            print('Area: {} mm2'.format(self.beamObject.sections[key].area*1000*1000))
            print('I: {} m4'.format(self.beamObject.sections[key].moment_of_inertia))

    def on_modify_section(self, event):
        #Dialogen är en vallista där man väljer vilken dialog man kommer till
        # section_dimensions = self.beamObject.sections['New'].get_dimensions()
        # dialog = AddISectionDialog(self, section_dimensions, self.beamObject.sections)
        pass

    def on_import_section(self, event):
        pass

    def on_import_moment(self, event):
        pass

    def on_import_shear(self, event):
        pass
