# -*- coding: cp1252 -*-

# @author David Karlsson.
# @date 2018-03-29.

import wx
from collections import OrderedDict
from pubsub import pub


class AddISectionDialog(wx.Dialog):

    def __init__(self, parent, section_name, section_dimensions):
        wx.Dialog.__init__(self, parent, title = "Lägg till section")
        self.panel = wx.Panel(self)

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        #Lista med följande ordning: Böf, töf, hlv, tliv, buf, tuf
        if type(section_dimensions) != list:
            self.section_dimensions = [300, 10, 400, 8, 350, 12]
            self.section_name = 'New'
        else:
            self.section_dimensions = section_dimensions
            self.section_name = section_name


        self.text_input_widgets = []
        self.create_input_widgets()
        self.create_buttons_sizer()

        self.panel.SetSizer(self.main_sizer)
        self.panel.Fit()
        self.Fit()


    def create_input_widgets(self):
        #Skapa namnraden
        outher_box = wx.StaticBox(self, -1, 'Namn')
        sizer = wx.StaticBoxSizer(outher_box, wx.HORIZONTAL)
        text_input = wx.TextCtrl(self.panel, wx.ID_ANY, self.section_name, size=(270, -1))
        sizer.Add(text_input, 0, wx.ALL, 5)
        self.text_input_widgets.append(text_input)

        self.main_sizer.Add(sizer, 0, wx.ALL, 5)

        #skapa resterande indatafält
        widget_dict = OrderedDict([('Överfläns', ['Bredd [mm]', 'Tjocklek [mm]']),
                                   ('Liv', ['Höjd [mm]', 'Tjocklek [mm]']),
                                   ('Underfläns',['Bredd [mm]', 'Tjocklek [mm]'])])
        i = 0
        for key, labels in widget_dict.items():
            outher_box = wx.StaticBox(self, -1, key)
            sizer = wx.StaticBoxSizer(outher_box, wx.HORIZONTAL)

            for text in labels:
                text_on_panel = wx.StaticText(self.panel, 0, text)
                text_input = wx.TextCtrl(self.panel, wx.ID_ANY, str(self.section_dimensions[i]), size = (50,-1))
                sizer.Add(text_on_panel, 0, wx.ALL, 5)
                sizer.Add(text_input, 0, wx.ALL, 5)
                self.text_input_widgets.append(text_input)
                i+=1

            self.main_sizer.Add(sizer, 0, wx.ALL, 5)


    def create_buttons_sizer(self):
        ok_btn = wx.Button(self.panel, wx.ID_ANY, 'OK')
        cancel_btn = wx.Button(self.panel, wx.ID_ANY, 'Cancel')

        button_sizer = wx.BoxSizer()
        button_sizer.Add(ok_btn, 0, wx.ALL, 5)
        button_sizer.Add(cancel_btn, 0, wx.ALL, 5)

        self.main_sizer.Add(button_sizer, 0, wx.ALL | wx.CENTER, 5)

        self.Bind(wx.EVT_BUTTON, self.on_ok, ok_btn)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, cancel_btn)

    def on_ok(self, event):
        self.output = []
        for obj in self.text_input_widgets:
            self.output.append(obj.GetValue())

        pub.sendMessage('section.addI', section_data=self.output)
        self.Close()
        #Justerar vad showmodal ska returna.
        # self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.Close()
