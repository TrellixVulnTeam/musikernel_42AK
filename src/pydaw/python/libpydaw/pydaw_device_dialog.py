#!/usr/bin/env python3

"""
This file is part of the MusiKernel project, Copyright MusiKernel Team

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

import os
import sys
import time
import ctypes

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

try:
    from libpydaw import pydaw_util, portaudio, portmidi
    from libpydaw.translate import _
except ImportError:
    import pydaw_util, portaudio, portmidi
    from translate import _

f_device_tooltip = _(
"""
Normal:  Run the audio engine without elevated privileges.  This generally
works well enough, but may require higher latency settings.
(YOU SHOULD PROBABLY USE THIS IF YOU ARE USING THE LIVE DVD/USB OR HAVE
SELINUX ENABLED, THE ELEVATED OPTIONS MAY NOT WORK DUE TO THE
SECURITY CONFIGURATION)

Elevated:  Run the audio engine with elevated privilege, this gives the
best possible latency, but if your desktop uses GTK+ it may refuse to run it.
(USE THIS OPTION IF POSSIBLE)

Elevated(sandbox):  Same as "Elevated", but works around GTK+'s decision
to prevent executing code with elevated rights by using a helper program
to launch the engine. (USE THIS OPTION IF POSSIBLE)

Debug:  Run an unoptimized binary with debug symbols and create a
core dump on crashing. This is useful for diagnosing the cause of a crash,
but consumes much more CPU and RAM, and is not recommended for normal use
unless the audio engine is crashing on your platform.

OPTIONS BELOW ARE DEVELOPER OPTIONS THAT NORMAL USERS SHOULD NEVER USE

GDB:  Open in the GDB debugger with no audio or external MIDI to allow setting
      breakpoints and pausing execution.

Valgrind:  Open in Valgrind, with no audio or external MIDI.
           VERY SLOW unless worker threads is set to 1!!!

GUI Only:  Run the UI only with no audio engine

No Audio:  No audio or MIDI, mostly useful for attaching an external debugger.
""")

THREADS_TOOLTIP = _(
"""This sets the number of worker threads for processing
plugins and effects.

Setting to 1 can result in the best latency, but
may (or may not) provide enough CPU power depending
on your CPU's single-threaded performance.  Also,
projects with complex audio routing may perform
better with fewer threads.

It is recommended that you not more than one thread
per CPU core. (Intel hyperthreading should NOT be
considered additional cores).

Auto attempts to pick a sane number of worker threads
automatically based on your CPU.

If you're not sure how to use this setting, you should
leave it on 'Auto'.

It is also recommended that you leave one or more
cores unused to power the UI and operating system,
for example:

dual-core:  1 worker thread
quad-core:  1 - 3 worker threads
""")

HUGEPAGES_TOOLTIP = _(
"""HugePages can improve memory/cache performance (sometimes significantly),
but you must allocate system memory for it that can only be used for HugePages.

It is recommended that you allocate at least 1GB of HugePages, and that you
leave AT LEAST 2GB of non-HugePage memory for other processes.  (if you use
other memory intensive applications that are not HugePage-enabled, you may
need to leave more than 2GB)

To allocate HugePages, run this command to see your HugePage size:

grep -i hugepage /proc/meminfo

Then add a line like this to the end of /etc/sysctl.conf and reboot:

# 1024 * 2MB HugePages = 2GB of HugePages
vm.nr_hugepages=1024

Some older CPUs and kernels don't support or have buggy support for HugePages,
disable this if it causes performance problems on your configuration.
"""
)

DEVICE_TOOLTIP = _("""Select your audio interface from this list.

If using JACK, the interface will be called the name of the JACK
virtual device, like "system" or similar.

