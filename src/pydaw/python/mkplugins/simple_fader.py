# -*- coding: utf-8 -*-
"""
This file is part of the MusiKernel project, Copyright MusiKernel Team

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

"""

from libpydaw.pydaw_widgets import *
from libpydaw.translate import _

SFADER_VOL_SLIDER = 0

SFADER_PORT_MAP = {
    "Volume Slider": SFADER_VOL_SLIDER,
}

class sfader_plugin_ui(pydaw_abstract_plugin_ui):
    def __init__(self, a_val_callback, a_project,
                 a_folder, a_plugin_uid, a_track_name, a_stylesheet,
                 a_configure_callback, a_midi_learn_callback,
                 a_cc_map_callback):
        pydaw_abstract_plugin_ui.__init__(
            self, a_val_callback, a_project, a_plugin_uid, a_stylesheet,
            a_configure_callback, a_folder, a_midi_learn_callback,
            a_cc_map_callback)
        self._plugin_name = "SFADER"
        self.set_window_title(a_track_name)
        self.is_instrument = False
        #self.layout.setSizeConstraint(QLayout.SetFixedSize)
        self.volume_gridlayout = QGridLayout()
        self.layout.addLayout(self.volume_gridlayout)
        self.volume_slider = pydaw_slider_control(
            QtCore.Qt.Vertical, "Vol", SFADER_VOL_SLIDER,
            self.plugin_rel_callback, self.plugin_val_callback,
            -5000, 0, 0, KC_DECIMAL, self.port_dict)
        self.volume_slider.add_to_grid_layout(self.volume_gridlayout, 0)
        self.volume_slider.control.setMinimumHeight(300)
        self.volume_slider.control.setSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.widget.setFixedWidth(100)
        self.volume_slider.value_label.setMinimumWidth(91)
        self.widget.setWidgetResizable(True)
        self.open_plugin_file()
        self.set_midi_learn(SFADER_PORT_MAP)

    def plugin_rel_callback(self, a_val1=None, a_val2=None):
        self.save_plugin_file()

    def open_plugin_file(self):
        pydaw_abstract_plugin_ui.open_plugin_file(self)

    def save_plugin_file(self):
        pydaw_abstract_plugin_ui.save_plugin_file(self)

    def set_window_title(self, a_track_name):
        self.track_name = str(a_track_name)
        self.widget.setWindowTitle(
            "Fader - {}".format(self.track_name))

    def widget_close_event(self, a_event):
        a_event.accept()

    def raise_widget(self):
        pydaw_abstract_plugin_ui.raise_widget(self)

    def ui_message(self, a_name, a_value):
        pydaw_abstract_plugin_ui.ui_message(a_name, a_value)


