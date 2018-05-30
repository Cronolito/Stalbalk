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
        wx.Frame.__init__(self, None, title='St�lbalk', size=(600, 600))

        self.panel = MainPanel(self)

        self.create_menus()

        self.section_names_list = []

        pub.subscribe(self.pub_on_changed_section, 'new_section_added')


    def create_menus(self):
        """Inneh�ller menydatan"""
        menu_data = OrderedDict()
        menu_data['Arkiv'] = (('Avsluta', 'Avslutar programmet', self.on_exit),)
        menu_data['Profil'] = (('Importera sektion', 'Importerar standardprofiler fr�n bibliotek', self.on_import_section),
                               ('L�gg till I-profil', 'L�gger till en ny I-sektion', self.on_add_Isection),
                               ('Modifiera sektion', 'Modifiera en tillagd sektion', self.on_modify_section),)
        menu_data['Last'] = (('Importera tv�rkraft', 'Importerar tv�rkraftskurva fr�n textfil', self.on_import_shear),
                             ('Importera b�jmoment', 'Importerar momentkurva fr�n textfil', self.on_import_moment),)
        menu_data['Balk'] = (('Definiera balk', 'Defineriar tv�rsnitt l�ngs l�ngd', self.on_import_shear),)

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
            # Todo: Starta den sektionsdialogen som tillh�r r�tt sektion beroende p� vilken klass sektionen �r instans av
        dialog.Destroy()

    def on_import_section(self, event):
        pass

    def on_import_moment(self, event):
        pass

    def on_import_shear(self, event):
        pass

# ---------------------- Pub listerners---------------
    ## Metoden lyssnar p� n�r en sektion har lagts till och uppdaterar listan med sektionsnamn
    def pub_on_changed_section(self, section_names):
        self.section_names_list = section_names
