# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx
from pubsub import pub
from collections import OrderedDict


class MainPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(600, 350))

        # self.SetBackgroundColour('White')
        #Subscribes
        pub.subscribe(self.pub_on_set_choices, 'new_section_added')

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.init_section_ui()

        self.SetSizer(self.main_sizer)
        self.Fit()

    def init_section_ui(self):
        #Innehåler sizer 21 och 22
        outher_box = wx.StaticBox(self, -1, 'Tvärsnitt')
        sizer1 = wx.StaticBoxSizer(outher_box, wx.HORIZONTAL)
        # Inehåller listan och bild
        sizer21 = wx.BoxSizer(wx.VERTICAL)
        # Innehåller sektionsdata
        sizer22 = wx.FlexGridSizer(3, 2, 10, 10)

        #Provisorisk sektionslista innan man lagt till
        self.section_choice_widget = wx.Choice(self, style= wx.CB_SORT, choices=['Ingen sektion tillagd',], size=(120,-1))
        self.section_choice_widget.Bind(wx.EVT_CHOICE, self.on_section_choice)

        sizer21.Add(self.section_choice_widget, 0, wx.EXPAND | wx.ALL, 5)

        text_dict = OrderedDict([('Area:', ['0', 'mm\u00B2']),
                                 ('Tröghetsmoment:', ['0', 'mm\u2074']),
                                 ])
        self.widget_dict = {}
        for key, labels in text_dict.items():
            text_label = wx.StaticText(self, wx.ID_ANY, key)
            value = wx.StaticText(self, wx.ID_ANY, labels[0] + ' ' + labels[1])

            sizer22.AddMany([(text_label), (value)])
            self.widget_dict[key] = value

        sizer1.Add(sizer21, 0, wx.ALL, 1)
        sizer1.Add(sizer22, 0, wx.ALL, 20)
        self.main_sizer.Add(sizer1, 0, wx.ALL, 10)

    def init_section_capacity_ui(self):
        pass

    def pub_on_set_choices(self, section_names):
        self.section_choice_widget.SetItems(section_names)


    # --------------Eventmetoder--------------------

    # Metoden uppdaterar UIt med nya värden då ny sektion har valts
    def on_section_choice(self, event):
        chosen_section_name = self.section_choice_widget.GetString(self.section_choice_widget.GetSelection())
        print(chosen_section_name+' är vald i ui')
        # Todo: Hämta nu all data och uppdatera uit
        import random
        from math import ceil
        for item in self.widget_dict.values():
            item.SetLabel(str(ceil(random.random()*100)/100))
