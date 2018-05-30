# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx
from pubsub import pub
from math import ceil
from collections import OrderedDict


class MainPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(600, 350))

        # self.SetBackgroundColour('White')
        #Subscribes
        pub.subscribe(self.pub_on_set_choices, 'new_section_added')
        pub.subscribe(self.pub_on_get_section_data, 'section.data')
        self.chosen_section_parameters = {}

        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.widget_dict = {}
        self.init_section_ui()
        self.init_section_capacity_ui()

        self.SetSizer(self.main_sizer)
        self.Fit()

    def init_section_ui(self):
        #Inneh�ler sizer 21 och 22
        outher_box = wx.StaticBox(self, -1, 'Tv�rsnitt')
        sizer1 = wx.StaticBoxSizer(outher_box, wx.HORIZONTAL)
        # Ineh�ller listan och bild
        sizer21 = wx.BoxSizer(wx.VERTICAL)
        # Inneh�ller sektionsdata
        sizer22 = wx.FlexGridSizer(10, 2, 10, 10)

        #Provisorisk sektionslista innan man lagt till
        self.section_choice_widget = wx.Choice(self, style= wx.CB_SORT, choices=['Ingen sektion tillagd',], size=(120,-1))
        self.section_choice_widget.Bind(wx.EVT_CHOICE, self.on_section_choice)

        sizer21.Add(self.section_choice_widget, 0, wx.EXPAND | wx.ALL, 5)

        # key [visad text, v�rde, skalning, enhet]
        text_dict = OrderedDict([('area', ['Area:', 0, 1000000,' mm\u00B2']),
                                 ('web area', ['Livarea:', 0, 1000000, ' mm\u00B2']),
                                 ('moment of inertia', ['Tr�ghetsmoment:', 0, 1, ' m\u2074']),
                                 ('top bending stiffness', ['B�jmoment �vre:', 0, 1, ' m\u00B3']),
                                 ('bottom bending stiffness', ['B�jmoment undre:', 0, 1, ' m\u00B3']),
                                 ])

        for key, labels in text_dict.items():
            text_label = wx.StaticText(self, wx.ID_ANY, labels[0])
            text_widget = wx.StaticText(self, wx.ID_ANY, str(labels[1]*labels[2]) + labels[3])

            sizer22.AddMany([(text_label), (text_widget)])
            self.widget_dict[key] = [text_widget, labels[2], labels[3]]

        sizer1.Add(sizer21, 0, wx.ALL, 1)
        sizer1.Add(sizer22, 0, wx.ALL, 20)
        self.main_sizer.Add(sizer1, 0, wx.ALL, 10)

    def init_section_capacity_ui(self):
        outher_box = wx.StaticBox(self, -1, 'Tv�rsnittskapacitet')
        sizer1 = wx.StaticBoxSizer(outher_box, wx.HORIZONTAL)
        sizer2 = wx.FlexGridSizer(10, 2, 10, 10)

        text_dict = OrderedDict([('normal force', ['Normalkraft:', 0, 1, ' kN']),
                                 ('shear force', ['Tv�rkraft:', 0, 1, ' kN']),
                                 ('top bending moment y', ['�vre moment:', 0, 1, ' kNm']),
                                 ('bot bending moment y', ['Moment undre:', 0, 1, ' kNm']),
                                 ])

        for key, labels in text_dict.items():
            text_label = wx.StaticText(self, wx.ID_ANY, labels[0])
            text_widget = wx.StaticText(self, wx.ID_ANY, str(labels[1] * labels[2]) + labels[3])

            sizer2.AddMany([(text_label), (text_widget)])
            self.widget_dict[key] = [text_widget, labels[2], labels[3]]

        sizer1.Add(sizer2, 0, wx.ALL, 1)
        self.main_sizer.Add(sizer1, 0, wx.ALL, 10)

    ## metoden lyssnar efter vskapad sektion
    def pub_on_set_choices(self, section_names):
        self.section_choice_widget.SetItems(section_names)

    ## Metoden lyssnar efter sektionsdata fr�n modellen
    def pub_on_get_section_data(self, section_data):
        self.chosen_section_parameters = section_data


        # --------------Eventmetoder--------------------

    # Metoden uppdaterar UIt med nya v�rden d� ny sektion har valts
    def on_section_choice(self, event):
        chosen_section_name = self.section_choice_widget.GetString(self.section_choice_widget.GetSelection())
        #�beropar sektionsdata
        pub.sendMessage('section.get_data', section_name=chosen_section_name)

        for key, items in self.widget_dict.items():
            try:
                # Todo: Fixa avrundningen som blir fel och att den visar bra enhet
                items[0].SetLabel(str(ceil(self.chosen_section_parameters[key]*items[1]*100)/100)+items[2])
            except:
                print('Hittar inte v�rde')

        # self.Fit()