Unless you are using Firewire (for which JACK is the only choice on Linux),
it is recommended that you stop the JACK server and select your
device directly from this list for best performance, stability and latency.
""")

class pydaw_device_dialog:
    def __init__(self, a_is_running=False):
        self.is_running = a_is_running
        self.device_name = None
        self.sample_rates = ["44100", "48000", "88200", "96000", "192000"]
        self.buffer_sizes = ["32", "64", "128", "256", "512", "1024", "2048"]

    def open_devices(self):
        f_portaudio_so_path = "libportaudio.so"
        ctypes.cdll.LoadLibrary(f_portaudio_so_path)
        self.pyaudio = ctypes.CDLL(f_portaudio_so_path)
        self.pyaudio.Pa_GetDeviceInfo.restype = ctypes.POINTER(
            portaudio.PaDeviceInfo)
        self.pyaudio.Pa_GetDeviceInfo.argstype = [ctypes.c_int]
        self.pyaudio.Pa_GetHostApiInfo.restype = ctypes.POINTER(
            portaudio.PaHostApiInfo)
        self.pyaudio.Pa_GetHostApiInfo.argstype = [ctypes.c_int]
        self.pyaudio.Pa_IsFormatSupported.argstype = [
            ctypes.POINTER(portaudio.PaStreamParameters),
            ctypes.POINTER(portaudio.PaStreamParameters), ctypes.c_double]
        self.pyaudio.Pa_Initialize()

        f_pm_dll = "libportmidi-0.dll" if "cygwin" in sys.platform \
            else "libportmidi.so"

        ctypes.cdll.LoadLibrary(f_pm_dll)
        self.pypm = ctypes.CDLL(f_pm_dll)
        self.pypm.Pm_GetDeviceInfo.restype = ctypes.POINTER(
            portmidi.PmDeviceInfo)
        self.pypm.Pm_Initialize()

    def close_devices(self):
        self.pyaudio.Pa_Terminate()
        self.pypm.Pm_Terminate()

    def check_device(self):
        if not pydaw_util.global_device_val_dict:
            self.show_device_dialog(
                _("No device configuration found"), a_exit_on_cancel=True)
            return
        elif not "name" in pydaw_util.global_device_val_dict:
            self.show_device_dialog(
                _("Invalid device configuration"), a_exit_on_cancel=True)
            return

        f_device_str = pydaw_util.global_device_val_dict["name"]

        self.open_devices()

        f_count = self.pyaudio.Pa_GetDeviceCount()

        f_audio_device_names = []

        for i in range(f_count):
            f_dev = self.pyaudio.Pa_GetDeviceInfo(i)
            f_dev_name = f_dev.contents.name.decode("utf-8")
            f_audio_device_names.append(f_dev_name)
            if f_device_str == f_dev_name:
                break

        self.close_devices()

        if not f_device_str in f_audio_device_names:
            print("{} not in {}".format(f_device_str, f_audio_device_names))
            pydaw_util.global_device_val_dict.pop("name")
            if "(hw:" in f_device_str:
                f_device_arr = f_device_str.split("(hw:")
                f_device_name = f_device_arr[0]
                f_device_num = f_device_arr[1].split(",", 1)[1]
                for f_device in f_audio_device_names:
                    if f_device.startswith(f_device_name) and \
                    f_device.endswith(f_device_num):
                        print(
                            _("It appears that the system switched up the "
                            "ALSA hw:X number, fixing it all sneaky-like "
                            "in the background.  (grumble, grumble...)"))
                        print(f_device)
                        pydaw_util.global_device_val_dict["name"] = f_device
                        f_file = open(
                            pydaw_util.global_pydaw_device_config, "w")
                        for k, v in pydaw_util.global_device_val_dict.items():
                            f_file.write("{}|{}\n".format(k, v))
                        f_file.write("\\")
                        f_file.close()
                        return
                self.show_device_dialog(
                    _("Device not found: {}").format(f_device_str),
                    a_exit_on_cancel=True)
            else:
                self.show_device_dialog(
                    _("Device not found: {}").format(f_device_str),
                    a_exit_on_cancel=True)


    def show_device_dialog(self, a_msg=None, a_exit_on_cancel=False):
        self.dialog_result = False
        self.open_devices()
        if self.is_running:
            f_window = QDialog()
        else:
            f_window = QWidget()
            f_window.setObjectName("plugin_ui")

        def f_close_event(a_self=None, a_event=None):
            self.close_devices()
            if a_exit_on_cancel and not self.dialog_result:
                exit(9876)

        f_window.closeEvent = f_close_event
        f_window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        f_window.setStyleSheet(pydaw_util.global_stylesheet)
        f_window.setWindowTitle(_("Hardware Settings..."))
        f_main_layout = QVBoxLayout(f_window)
        f_tab_widget = QTabWidget()
        f_main_layout.addWidget(f_tab_widget)

        f_audio_out_tab = QWidget()
        f_tab_widget.addTab(f_audio_out_tab, _("Audio Out"))
        f_window_layout = QGridLayout(f_audio_out_tab)

        f_audio_in_tab = QWidget()
        f_tab_widget.addTab(f_audio_in_tab, _("Audio In"))
        f_audio_in_layout = QGridLayout(f_audio_in_tab)

        f_midi_in_tab = QTabWidget()
        f_tab_widget.addTab(f_midi_in_tab, _("MIDI In"))
        f_midi_in_layout = QVBoxLayout(f_midi_in_tab)

        f_window_layout.addWidget(QLabel(_("Audio Device:")), 0, 0)
        f_device_name_combobox = QComboBox()
        f_device_name_combobox.setToolTip(DEVICE_TOOLTIP)
        f_device_name_combobox.setMinimumWidth(390)
        f_window_layout.addWidget(f_device_name_combobox, 0, 1)
        f_window_layout.addWidget(QLabel(_("Sample Rate:")), 1, 0)
        f_samplerate_combobox = QComboBox()
        f_samplerate_combobox.addItems(self.sample_rates)
        f_window_layout.addWidget(f_samplerate_combobox, 1, 1)
        f_buffer_size_combobox = QComboBox()
        f_buffer_size_combobox.addItems(self.buffer_sizes)
        f_buffer_size_combobox.setCurrentIndex(4)
        f_window_layout.addWidget(QLabel(_("Buffer Size:")), 2, 0)
        f_window_layout.addWidget(f_buffer_size_combobox, 2, 1)
        f_latency_label = QLabel("")
        f_window_layout.addWidget(f_latency_label, 2, 2)
        f_window_layout.addWidget(QLabel(_("Worker Threads:")), 3, 0)
        f_worker_threads_combobox = QComboBox()
        f_worker_threads_combobox.addItems(
            [_("Auto")] + [str(x) for x in range(1, 9)])
        f_worker_threads_combobox.setToolTip(THREADS_TOOLTIP)
        f_window_layout.addWidget(f_worker_threads_combobox, 3, 1)
        f_window_layout.addWidget(QLabel(_("Audio Engine")), 4, 0)
        f_audio_engine_combobox = QComboBox()
        f_audio_engine_combobox.addItems(
            [_("Normal"), _("Elevated"), _("Elevated(sandbox)"),
             _("Debug"), _("GDB"), _("Valgrind"),
             _("GUI Only"), _("No Audio")])
        f_audio_engine_combobox.setToolTip(f_device_tooltip)
        f_window_layout.addWidget(f_audio_engine_combobox, 4, 1)
        f_thread_affinity_checkbox = QCheckBox(
            _("Lock worker threads to own core?"))
        f_thread_affinity_checkbox.setToolTip(
            _("This may give better performance with fewer "
            "Xruns at low latency, "
            "but may perform badly\non certain configurations.  "
            "The audio engine setting must "
            "be set to 'Elevated' or "
            "'Elevated(Sandbox)', otherwise this setting has no effect."))
        f_window_layout.addWidget(f_thread_affinity_checkbox, 5, 1)

        f_governor_checkbox = QCheckBox(
            _("Force CPU governor to performance mode "
                "when MusiKernel is running?"))
        f_governor_checkbox.setToolTip(
            _("This forces the CPU to use more aggressive "
            "clockspeeds when MusiKernel is "
            "running, and reverts back to 'On Demand'\n"
            "when MusiKernel is closed.  Use this for best "
            "performance if possible.\n\n"
            "The audio engine setting must be set to "
            "'Elevated' or 'Elevated(Sandbox)', "
            "otherwise this setting has "
            "no effect.\n"
            "Also, support for cpufreq must be compiled in, "
            "which requires different dependencies in each distro, "
            "currently\n"
            "it's only default for Ubuntu.  However, you can make this "
            "setting in other distros using their default tools\nfor "
            "changing the CPU governor, such as the 'cpupower' command."
            "\n\n"
            "IMPORTANT:  Enabling this usually crashes the "
            "audio engine when run "
            "from within Virtualbox or on "
            "systems with\n"
            "certain security configurations.  Disable this if the "
            "engine crashes on startup."))
        f_window_layout.addWidget(f_governor_checkbox, 6, 1)
        f_hugepages_checkbox = QCheckBox(
            _("Use HugePages? (You must configure HugePages on your "
            "system first)"))
        f_hugepages_checkbox.setToolTip(_(HUGEPAGES_TOOLTIP))
        f_window_layout.addWidget(f_hugepages_checkbox, 7, 1)

        f_ok_cancel_layout = QHBoxLayout()
        f_main_layout.addLayout(f_ok_cancel_layout)
        f_ok_button = QPushButton(_("OK"))
        f_ok_cancel_layout.addWidget(f_ok_button)
        f_cancel_button = QPushButton(_("Cancel"))
        f_ok_cancel_layout.addWidget(f_cancel_button)

        #f_count = self.pyaudio.Pa_GetHostApiCount()

        f_count = self.pyaudio.Pa_GetDeviceCount()
        print("f_count == {}".format(f_count))

        f_result_dict = {}
        f_name_to_index = {}
        f_audio_device_names = []

        for i in range(f_count):
            f_dev = self.pyaudio.Pa_GetDeviceInfo(i)
            print("\nDevice Index: {}".format(i))
            f_dev_name = f_dev.contents.name.decode("utf-8")
            print("Name : {}".format(f_dev_name))
            print("maxInputChannels : {}".format(
                f_dev.contents.maxInputChannels))
            print("maxOutputChannels : {}".format(
                f_dev.contents.maxOutputChannels))
            print()
            f_name_to_index[f_dev_name] = i
            f_result_dict[f_dev_name] = f_dev.contents
            f_audio_device_names.append(f_dev_name)

        print("\n")

        f_audio_in_layout.addWidget(QLabel(_("Input Count")), 0, 0)
        f_audio_in_spinbox = QSpinBox()
        f_audio_in_spinbox.setRange(0, 0)
        f_audio_in_layout.addWidget(f_audio_in_spinbox, 0, 1)

        f_audio_in_layout.addItem(
            QSpacerItem(
                1, 1, QSizePolicy.Expanding,
                QSizePolicy.Expanding), 200, 0)

        self.midi_in_checkboxes = {}

        for loop in range(self.pypm.Pm_CountDevices()):
            f_midi_device = self.pypm.Pm_GetDeviceInfo(loop)
            f_midi_device_name = f_midi_device.contents.name.decode("utf-8")
            print("DeviceID: {} Name: '{}' Input?: {} "
                "Output?: {} Opened: {} ".format(
                loop, f_midi_device_name, f_midi_device.contents.input,
                f_midi_device.contents.output, f_midi_device.contents.opened))
            if f_midi_device.contents.input == 1:
                f_checkbox = QCheckBox(f_midi_device_name)
                if f_midi_device_name in pydaw_util.MIDI_IN_DEVICES:
                    f_checkbox.setChecked(True)
                self.midi_in_checkboxes[f_midi_device_name] = f_checkbox

        for f_cbox in sorted(
        self.midi_in_checkboxes, key=lambda x: x.lower()):
            f_midi_in_layout.addWidget(self.midi_in_checkboxes[f_cbox])

        f_midi_in_layout.addItem(
            QSpacerItem(1, 1, vPolicy=QSizePolicy.Expanding))

        def latency_changed(a_self=None, a_val=None):
            f_sample_rate = float(str(f_samplerate_combobox.currentText()))
            f_buffer_size = float(str(f_buffer_size_combobox.currentText()))
            f_latency = (f_buffer_size / f_sample_rate) * 1000.0
            f_latency_label.setText("{} ms".format(round(f_latency, 1)))

        f_samplerate_combobox.currentIndexChanged.connect(latency_changed)
        f_buffer_size_combobox.currentIndexChanged.connect(latency_changed)

        def combobox_changed(a_self=None, a_val=None):
            self.device_name = str(f_device_name_combobox.currentText())
            f_samplerate = str(
                int(f_result_dict[self.device_name].defaultSampleRate))
            if f_samplerate in self.sample_rates:
                f_samplerate_combobox.setCurrentIndex(
                    f_samplerate_combobox.findText(f_samplerate))
            f_in_count = f_result_dict[self.device_name].maxInputChannels
            f_in_count = pydaw_util.pydaw_clip_value(f_in_count, 0, 128)
            f_audio_in_spinbox.setMaximum(f_in_count)

        def on_ok(a_self=None):
            f_buffer_size = int(str(f_buffer_size_combobox.currentText()))
            f_samplerate = int(str(f_samplerate_combobox.currentText()))
            f_worker_threads = f_worker_threads_combobox.currentIndex()
            f_midi_in_devices = sorted(str(k)
                for k, v in self.midi_in_checkboxes.items() if v.isChecked())
            if len(f_midi_in_devices) >= 8:
                QMessageBox.warning(
                    f_window, _("Error"),
                    _("Using more than 8 MIDI devices is not supported, "
                    "please de-select some devices"))
                return
            f_audio_engine = f_audio_engine_combobox.currentIndex()
            f_thread_affinity = 1 if f_thread_affinity_checkbox.isChecked() \
                else 0
            f_performance = 1 if f_governor_checkbox.isChecked() else 0
            f_hugepages = 1 if f_hugepages_checkbox.isChecked() else 0
            f_audio_inputs = f_audio_in_spinbox.value()
            try:
                #This doesn't work if the device is open already,
                #so skip the test, and if it fails the
                #user will be prompted again next time MusiKernel starts
                if f_audio_engine != 7 or \
                not self.is_running or \
                "name" not in pydaw_util.global_device_val_dict or \
                pydaw_util.global_device_val_dict["name"] != self.device_name:
                    f_output = portaudio.PaStreamParameters(
                        f_name_to_index[self.device_name],
                        2, portaudio.paInt16,
                        float(f_buffer_size)/float(f_samplerate), None)
                    f_supported = self.pyaudio.Pa_IsFormatSupported(
                        0, ctypes.byref(f_output), f_samplerate)
                    if not f_supported:
                        raise Exception()
                f_file = open(pydaw_util.global_pydaw_device_config, "w")
                f_file.write("name|{}\n".format(self.device_name))
                f_file.write("bufferSize|{}\n".format(f_buffer_size))
                f_file.write("sampleRate|{}\n".format(f_samplerate))
                f_file.write("audioEngine|{}\n".format(f_audio_engine))
                f_file.write("threads|{}\n".format(f_worker_threads))
                f_file.write("threadAffinity|{}\n".format(f_thread_affinity))
                f_file.write("hugePages|{}\n".format(f_hugepages))
                f_file.write("performance|{}\n".format(f_performance))
                f_file.write("audioInputs|{}\n".format(f_audio_inputs))
                for f_midi_in_device in f_midi_in_devices:
                    f_file.write("midiInDevice|{}\n".format(f_midi_in_device))

                f_file.write("\\")
                f_file.close()
                self.close_devices()

                self.dialog_result = True

                time.sleep(1.0)
                pydaw_util.pydaw_read_device_config()
                f_window.close()

            except Exception as ex:
                QMessageBox.warning(f_window, _("Error"),
                    _("Couldn't open audio device\n\n{}\n\n"
                    "This may (or may not) be because the "
                    "device is already open by another application or "
                    "a sound daemon such as JACK.").format(ex))

        def on_cancel(a_self=None):
            f_window.close()

        f_ok_button.pressed.connect(on_ok)
        f_cancel_button.pressed.connect(on_cancel)

        f_device_name_combobox.currentIndexChanged.connect(combobox_changed)
        f_audio_device_names.sort(key=lambda x: x.lower())
        f_device_name_combobox.addItems(f_audio_device_names)

        if "name" in pydaw_util.global_device_val_dict:
            f_name = pydaw_util.global_device_val_dict["name"]
            if f_name in f_result_dict:
                f_device_name_combobox.setCurrentIndex(
                    f_device_name_combobox.findText(f_name))
            elif "(hw:" in f_name:
                f_name = f_name.split("(hw:")[0]
                for f_dev in f_result_dict:
                    if f_dev.startswith(f_name):
                        print("Device number changed, fixing")
                        f_device_name_combobox.setCurrentIndex(
                            f_device_name_combobox.findText(f_dev))
                        break


        if "audioInputs" in pydaw_util.global_device_val_dict:
            f_count = int(pydaw_util.global_device_val_dict["audioInputs"])
            f_audio_in_spinbox.setValue(f_count)

        if "bufferSize" in pydaw_util.global_device_val_dict and \
        pydaw_util.global_device_val_dict["bufferSize"] in self.buffer_sizes:
            f_buffer_size_combobox.setCurrentIndex(
                f_buffer_size_combobox.findText(
                    pydaw_util.global_device_val_dict["bufferSize"]))

        if "sampleRate" in pydaw_util.global_device_val_dict and \
        pydaw_util.global_device_val_dict["sampleRate"] in self.sample_rates:
            f_samplerate_combobox.setCurrentIndex(
                f_samplerate_combobox.findText(
                    pydaw_util.global_device_val_dict["sampleRate"]))

        if "threads" in pydaw_util.global_device_val_dict:
            f_worker_threads_combobox.setCurrentIndex(
                int(pydaw_util.global_device_val_dict["threads"]))

        if "threadAffinity" in pydaw_util.global_device_val_dict:
            if int(pydaw_util.global_device_val_dict["threadAffinity"]) == 1:
                f_thread_affinity_checkbox.setChecked(True)

        if "performance" in pydaw_util.global_device_val_dict:
            if int(pydaw_util.global_device_val_dict["performance"]) == 1:
                f_governor_checkbox.setChecked(True)

        if "hugePages" in pydaw_util.global_device_val_dict and \
        int(pydaw_util.global_device_val_dict["hugePages"]) == 1:
            f_hugepages_checkbox.setChecked(True)

        if "audioEngine" in pydaw_util.global_device_val_dict:
            f_audio_engine_combobox.setCurrentIndex(
                int(pydaw_util.global_device_val_dict["audioEngine"]))

        if a_msg is not None:
            QMessageBox.warning(f_window, _("Error"), a_msg)

        f_screen = QDesktopWidget().screenGeometry()
        f_size = f_window.geometry()
        f_hpos = (f_screen.width() - f_size.width()) / 2
        f_vpos = (f_screen.height() - f_size.height()) / 2
        f_window.move(f_hpos, f_vpos)
        latency_changed()
        if self.is_running:
            f_window.exec_()
        else:
            f_window.show()

if __name__ == "__main__":
    def _pydaw_device_dialog_standalone():
        app = QApplication(sys.argv)
        if len(sys.argv) == 2:
            f_msg = sys.argv[1]
        else:
            f_msg = None

        f_pydaw_device_dialog = pydaw_device_dialog()
        f_pydaw_device_dialog.show_device_dialog(f_msg)
        sys.exit(app.exec_())

    _pydaw_device_dialog_standalone()
