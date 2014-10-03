/*
This file is part of the PyDAW project, Copyright PyDAW Team

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
*/

#ifndef SCC_LIBMODSYNTH_H
#define	SCC_LIBMODSYNTH_H

#ifdef	__cplusplus
extern "C" {
#endif

#include "../../libmodsynth/constants.h"
#include "../../libmodsynth/modules/dynamics/sidechain_comp.h"


typedef struct
{
    t_scc_sidechain_comp sidechain_comp;
}t_scc_mono_modules;

t_scc_mono_modules * v_scc_mono_init(float, int);

t_scc_mono_modules * v_scc_mono_init(float a_sr, int a_plugin_uid)
{
    t_scc_mono_modules * f_result;
    g_scc_init(&f_result->sidechain_comp, a_sr);
    return f_result;
}



#ifdef	__cplusplus
}
#endif

#endif	/* LIBMODSYNTH_H */

