# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx
from pubsub import pub

from .mainpanel import  MainPanel
from collections import OrderedDict
from .sectiondialog import AddISectionDialog
from .editsectiondialog import EditSectionDialog
import model as pf


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Stålbalk', size=(600, 600))

        self.panel = MainPanel(self)

        self.create_menus()

        self.section_names_list = []

        pub.subscribe(self.pub_on_changed_section, 'new_section_added')


    def create_menus(self):
        """Innehåller menydatan"""
        menu_data = OrderedDict()
        menu_data['Arkiv'] = (('Avsluta', 'Avslutar programmet', self.on_exit),)
        menu_data['Profil'] = (('Importera sektion', 'Importerar standardprofiler från bibliotek', self.on_import_section),
                               ('Lägg till I-profil', 'Lägger till en ny I-sektion', self.on_add_Isection),
                               ('Modifiera sektion', 'Modifiera en tillagd sektion', self.on_modify_section),)
        menu_data['Last'] = (('Importera tvärkraft', 'Importerar tvärkraftskurva från textfil', self.on_import_shear),
                             ('Importera böjmoment', 'Importerar momentkurva från textfil', self.on_import_moment),)
        menu_data['Balk'] = (('Definiera balk', 'Defineriar tvärsnitt längs längd', self.on_import_shear),)

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
        dialog = AddISectionDialog(self, None, 'I-Sektion')
        dialog.ShowModal()
        dialog.Destroy()

    def on_modify_section(self, event):
        dialog = EditSectionDialog(self, self.section_names_list)
        if dialog.ShowModal():
            print('Vald sektion = '+dialog.chosen_section_name)
            # Todo: Starta den sektionsdialogen som tillhör rätt sektion beroende på vilken klass sektionen är instans av
        dialog.Destroy()

    def on_import_section(self, event):
        pass

    def on_import_moment(self, event):
        pass

    def on_import_shear(self, event):
        pass

# ---------------------- Pub listerners---------------
    ## Metoden lyssnar på när en sektion har lagts till och uppdaterar listan med sektionsnamn
    def pub_on_changed_section(self, section_names):
        self.section_names_list = section_names
