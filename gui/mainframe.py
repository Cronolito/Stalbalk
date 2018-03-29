# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx
from mainpanel import  MainPanel
from collections import OrderedDict
from sectiondialog import AddISectionDialog


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Stålbalk', size=(600, 600))

        self.panel = MainPanel(self)

        self.create_menus()

    def create_menus(self):
        """Innehåller menydatan"""
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
        dialog = AddISectionDialog(self)
        dialog.Show()

