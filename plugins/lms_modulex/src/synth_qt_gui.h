/* -*- c-basic-offset: 4 -*-  vi:set ts=8 sts=4 sw=4: */

/* synth_qt_gui.h


This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

*/

#ifndef MODULEX_QT_GUI_H_INCLUDED_
#define MODULEX_QT_GUI_H_INCLUDED_

#include <QFrame>
#include <QDial>
#include <QLabel>
#include <QLayout>
#include <QGroupBox>
#include <QComboBox>
#include <QPixmap>

#include <string>
#include <stdlib.h>

#include "../../libmodsynth/widgets/lms_main_layout.h"
#include "../../libmodsynth/widgets/ui_modules/multieffect_basic.h"

extern "C" {
#include <lo/lo.h>
}

class modulex_gui : public QFrame
{
    Q_OBJECT

public:
    modulex_gui(const char * host, const char * port,
	     QByteArray controlPath, QByteArray midiPath, QByteArray programPath,
	     QByteArray exitingPath, QWidget *w = 0);
    virtual ~modulex_gui();

    bool ready() const { return m_ready; }
    void setReady(bool ready) { m_ready = ready; }

    void setHostRequestedQuit(bool r) { m_hostRequestedQuit = r; }
    
    
    void v_set_control(int, float);
    void v_control_changed(int, int, bool);
    int i_get_control(int);
        
    void v_print_port_name_to_cerr(int);
    void lms_set_value(float val, LMS_control * a_ctrl );
    void lms_value_changed(int a_value, LMS_control * a_ctrl);
        
public slots:
    /*Event handlers for setting knob values*/
    void setFX0knob0 (float val);
    void setFX0knob1 (float val);
    void setFX0knob2 (float val);
    void setFX0combobox (float val);
    
    void setFX1knob0 (float val);
    void setFX1knob1 (float val);
    void setFX1knob2 (float val);
    void setFX1combobox (float val);
    
    void setFX2knob0 (float val);
    void setFX2knob1 (float val);
    void setFX2knob2 (float val);
    void setFX2combobox (float val);
    
    void setFX3knob0 (float val);
    void setFX3knob1 (float val);
    void setFX3knob2 (float val);
    void setFX3combobox (float val);
    
    void aboutToQuit();
    
protected slots:
    /*Event handlers for receiving changed knob values*/
    void fx0knob0Changed(int);
    void fx0knob1Changed(int);
    void fx0knob2Changed(int);
    void fx0comboboxChanged(int);
    
    void fx1knob0Changed(int);
    void fx1knob1Changed(int);
    void fx1knob2Changed(int);
    void fx1comboboxChanged(int);
    
    void fx2knob0Changed(int);
    void fx2knob1Changed(int);
    void fx2knob2Changed(int);
    void fx2comboboxChanged(int);
    
    void fx3knob0Changed(int);
    void fx3knob1Changed(int);
    void fx3knob2Changed(int);
    void fx3comboboxChanged(int);
        
    void oscRecv();
protected:
    
    /*Declare a QLabel and QDial for each knob.  Also declare any other controls that set/receive values here*/
    LMS_main_layout * m_main_layout;
    LMS_multieffect * m_fx0;
    LMS_multieffect * m_fx1;
    LMS_multieffect * m_fx2;
    LMS_multieffect * m_fx3;
    
    lo_address m_host;
    QByteArray m_controlPath;
    QByteArray m_midiPath;
    QByteArray m_programPath;
    QByteArray m_exitingPath;

    bool m_suppressHostUpdate;
    bool m_hostRequestedQuit;
    bool m_ready;    
};


#endif
