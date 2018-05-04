# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx

class MainPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(600, 350))

        # self.SetBackgroundColour('White')

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(self.main_sizer)

    def init_section_ui(self):
        outher_box = wx.StaticBox(self, -1, 'Tvärsnitt')
        sizer = wx.StaticBoxSizer(outher_box, wx.HORIZONTAL)

        # sample_list = 'Här ska jag ha in sektionerna men nstan behov av docview, annars får jag skicka tillbaka objektet'
        # combo_box = wx.ComboBox(self, wx.ID_ANY, 'Default', wx.DefaultPosition, (100, -1), sample_list, wx.CB_DROPDOWN

    def init_section_capacity_ui(self):
        pass

