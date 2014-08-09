# -*- coding: utf-8 -*-
"""
This file is part of the PyDAW project, Copyright PyDAW Team

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
"""

#Euphoria
EUPHORIA_FILES_STRING_DELIMITER = '|'
EUPHORIA_MAX_SAMPLE_COUNT = 100

#Total number of LFOs, ADSRs, other envelopes, etc... Used for the PolyFX mod matrix
EUPHORIA_MODULATOR_COUNT = 4
#How many modular PolyFX
EUPHORIA_MODULAR_POLYFX_COUNT = 4
#How many ports per PolyFX, 3 knobs and a combobox
EUPHORIA_PORTS_PER_MOD_EFFECT = 4
#How many knobs per PolyFX, 3 knobs
EUPHORIA_CONTROLS_PER_MOD_EFFECT = 3
EUPHORIA_EFFECTS_GROUPS_COUNT = 1
#The number of mono_fx groups
EUPHORIA_MONO_FX_GROUPS_COUNT = EUPHORIA_MAX_SAMPLE_COUNT
EUPHORIA_MONO_FX_COUNT = 4
EUPHORIA_OUTPUT_LEFT = 0
EUPHORIA_OUTPUT_RIGHT = 1
EUPHORIA_FIRST_CONTROL_PORT = 2
EUPHORIA_SELECTED_SAMPLE = 2
EUPHORIA_ATTACK = 3
EUPHORIA_DECAY = 4
EUPHORIA_SUSTAIN = 5
EUPHORIA_RELEASE = 6
EUPHORIA_FILTER_ATTACK = 7
EUPHORIA_FILTER_DECAY = 8
EUPHORIA_FILTER_SUSTAIN = 9
EUPHORIA_FILTER_RELEASE = 10
EUPHORIA_LFO_PITCH = 11
EUPHORIA_MASTER_VOLUME = 12
EUPHORIA_MASTER_GLIDE = 13
EUPHORIA_MASTER_PITCHBEND_AMT = 14
EUPHORIA_PITCH_ENV_TIME = 15
EUPHORIA_LFO_FREQ = 16
EUPHORIA_LFO_TYPE = 17
#From Modulex
EUPHORIA_FX0_KNOB0 = 18
EUPHORIA_FX0_KNOB1 = 19
EUPHORIA_FX0_KNOB2 = 20
EUPHORIA_FX0_COMBOBOX = 21
EUPHORIA_FX1_KNOB0 = 22
EUPHORIA_FX1_KNOB1 = 23
EUPHORIA_FX1_KNOB2 = 24
EUPHORIA_FX1_COMBOBOX = 25
EUPHORIA_FX2_KNOB0 = 26
EUPHORIA_FX2_KNOB1 = 27
EUPHORIA_FX2_KNOB2 = 28
EUPHORIA_FX2_COMBOBOX = 29
EUPHORIA_FX3_KNOB0 = 30
EUPHORIA_FX3_KNOB1 = 31
EUPHORIA_FX3_KNOB2 = 32
EUPHORIA_FX3_COMBOBOX = 33
#PolyFX Mod Matrix
EUPHORIA_PFXMATRIX_FIRST_PORT = 34
EUPHORIA_PFXMATRIX_GRP0DST0SRC0CTRL0 = 34
EUPHORIA_PFXMATRIX_GRP0DST0SRC0CTRL1 = 35
EUPHORIA_PFXMATRIX_GRP0DST0SRC0CTRL2 = 36
EUPHORIA_PFXMATRIX_GRP0DST0SRC1CTRL0 = 37
EUPHORIA_PFXMATRIX_GRP0DST0SRC1CTRL1 = 38
EUPHORIA_PFXMATRIX_GRP0DST0SRC1CTRL2 = 39
EUPHORIA_PFXMATRIX_GRP0DST0SRC2CTRL0 = 40
EUPHORIA_PFXMATRIX_GRP0DST0SRC2CTRL1 = 41
EUPHORIA_PFXMATRIX_GRP0DST0SRC2CTRL2 = 42
EUPHORIA_PFXMATRIX_GRP0DST0SRC3CTRL0 = 43
EUPHORIA_PFXMATRIX_GRP0DST0SRC3CTRL1 = 44
EUPHORIA_PFXMATRIX_GRP0DST0SRC3CTRL2 = 45
EUPHORIA_PFXMATRIX_GRP0DST1SRC0CTRL0 = 46
EUPHORIA_PFXMATRIX_GRP0DST1SRC0CTRL1 = 47
EUPHORIA_PFXMATRIX_GRP0DST1SRC0CTRL2 = 48
EUPHORIA_PFXMATRIX_GRP0DST1SRC1CTRL0 = 49
EUPHORIA_PFXMATRIX_GRP0DST1SRC1CTRL1 = 50
EUPHORIA_PFXMATRIX_GRP0DST1SRC1CTRL2 = 51
EUPHORIA_PFXMATRIX_GRP0DST1SRC2CTRL0 = 52
EUPHORIA_PFXMATRIX_GRP0DST1SRC2CTRL1 = 53
EUPHORIA_PFXMATRIX_GRP0DST1SRC2CTRL2 = 54
EUPHORIA_PFXMATRIX_GRP0DST1SRC3CTRL0 = 55
EUPHORIA_PFXMATRIX_GRP0DST1SRC3CTRL1 = 56
EUPHORIA_PFXMATRIX_GRP0DST1SRC3CTRL2 = 57
EUPHORIA_PFXMATRIX_GRP0DST2SRC0CTRL0 = 58
EUPHORIA_PFXMATRIX_GRP0DST2SRC0CTRL1 = 59
EUPHORIA_PFXMATRIX_GRP0DST2SRC0CTRL2 = 60
EUPHORIA_PFXMATRIX_GRP0DST2SRC1CTRL0 = 61
EUPHORIA_PFXMATRIX_GRP0DST2SRC1CTRL1 = 62
EUPHORIA_PFXMATRIX_GRP0DST2SRC1CTRL2 = 63
EUPHORIA_PFXMATRIX_GRP0DST2SRC2CTRL0 = 64
EUPHORIA_PFXMATRIX_GRP0DST2SRC2CTRL1 = 65
EUPHORIA_PFXMATRIX_GRP0DST2SRC2CTRL2 = 66
EUPHORIA_PFXMATRIX_GRP0DST2SRC3CTRL0 = 67
EUPHORIA_PFXMATRIX_GRP0DST2SRC3CTRL1 = 68
EUPHORIA_PFXMATRIX_GRP0DST2SRC3CTRL2 = 69
EUPHORIA_PFXMATRIX_GRP0DST3SRC0CTRL0 = 70
EUPHORIA_PFXMATRIX_GRP0DST3SRC0CTRL1 = 71
EUPHORIA_PFXMATRIX_GRP0DST3SRC0CTRL2 = 72
EUPHORIA_PFXMATRIX_GRP0DST3SRC1CTRL0 = 73
EUPHORIA_PFXMATRIX_GRP0DST3SRC1CTRL1 = 74
EUPHORIA_PFXMATRIX_GRP0DST3SRC1CTRL2 = 75
EUPHORIA_PFXMATRIX_GRP0DST3SRC2CTRL0 = 76
EUPHORIA_PFXMATRIX_GRP0DST3SRC2CTRL1 = 77
EUPHORIA_PFXMATRIX_GRP0DST3SRC2CTRL2 = 78
EUPHORIA_PFXMATRIX_GRP0DST3SRC3CTRL0 = 79
EUPHORIA_PFXMATRIX_GRP0DST3SRC3CTRL1 = 80
EUPHORIA_PFXMATRIX_GRP0DST3SRC3CTRL2 = 81

EUPHORIA_PFXMATRIX_GRP0DST0SRC4CTRL0 = 82
EUPHORIA_PFXMATRIX_GRP0DST0SRC4CTRL1 = 83
EUPHORIA_PFXMATRIX_GRP0DST0SRC4CTRL2 = 84
EUPHORIA_PFXMATRIX_GRP0DST1SRC4CTRL0 = 85
EUPHORIA_PFXMATRIX_GRP0DST1SRC4CTRL1 = 86
EUPHORIA_PFXMATRIX_GRP0DST1SRC4CTRL2 = 87
EUPHORIA_PFXMATRIX_GRP0DST2SRC4CTRL0 = 88
EUPHORIA_PFXMATRIX_GRP0DST2SRC4CTRL1 = 89
EUPHORIA_PFXMATRIX_GRP0DST2SRC4CTRL2 = 90
EUPHORIA_PFXMATRIX_GRP0DST3SRC4CTRL0 = 91
EUPHORIA_PFXMATRIX_GRP0DST3SRC4CTRL1 = 92
EUPHORIA_PFXMATRIX_GRP0DST3SRC4CTRL2 = 93

EUPHORIA_PFXMATRIX_GRP0DST0SRC5CTRL0 = 94
EUPHORIA_PFXMATRIX_GRP0DST0SRC5CTRL1 = 95
EUPHORIA_PFXMATRIX_GRP0DST0SRC5CTRL2 = 96
EUPHORIA_PFXMATRIX_GRP0DST1SRC5CTRL0 = 97
EUPHORIA_PFXMATRIX_GRP0DST1SRC5CTRL1 = 98
EUPHORIA_PFXMATRIX_GRP0DST1SRC5CTRL2 = 99
EUPHORIA_PFXMATRIX_GRP0DST2SRC5CTRL0 = 100
EUPHORIA_PFXMATRIX_GRP0DST2SRC5CTRL1 = 101
EUPHORIA_PFXMATRIX_GRP0DST2SRC5CTRL2 = 102
EUPHORIA_PFXMATRIX_GRP0DST3SRC5CTRL0 = 103
EUPHORIA_PFXMATRIX_GRP0DST3SRC5CTRL1 = 104
EUPHORIA_PFXMATRIX_GRP0DST3SRC5CTRL2 = 105

#End PolyFX Mod Matrix

# This is the last control port, + 1, for zero-based iteration
EUPHORIA_LAST_REGULAR_CONTROL_PORT = 106
# The first port to use when enumerating the ports for mod_matrix controls.
# All of the mod_matrix ports should be sequential,
# * any additional ports should prepend self port number
EUPHORIA_FIRST_SAMPLE_TABLE_PORT = 106
#The range of ports for sample pitch
EUPHORIA_SAMPLE_PITCH_PORT_RANGE_MIN = EUPHORIA_FIRST_SAMPLE_TABLE_PORT
EUPHORIA_SAMPLE_PITCH_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_PITCH_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
#The range of ports for the low note to play a sample on
EUPHORIA_PLAY_PITCH_LOW_PORT_RANGE_MIN = EUPHORIA_SAMPLE_PITCH_PORT_RANGE_MAX
EUPHORIA_PLAY_PITCH_LOW_PORT_RANGE_MAX = \
    (EUPHORIA_PLAY_PITCH_LOW_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
#The range of ports for the high note to play a sample on
EUPHORIA_PLAY_PITCH_HIGH_PORT_RANGE_MIN = EUPHORIA_PLAY_PITCH_LOW_PORT_RANGE_MAX
EUPHORIA_PLAY_PITCH_HIGH_PORT_RANGE_MAX = \
    (EUPHORIA_PLAY_PITCH_HIGH_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
#The range of ports for sample volume
EUPHORIA_SAMPLE_VOLUME_PORT_RANGE_MIN = EUPHORIA_PLAY_PITCH_HIGH_PORT_RANGE_MAX
EUPHORIA_SAMPLE_VOLUME_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_VOLUME_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_SAMPLE_START_PORT_RANGE_MIN = EUPHORIA_SAMPLE_VOLUME_PORT_RANGE_MAX
EUPHORIA_SAMPLE_START_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_START_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_SAMPLE_END_PORT_RANGE_MIN = EUPHORIA_SAMPLE_START_PORT_RANGE_MAX
EUPHORIA_SAMPLE_END_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_END_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_SAMPLE_VEL_SENS_PORT_RANGE_MIN = EUPHORIA_SAMPLE_END_PORT_RANGE_MAX
EUPHORIA_SAMPLE_VEL_SENS_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_VEL_SENS_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_SAMPLE_VEL_LOW_PORT_RANGE_MIN = EUPHORIA_SAMPLE_VEL_SENS_PORT_RANGE_MAX
EUPHORIA_SAMPLE_VEL_LOW_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_VEL_LOW_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_SAMPLE_VEL_HIGH_PORT_RANGE_MIN = EUPHORIA_SAMPLE_VEL_LOW_PORT_RANGE_MAX
EUPHORIA_SAMPLE_VEL_HIGH_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_VEL_HIGH_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_PITCH_PORT_RANGE_MIN = EUPHORIA_SAMPLE_VEL_HIGH_PORT_RANGE_MAX
EUPHORIA_PITCH_PORT_RANGE_MAX = (EUPHORIA_PITCH_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_TUNE_PORT_RANGE_MIN = EUPHORIA_PITCH_PORT_RANGE_MAX
EUPHORIA_TUNE_PORT_RANGE_MAX = (EUPHORIA_TUNE_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_SAMPLE_INTERPOLATION_MODE_PORT_RANGE_MIN = EUPHORIA_TUNE_PORT_RANGE_MAX
EUPHORIA_SAMPLE_INTERPOLATION_MODE_PORT_RANGE_MAX = \
(EUPHORIA_SAMPLE_INTERPOLATION_MODE_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_SAMPLE_LOOP_START_PORT_RANGE_MIN = EUPHORIA_SAMPLE_INTERPOLATION_MODE_PORT_RANGE_MAX
EUPHORIA_SAMPLE_LOOP_START_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_LOOP_START_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_SAMPLE_LOOP_END_PORT_RANGE_MIN = EUPHORIA_SAMPLE_LOOP_START_PORT_RANGE_MAX
EUPHORIA_SAMPLE_LOOP_END_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_LOOP_END_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
EUPHORIA_SAMPLE_LOOP_MODE_PORT_RANGE_MIN = EUPHORIA_SAMPLE_LOOP_END_PORT_RANGE_MAX
EUPHORIA_SAMPLE_LOOP_MODE_PORT_RANGE_MAX = \
    (EUPHORIA_SAMPLE_LOOP_MODE_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
#MonoFX0
EUPHORIA_MONO_FX0_KNOB0_PORT_RANGE_MIN = EUPHORIA_SAMPLE_LOOP_MODE_PORT_RANGE_MAX
EUPHORIA_MONO_FX0_KNOB0_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX0_KNOB0_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX0_KNOB1_PORT_RANGE_MIN = EUPHORIA_MONO_FX0_KNOB0_PORT_RANGE_MAX
EUPHORIA_MONO_FX0_KNOB1_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX0_KNOB1_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX0_KNOB2_PORT_RANGE_MIN = EUPHORIA_MONO_FX0_KNOB1_PORT_RANGE_MAX
EUPHORIA_MONO_FX0_KNOB2_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX0_KNOB2_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX0_COMBOBOX_PORT_RANGE_MIN = EUPHORIA_MONO_FX0_KNOB2_PORT_RANGE_MAX
EUPHORIA_MONO_FX0_COMBOBOX_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX0_COMBOBOX_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
#MonoFX1
EUPHORIA_MONO_FX1_KNOB0_PORT_RANGE_MIN = EUPHORIA_MONO_FX0_COMBOBOX_PORT_RANGE_MAX
EUPHORIA_MONO_FX1_KNOB0_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX1_KNOB0_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX1_KNOB1_PORT_RANGE_MIN = EUPHORIA_MONO_FX1_KNOB0_PORT_RANGE_MAX
EUPHORIA_MONO_FX1_KNOB1_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX1_KNOB1_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX1_KNOB2_PORT_RANGE_MIN = EUPHORIA_MONO_FX1_KNOB1_PORT_RANGE_MAX
EUPHORIA_MONO_FX1_KNOB2_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX1_KNOB2_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX1_COMBOBOX_PORT_RANGE_MIN = EUPHORIA_MONO_FX1_KNOB2_PORT_RANGE_MAX
EUPHORIA_MONO_FX1_COMBOBOX_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX1_COMBOBOX_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
#MonoFX2
EUPHORIA_MONO_FX2_KNOB0_PORT_RANGE_MIN = EUPHORIA_MONO_FX1_COMBOBOX_PORT_RANGE_MAX
EUPHORIA_MONO_FX2_KNOB0_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX2_KNOB0_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX2_KNOB1_PORT_RANGE_MIN = EUPHORIA_MONO_FX2_KNOB0_PORT_RANGE_MAX
EUPHORIA_MONO_FX2_KNOB1_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX2_KNOB1_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX2_KNOB2_PORT_RANGE_MIN = EUPHORIA_MONO_FX2_KNOB1_PORT_RANGE_MAX
EUPHORIA_MONO_FX2_KNOB2_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX2_KNOB2_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX2_COMBOBOX_PORT_RANGE_MIN = EUPHORIA_MONO_FX2_KNOB2_PORT_RANGE_MAX
EUPHORIA_MONO_FX2_COMBOBOX_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX2_COMBOBOX_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
#MonoFX3
EUPHORIA_MONO_FX3_KNOB0_PORT_RANGE_MIN = EUPHORIA_MONO_FX2_COMBOBOX_PORT_RANGE_MAX
EUPHORIA_MONO_FX3_KNOB0_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX3_KNOB0_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX3_KNOB1_PORT_RANGE_MIN = EUPHORIA_MONO_FX3_KNOB0_PORT_RANGE_MAX
EUPHORIA_MONO_FX3_KNOB1_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX3_KNOB1_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX3_KNOB2_PORT_RANGE_MIN = EUPHORIA_MONO_FX3_KNOB1_PORT_RANGE_MAX
EUPHORIA_MONO_FX3_KNOB2_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX3_KNOB2_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
EUPHORIA_MONO_FX3_COMBOBOX_PORT_RANGE_MIN = EUPHORIA_MONO_FX3_KNOB2_PORT_RANGE_MAX
EUPHORIA_MONO_FX3_COMBOBOX_PORT_RANGE_MAX = \
    (EUPHORIA_MONO_FX3_COMBOBOX_PORT_RANGE_MIN + EUPHORIA_MONO_FX_GROUPS_COUNT)
#Sample FX Group
EUPHORIA_SAMPLE_MONO_FX_GROUP_PORT_RANGE_MIN = EUPHORIA_MONO_FX3_COMBOBOX_PORT_RANGE_MAX
EUPHORIA_SAMPLE_MONO_FX_GROUP_PORT_RANGE_MAX = \
(EUPHORIA_SAMPLE_MONO_FX_GROUP_PORT_RANGE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
#Noise amp
EUPHORIA_NOISE_AMP_MIN = EUPHORIA_SAMPLE_MONO_FX_GROUP_PORT_RANGE_MAX
EUPHORIA_NOISE_AMP_MAX = (EUPHORIA_NOISE_AMP_MIN + EUPHORIA_MAX_SAMPLE_COUNT)
#Noise type
EUPHORIA_NOISE_TYPE_MIN = EUPHORIA_NOISE_AMP_MAX
EUPHORIA_NOISE_TYPE_MAX = (EUPHORIA_NOISE_TYPE_MIN + EUPHORIA_MAX_SAMPLE_COUNT)

#sample fade-in
EUPHORIA_SAMPLE_FADE_IN_MIN = EUPHORIA_NOISE_TYPE_MAX
EUPHORIA_SAMPLE_FADE_IN_MAX = (EUPHORIA_SAMPLE_FADE_IN_MIN + EUPHORIA_MAX_SAMPLE_COUNT)

#sample fade-out
EUPHORIA_SAMPLE_FADE_OUT_MIN = EUPHORIA_SAMPLE_FADE_IN_MAX
EUPHORIA_SAMPLE_FADE_OUT_MAX = (EUPHORIA_SAMPLE_FADE_OUT_MIN + EUPHORIA_MAX_SAMPLE_COUNT)

EUPHORIA_FIRST_EQ_PORT = EUPHORIA_SAMPLE_FADE_OUT_MAX

# Stacked as:
# 100 *
#     [freq, bw, gain] * 6

EUPHORIA_LAST_EQ_PORT = (EUPHORIA_FIRST_EQ_PORT + (18 * 100))

EUPHORIA_LFO_PITCH_FINE = EUPHORIA_LAST_EQ_PORT
EUPHORIA_MIN_NOTE = EUPHORIA_LFO_PITCH_FINE + 1
EUPHORIA_MAX_NOTE = EUPHORIA_MIN_NOTE + 1


#Modulex

MODULEX_INPUT0 = 0
MODULEX_INPUT1 = 1
MODULEX_OUTPUT0 = 2
MODULEX_OUTPUT1 = 3
MODULEX_FIRST_CONTROL_PORT = 4
MODULEX_FX0_KNOB0 = 4
MODULEX_FX0_KNOB1 = 5
MODULEX_FX0_KNOB2 = 6
MODULEX_FX0_COMBOBOX = 7
MODULEX_FX1_KNOB0 = 8
MODULEX_FX1_KNOB1 = 9
MODULEX_FX1_KNOB2 = 10
MODULEX_FX1_COMBOBOX = 11
MODULEX_FX2_KNOB0 = 12
MODULEX_FX2_KNOB1 = 13
MODULEX_FX2_KNOB2 = 14
MODULEX_FX2_COMBOBOX = 15
MODULEX_FX3_KNOB0 = 16
MODULEX_FX3_KNOB1 = 17
MODULEX_FX3_KNOB2 = 18
MODULEX_FX3_COMBOBOX = 19
MODULEX_FX4_KNOB0 = 20
MODULEX_FX4_KNOB1 = 21
MODULEX_FX4_KNOB2 = 22
MODULEX_FX4_COMBOBOX = 23
MODULEX_FX5_KNOB0 = 24
MODULEX_FX5_KNOB1 = 25
MODULEX_FX5_KNOB2 = 26
MODULEX_FX5_COMBOBOX = 27
MODULEX_FX6_KNOB0 = 28
MODULEX_FX6_KNOB1 = 29
MODULEX_FX6_KNOB2 = 30
MODULEX_FX6_COMBOBOX = 31
MODULEX_FX7_KNOB0 = 32
MODULEX_FX7_KNOB1 = 33
MODULEX_FX7_KNOB2 = 34
MODULEX_FX7_COMBOBOX = 35
MODULEX_DELAY_TIME = 36
MODULEX_FEEDBACK = 37
MODULEX_DRY = 38
MODULEX_WET = 39
MODULEX_DUCK = 40
MODULEX_CUTOFF = 41
MODULEX_STEREO = 42
MODULEX_VOL_SLIDER = 43
MODULEX_REVERB_TIME = 44
MODULEX_REVERB_WET = 45
MODULEX_REVERB_COLOR = 46

MODULEX_EQ_ON = 47
MODULEX_EQ1_FREQ = 48
MODULEX_EQ1_RES = 49
MODULEX_EQ1_GAIN = 50
MODULEX_EQ1_FREQ = 48
MODULEX_EQ1_RES = 49
MODULEX_EQ1_GAIN = 50
MODULEX_EQ2_FREQ = 51
MODULEX_EQ2_RES = 52
MODULEX_EQ2_GAIN = 53
MODULEX_EQ3_FREQ = 54
MODULEX_EQ3_RES = 55
MODULEX_EQ3_GAIN = 56
MODULEX_EQ4_FREQ = 57
MODULEX_EQ4_RES = 58
MODULEX_EQ4_GAIN = 59
MODULEX_EQ5_FREQ = 60
MODULEX_EQ5_RES = 61
MODULEX_EQ5_GAIN = 62
MODULEX_EQ6_FREQ = 63
MODULEX_EQ6_RES = 64
MODULEX_EQ6_GAIN = 65
MODULEX_SPECTRUM_ENABLED = 66
MODULEX_GATE_NOTE = 67
MODULEX_GATE_MODE = 68
MODULEX_GATE_WET = 69
MODULEX_GATE_PITCH = 70
MODULEX_GLITCH_ON = 71
MODULEX_GLITCH_NOTE = 72
MODULEX_GLITCH_TIME = 73
MODULEX_REVERB_DRY = 74
MODULEX_GLITCH_PB = 75
MODULEX_REVERB_PRE_DELAY = 76

#Total number of LFOs, ADSRs, other envelopes, etc... Used for the PolyFX mod matrix
WAYV_MODULATOR_COUNT = 4
#How many modular PolyFX
WAYV_MODULAR_POLYFX_COUNT = 4
#How many ports per PolyFX, 3 knobs and a combobox
WAYV_PORTS_PER_MOD_EFFECT = 4
#How many knobs per PolyFX, 3 knobs
WAYV_CONTROLS_PER_MOD_EFFECT = 3
WAYV_EFFECTS_GROUPS_COUNT = 1
WAYV_OUTPUT0 = 0
WAYV_OUTPUT1 = 1
WAYV_FIRST_CONTROL_PORT = 2
WAYV_ATTACK_MAIN = 2
WAYV_DECAY_MAIN = 3
WAYV_SUSTAIN_MAIN = 4
WAYV_RELEASE_MAIN = 5
WAYV_NOISE_AMP = 6
WAYV_OSC1_TYPE = 7
WAYV_OSC1_PITCH = 8
WAYV_OSC1_TUNE = 9
WAYV_OSC1_VOLUME = 10
WAYV_OSC2_TYPE = 11
WAYV_OSC2_PITCH = 12
WAYV_OSC2_TUNE = 13
WAYV_OSC2_VOLUME = 14
WAYV_MASTER_VOLUME = 15
WAYV_OSC1_UNISON_VOICES = 16
WAYV_OSC1_UNISON_SPREAD = 17
WAYV_MASTER_GLIDE = 18
WAYV_MASTER_PITCHBEND_AMT = 19
WAYV_ATTACK1 = 20
WAYV_DECAY1 = 21
WAYV_SUSTAIN1 = 22
WAYV_RELEASE1 = 23
WAYV_ATTACK2 = 24
WAYV_DECAY2 = 25
WAYV_SUSTAIN2 = 26
WAYV_RELEASE2 = 27
WAYV_ATTACK_PFX1 = 28
WAYV_DECAY_PFX1 = 29
WAYV_SUSTAIN_PFX1 = 30
WAYV_RELEASE_PFX1 = 31
WAYV_ATTACK_PFX2 = 32
WAYV_DECAY_PFX2 = 33
WAYV_SUSTAIN_PFX2 = 34
WAYV_RELEASE_PFX2 = 35
WAYV_NOISE_TYPE = 36
WAYV_RAMP_ENV_TIME = 37
WAYV_LFO_FREQ = 38
WAYV_LFO_TYPE = 39
WAYV_FX0_KNOB0 = 40
WAYV_FX0_KNOB1 = 41
WAYV_FX0_KNOB2 = 42
WAYV_FX0_COMBOBOX = 43
WAYV_FX1_KNOB0 = 44
WAYV_FX1_KNOB1 = 45
WAYV_FX1_KNOB2 = 46
WAYV_FX1_COMBOBOX = 47
WAYV_FX2_KNOB0 = 48
WAYV_FX2_KNOB1 = 49
WAYV_FX2_KNOB2 = 50
WAYV_FX2_COMBOBOX = 51
WAYV_FX3_KNOB0 = 52
WAYV_FX3_KNOB1 = 53
WAYV_FX3_KNOB2 = 54
WAYV_FX3_COMBOBOX = 55
#PolyFX Mod Matrix
WAVV_PFXMATRIX_FIRST_PORT = 56
WAVV_PFXMATRIX_GRP0DST0SRC0CTRL0 = 56
WAVV_PFXMATRIX_GRP0DST0SRC0CTRL1 = 57
WAVV_PFXMATRIX_GRP0DST0SRC0CTRL2 = 58
WAVV_PFXMATRIX_GRP0DST0SRC1CTRL0 = 59
WAVV_PFXMATRIX_GRP0DST0SRC1CTRL1 = 60
WAVV_PFXMATRIX_GRP0DST0SRC1CTRL2 = 61
WAVV_PFXMATRIX_GRP0DST0SRC2CTRL0 = 62
WAVV_PFXMATRIX_GRP0DST0SRC2CTRL1 = 63
WAVV_PFXMATRIX_GRP0DST0SRC2CTRL2 = 64
WAVV_PFXMATRIX_GRP0DST0SRC3CTRL0 = 65
WAVV_PFXMATRIX_GRP0DST0SRC3CTRL1 = 66
WAVV_PFXMATRIX_GRP0DST0SRC3CTRL2 = 67
WAVV_PFXMATRIX_GRP0DST1SRC0CTRL0 = 68
WAVV_PFXMATRIX_GRP0DST1SRC0CTRL1 = 69
WAVV_PFXMATRIX_GRP0DST1SRC0CTRL2 = 70
WAVV_PFXMATRIX_GRP0DST1SRC1CTRL0 = 71
WAVV_PFXMATRIX_GRP0DST1SRC1CTRL1 = 72
WAVV_PFXMATRIX_GRP0DST1SRC1CTRL2 = 73
WAVV_PFXMATRIX_GRP0DST1SRC2CTRL0 = 74
WAVV_PFXMATRIX_GRP0DST1SRC2CTRL1 = 75
WAVV_PFXMATRIX_GRP0DST1SRC2CTRL2 = 76
WAVV_PFXMATRIX_GRP0DST1SRC3CTRL0 = 77
WAVV_PFXMATRIX_GRP0DST1SRC3CTRL1 = 78
WAVV_PFXMATRIX_GRP0DST1SRC3CTRL2 = 79
WAVV_PFXMATRIX_GRP0DST2SRC0CTRL0 = 80
WAVV_PFXMATRIX_GRP0DST2SRC0CTRL1 = 81
WAVV_PFXMATRIX_GRP0DST2SRC0CTRL2 = 82
WAVV_PFXMATRIX_GRP0DST2SRC1CTRL0 = 83
WAVV_PFXMATRIX_GRP0DST2SRC1CTRL1 = 84
WAVV_PFXMATRIX_GRP0DST2SRC1CTRL2 = 85
WAVV_PFXMATRIX_GRP0DST2SRC2CTRL0 = 86
WAVV_PFXMATRIX_GRP0DST2SRC2CTRL1 = 87
WAVV_PFXMATRIX_GRP0DST2SRC2CTRL2 = 88
WAVV_PFXMATRIX_GRP0DST2SRC3CTRL0 = 89
WAVV_PFXMATRIX_GRP0DST2SRC3CTRL1 = 90
WAVV_PFXMATRIX_GRP0DST2SRC3CTRL2 = 91
WAVV_PFXMATRIX_GRP0DST3SRC0CTRL0 = 92
WAVV_PFXMATRIX_GRP0DST3SRC0CTRL1 = 93
WAVV_PFXMATRIX_GRP0DST3SRC0CTRL2 = 94
WAVV_PFXMATRIX_GRP0DST3SRC1CTRL0 = 95
WAVV_PFXMATRIX_GRP0DST3SRC1CTRL1 = 96
WAVV_PFXMATRIX_GRP0DST3SRC1CTRL2 = 97
WAVV_PFXMATRIX_GRP0DST3SRC2CTRL0 = 98
WAVV_PFXMATRIX_GRP0DST3SRC2CTRL1 = 99
WAVV_PFXMATRIX_GRP0DST3SRC2CTRL2 = 100
WAVV_PFXMATRIX_GRP0DST3SRC3CTRL0 = 101
WAVV_PFXMATRIX_GRP0DST3SRC3CTRL1 = 102
WAVV_PFXMATRIX_GRP0DST3SRC3CTRL2 = 103
#End PolyFX Mod Matrix
WAYV_ADSR1_CHECKBOX = 105
WAYV_ADSR2_CHECKBOX = 106
WAYV_LFO_AMP = 107
WAYV_LFO_PITCH = 108
WAYV_PITCH_ENV_AMT = 109
WAYV_OSC2_UNISON_VOICES = 110
WAYV_OSC2_UNISON_SPREAD = 111
WAYV_LFO_AMOUNT = 112
WAYV_OSC3_TYPE = 113
WAYV_OSC3_PITCH = 114
WAYV_OSC3_TUNE = 115
WAYV_OSC3_VOLUME = 116
WAYV_OSC3_UNISON_VOICES = 117
WAYV_OSC3_UNISON_SPREAD = 118
WAYV_OSC1_FM1 = 119
WAYV_OSC1_FM2 = 120
WAYV_OSC1_FM3 = 121
WAYV_OSC2_FM1 = 122
WAYV_OSC2_FM2 = 123
WAYV_OSC2_FM3 = 124
WAYV_OSC3_FM1 = 125
WAYV_OSC3_FM2 = 126
WAYV_OSC3_FM3 = 127
WAYV_ATTACK3 = 128
WAYV_DECAY3 = 129
WAYV_SUSTAIN3 = 130
WAYV_RELEASE3 = 131
WAYV_ADSR3_CHECKBOX = 132

WAVV_PFXMATRIX_GRP0DST0SRC4CTRL0 = 133
WAVV_PFXMATRIX_GRP0DST0SRC4CTRL1 = 134
WAVV_PFXMATRIX_GRP0DST0SRC4CTRL2 = 135
WAVV_PFXMATRIX_GRP0DST1SRC4CTRL0 = 136
WAVV_PFXMATRIX_GRP0DST1SRC4CTRL1 = 137
WAVV_PFXMATRIX_GRP0DST1SRC4CTRL2 = 138
WAVV_PFXMATRIX_GRP0DST2SRC4CTRL0 = 139
WAVV_PFXMATRIX_GRP0DST2SRC4CTRL1 = 140
WAVV_PFXMATRIX_GRP0DST2SRC4CTRL2 = 141
WAVV_PFXMATRIX_GRP0DST3SRC4CTRL0 = 142
WAVV_PFXMATRIX_GRP0DST3SRC4CTRL1 = 143
WAVV_PFXMATRIX_GRP0DST3SRC4CTRL2 = 144

WAVV_PFXMATRIX_GRP0DST0SRC5CTRL0 = 145
WAVV_PFXMATRIX_GRP0DST0SRC5CTRL1 = 146
WAVV_PFXMATRIX_GRP0DST0SRC5CTRL2 = 147
WAVV_PFXMATRIX_GRP0DST1SRC5CTRL0 = 148
WAVV_PFXMATRIX_GRP0DST1SRC5CTRL1 = 149
WAVV_PFXMATRIX_GRP0DST1SRC5CTRL2 = 150
WAVV_PFXMATRIX_GRP0DST2SRC5CTRL0 = 151
WAVV_PFXMATRIX_GRP0DST2SRC5CTRL1 = 152
WAVV_PFXMATRIX_GRP0DST2SRC5CTRL2 = 153
WAVV_PFXMATRIX_GRP0DST3SRC5CTRL0 = 154
WAVV_PFXMATRIX_GRP0DST3SRC5CTRL1 = 155
WAVV_PFXMATRIX_GRP0DST3SRC5CTRL2 = 156
WAYV_PERC_ENV_TIME1 = 157
WAYV_PERC_ENV_PITCH1 = 158
WAYV_PERC_ENV_TIME2 = 159
WAYV_PERC_ENV_PITCH2 = 160
WAYV_PERC_ENV_ON = 161
WAYV_RAMP_CURVE = 162
WAYV_MONO_MODE = 163

WAYV_OSC4_TYPE = 164
WAYV_OSC4_PITCH = 165
WAYV_OSC4_TUNE = 166
WAYV_OSC4_VOLUME = 167
WAYV_OSC4_UNISON_VOICES = 168
WAYV_OSC4_UNISON_SPREAD = 169
WAYV_OSC1_FM4 = 170
WAYV_OSC2_FM4 = 171
WAYV_OSC3_FM4 = 172
WAYV_OSC4_FM1 = 173
WAYV_OSC4_FM2 = 174
WAYV_OSC4_FM3 = 175
WAYV_OSC4_FM4 = 176
WAYV_ATTACK4 = 177
WAYV_DECAY4 =  178
WAYV_SUSTAIN4 = 179
WAYV_RELEASE4 = 180
WAYV_ADSR4_CHECKBOX = 181

WAYV_FM_MACRO1 = 182
WAYV_FM_MACRO1_OSC1_FM1 = 183
WAYV_FM_MACRO1_OSC1_FM2 = 184
WAYV_FM_MACRO1_OSC1_FM3 = 185
WAYV_FM_MACRO1_OSC1_FM4 = 186
WAYV_FM_MACRO1_OSC2_FM1 = 187
WAYV_FM_MACRO1_OSC2_FM2 = 188
WAYV_FM_MACRO1_OSC2_FM3 = 189
WAYV_FM_MACRO1_OSC2_FM4 = 190
WAYV_FM_MACRO1_OSC3_FM1 = 191
WAYV_FM_MACRO1_OSC3_FM2 = 192
WAYV_FM_MACRO1_OSC3_FM3 = 193
WAYV_FM_MACRO1_OSC3_FM4 = 194
WAYV_FM_MACRO1_OSC4_FM1 = 195
WAYV_FM_MACRO1_OSC4_FM2 = 196
WAYV_FM_MACRO1_OSC4_FM3 = 197
WAYV_FM_MACRO1_OSC4_FM4 = 198

WAYV_FM_MACRO2 = 199
WAYV_FM_MACRO2_OSC1_FM1 = 200
WAYV_FM_MACRO2_OSC1_FM2 = 201
WAYV_FM_MACRO2_OSC1_FM3 = 202
WAYV_FM_MACRO2_OSC1_FM4 = 203
WAYV_FM_MACRO2_OSC2_FM1 = 204
WAYV_FM_MACRO2_OSC2_FM2 = 205
WAYV_FM_MACRO2_OSC2_FM3 = 206
WAYV_FM_MACRO2_OSC2_FM4 = 207
WAYV_FM_MACRO2_OSC3_FM1 = 208
WAYV_FM_MACRO2_OSC3_FM2 = 209
WAYV_FM_MACRO2_OSC3_FM3 = 210
WAYV_FM_MACRO2_OSC3_FM4 = 211
WAYV_FM_MACRO2_OSC4_FM1 = 212
WAYV_FM_MACRO2_OSC4_FM2 = 213
WAYV_FM_MACRO2_OSC4_FM3 = 214
WAYV_FM_MACRO2_OSC4_FM4 = 215

WAYV_LFO_PHASE = 216

WAYV_FM_MACRO1_OSC1_VOL = 217
WAYV_FM_MACRO1_OSC2_VOL = 218
WAYV_FM_MACRO1_OSC3_VOL = 219
WAYV_FM_MACRO1_OSC4_VOL = 220

WAYV_FM_MACRO2_OSC1_VOL = 221
WAYV_FM_MACRO2_OSC2_VOL = 222
WAYV_FM_MACRO2_OSC3_VOL = 223
WAYV_FM_MACRO2_OSC4_VOL = 224
WAYV_LFO_PITCH_FINE = 225
WAYV_ADSR_PREFX = 226

WAYV_ADSR1_DELAY = 227
WAYV_ADSR2_DELAY = 228
WAYV_ADSR3_DELAY = 229
WAYV_ADSR4_DELAY = 230

WAYV_ADSR1_HOLD = 231
WAYV_ADSR2_HOLD = 232
WAYV_ADSR3_HOLD = 233
WAYV_ADSR4_HOLD = 234

WAYV_PFX_ADSR_DELAY = 235
WAYV_PFX_ADSR_F_DELAY = 236
WAYV_PFX_ADSR_HOLD = 237
WAYV_PFX_ADSR_F_HOLD = 238
WAYV_HOLD_MAIN  = 239

WAYV_DELAY_NOISE = 240
WAYV_ATTACK_NOISE = 241
WAYV_HOLD_NOISE = 242
WAYV_DECAY_NOISE = 243
WAYV_SUSTAIN_NOISE = 244
WAYV_RELEASE_NOISE = 245
WAYV_ADSR_NOISE_ON = 246

WAYV_DELAY_LFO = 247
WAYV_ATTACK_LFO = 248
WAYV_HOLD_LFO = 249
WAYV_DECAY_LFO = 250
WAYV_SUSTAIN_LFO = 251
WAYV_RELEASE_LFO = 252
WAYV_ADSR_LFO_ON = 253


WAYV_OSC5_TYPE = 254
WAYV_OSC5_PITCH = 255
WAYV_OSC5_TUNE = 256
WAYV_OSC5_VOLUME = 257
WAYV_OSC5_UNISON_VOICES = 258
WAYV_OSC5_UNISON_SPREAD = 259
WAYV_OSC1_FM5 = 260
WAYV_OSC2_FM5 = 261
WAYV_OSC3_FM5 = 262
WAYV_OSC4_FM5 = 263
WAYV_OSC5_FM5 = 264
WAYV_OSC6_FM5 = 265
WAYV_ADSR5_DELAY = 266
WAYV_ATTACK5 = 267
WAYV_ADSR5_HOLD = 268
WAYV_DECAY5 = 269
WAYV_SUSTAIN5 = 270
WAYV_RELEASE5 = 271
WAYV_ADSR5_CHECKBOX = 272

WAYV_OSC6_TYPE = 273
WAYV_OSC6_PITCH = 274
WAYV_OSC6_TUNE = 275
WAYV_OSC6_VOLUME = 276
WAYV_OSC6_UNISON_VOICES = 277
WAYV_OSC6_UNISON_SPREAD = 278
WAYV_OSC1_FM6 = 279
WAYV_OSC2_FM6 = 280
WAYV_OSC3_FM6 = 281
WAYV_OSC4_FM6 = 282
WAYV_OSC5_FM6 = 283
WAYV_OSC6_FM6 = 284
WAYV_ADSR6_DELAY = 285
WAYV_ATTACK6 = 286
WAYV_ADSR6_HOLD = 287
WAYV_DECAY6 = 288
WAYV_SUSTAIN6 = 289
WAYV_RELEASE6 = 290
WAYV_ADSR6_CHECKBOX = 291


WAYV_FM_MACRO1_OSC1_FM5 = 292
WAYV_FM_MACRO1_OSC2_FM5 = 293
WAYV_FM_MACRO1_OSC3_FM5 = 294
WAYV_FM_MACRO1_OSC4_FM5 = 295
WAYV_FM_MACRO1_OSC5_FM5 = 296
WAYV_FM_MACRO1_OSC6_FM5 = 297

WAYV_FM_MACRO1_OSC1_FM6 = 298
WAYV_FM_MACRO1_OSC2_FM6 = 299
WAYV_FM_MACRO1_OSC3_FM6 = 300
WAYV_FM_MACRO1_OSC4_FM6 = 301
WAYV_FM_MACRO1_OSC5_FM6 = 302
WAYV_FM_MACRO1_OSC6_FM6 = 303

WAYV_FM_MACRO1_OSC5_FM1 = 304
WAYV_FM_MACRO1_OSC5_FM2 = 305
WAYV_FM_MACRO1_OSC5_FM3 = 306
WAYV_FM_MACRO1_OSC5_FM4 = 307

WAYV_FM_MACRO1_OSC6_FM1 = 308
WAYV_FM_MACRO1_OSC6_FM2 = 309
WAYV_FM_MACRO1_OSC6_FM3 = 310
WAYV_FM_MACRO1_OSC6_FM4 = 311

WAYV_FM_MACRO1_OSC5_VOL = 312
WAYV_FM_MACRO1_OSC6_VOL = 313

WAYV_FM_MACRO2_OSC1_FM5 = 314
WAYV_FM_MACRO2_OSC2_FM5 = 315
WAYV_FM_MACRO2_OSC3_FM5 = 316
WAYV_FM_MACRO2_OSC4_FM5 = 317
WAYV_FM_MACRO2_OSC5_FM5 = 318
WAYV_FM_MACRO2_OSC6_FM5 = 319

WAYV_FM_MACRO2_OSC1_FM6 = 320
WAYV_FM_MACRO2_OSC2_FM6 = 321
WAYV_FM_MACRO2_OSC3_FM6 = 322
WAYV_FM_MACRO2_OSC4_FM6 = 323
WAYV_FM_MACRO2_OSC5_FM6 = 324
WAYV_FM_MACRO2_OSC6_FM6 = 325

WAYV_FM_MACRO2_OSC5_FM1 = 326
WAYV_FM_MACRO2_OSC5_FM2 = 327
WAYV_FM_MACRO2_OSC5_FM3 = 328
WAYV_FM_MACRO2_OSC5_FM4 = 329

WAYV_FM_MACRO2_OSC6_FM1 = 330
WAYV_FM_MACRO2_OSC6_FM2 = 331
WAYV_FM_MACRO2_OSC6_FM3 = 332
WAYV_FM_MACRO2_OSC6_FM4 = 333

WAYV_FM_MACRO2_OSC5_VOL = 334
WAYV_FM_MACRO2_OSC6_VOL = 335

WAYV_OSC5_FM1 = 336
WAYV_OSC5_FM2 = 337
WAYV_OSC5_FM3 = 338
WAYV_OSC5_FM4 = 339

WAYV_OSC6_FM1 = 340
WAYV_OSC6_FM2 = 341
WAYV_OSC6_FM3 = 342
WAYV_OSC6_FM4 = 343
WAYV_NOISE_PREFX = 344

WAVV_PFXMATRIX_GRP0DST0SRC6CTRL0 = 345
WAVV_PFXMATRIX_GRP0DST0SRC6CTRL1 = 346
WAVV_PFXMATRIX_GRP0DST0SRC6CTRL2 = 347
WAVV_PFXMATRIX_GRP0DST1SRC6CTRL0 = 348
WAVV_PFXMATRIX_GRP0DST1SRC6CTRL1 = 349
WAVV_PFXMATRIX_GRP0DST1SRC6CTRL2 = 350
WAVV_PFXMATRIX_GRP0DST2SRC6CTRL0 = 351
WAVV_PFXMATRIX_GRP0DST2SRC6CTRL1 = 352
WAVV_PFXMATRIX_GRP0DST2SRC6CTRL2 = 353
WAVV_PFXMATRIX_GRP0DST3SRC6CTRL0 = 354
WAVV_PFXMATRIX_GRP0DST3SRC6CTRL1 = 355
WAVV_PFXMATRIX_GRP0DST3SRC6CTRL2 = 356

WAVV_PFXMATRIX_GRP0DST0SRC7CTRL0 = 357
WAVV_PFXMATRIX_GRP0DST0SRC7CTRL1 = 358
WAVV_PFXMATRIX_GRP0DST0SRC7CTRL2 = 359
WAVV_PFXMATRIX_GRP0DST1SRC7CTRL0 = 360
WAVV_PFXMATRIX_GRP0DST1SRC7CTRL1 = 361
WAVV_PFXMATRIX_GRP0DST1SRC7CTRL2 = 362
WAVV_PFXMATRIX_GRP0DST2SRC7CTRL0 = 363
WAVV_PFXMATRIX_GRP0DST2SRC7CTRL1 = 364
WAVV_PFXMATRIX_GRP0DST2SRC7CTRL2 = 365
WAVV_PFXMATRIX_GRP0DST3SRC7CTRL0 = 366
WAVV_PFXMATRIX_GRP0DST3SRC7CTRL1 = 367
WAVV_PFXMATRIX_GRP0DST3SRC7CTRL2 = 368

WAYV_MIN_NOTE = 369
WAYV_MAX_NOTE = 370

#Ray-V

RAYV_OUTPUT0 = 0
RAYV_OUTPUT1 = 1
RAYV_FIRST_CONTROL_PORT = 2
RAYV_ATTACK = 2
RAYV_DECAY = 3
RAYV_SUSTAIN = 4
RAYV_RELEASE = 5
RAYV_TIMBRE = 6
RAYV_RES = 7
RAYV_DIST = 8
RAYV_FILTER_ATTACK = 9
RAYV_FILTER_DECAY = 10
RAYV_FILTER_SUSTAIN = 11
RAYV_FILTER_RELEASE = 12
RAYV_NOISE_AMP = 13
RAYV_FILTER_ENV_AMT = 14
RAYV_DIST_WET = 15
RAYV_OSC1_TYPE = 16
RAYV_OSC1_PITCH = 17
RAYV_OSC1_TUNE = 18
RAYV_OSC1_VOLUME = 19
RAYV_OSC2_TYPE = 20
RAYV_OSC2_PITCH = 21
RAYV_OSC2_TUNE = 22
RAYV_OSC2_VOLUME = 23
RAYV_MASTER_VOLUME = 24
RAYV_MASTER_UNISON_VOICES = 25
RAYV_MASTER_UNISON_SPREAD = 26
RAYV_MASTER_GLIDE = 27
RAYV_MASTER_PITCHBEND_AMT = 28
RAYV_PITCH_ENV_TIME = 29
RAYV_PITCH_ENV_AMT = 30
RAYV_LFO_FREQ = 31
RAYV_LFO_TYPE = 32
RAYV_LFO_AMP = 33
RAYV_LFO_PITCH = 34
RAYV_LFO_FILTER = 35
RAYV_OSC_HARD_SYNC = 36
RAYV_RAMP_CURVE = 37
RAYV_FILTER_KEYTRK = 38
RAYV_MONO_MODE = 39
RAYV_LFO_PHASE = 40
RAYV_LFO_PITCH_FINE = 41
RAYV_ADSR_PREFX = 42
RAYV_MIN_NOTE = 43
RAYV_MAX_NOTE = 44

#Port maps


# TODO at PyDAWv5:
# Remove those which don't really make sense to automate

WAYV_PORT_MAP = {
    "Master Attack": WAYV_ATTACK_MAIN,
    "Master Hold": WAYV_HOLD_MAIN,
    "Master Decay": WAYV_DECAY_MAIN,
    "Master Sustain": WAYV_SUSTAIN_MAIN,
    "Master Release": WAYV_RELEASE_MAIN,
    "Noise Amp": WAYV_OSC1_TYPE,
    "Master Glide": 18,
    "Osc1 Attack": WAYV_ATTACK1,
    "Osc1 Decay": WAYV_DECAY1,
    "Osc1 Sustain": WAYV_SUSTAIN1,
    "Osc1 Release": WAYV_RELEASE1,
    "Osc2 Attack": WAYV_ATTACK2,
    "Osc2 Decay": WAYV_DECAY2,
    "Osc2 Sustain": WAYV_SUSTAIN2,
    "Osc2 Release": WAYV_RELEASE2,
    "PFX ADSR1 Attack": 28,
    "PFX ADSR1 Decay": 29,
    "PFX ADSR1 Sustain": "30",
    "PFX ADSR1 Release": "31",
    "PFX ADSR2 Attack": "32",
    "PFX ADSR2 Decay": "33",
    "PFX ADSR2 Sustain": "34",
    "PFX ADSR2 Release": "35",
    "Pitch Env Time": "37",
    "LFO Freq": "38",
    "FX0 Knob0": "40",
    "FX0 Knob1": "41",
    "FX0 Knob2": "42",
    "FX1 Knob0": "44",
    "FX1 Knob1": "45",
    "FX1 Knob2": "46",
    "FX2 Knob0": "48",
    "FX2 Knob1": "49",
    "FX2 Knob2": "50",
    "FX3 Knob0": "52",
    "FX3 Knob1": "53",
    "FX3 Knob2": "54",
    "LFO Amp": "107",
    "LFO Pitch": "108",
    "LFO Pitch Fine": WAYV_LFO_PITCH_FINE,
    "Pitch Env Amt": "109",
    "LFO Amount": "112",
    "Osc1 FM1": WAYV_OSC1_FM1,
    "Osc1 FM2": WAYV_OSC1_FM2,
    "Osc1 FM3": WAYV_OSC1_FM3,
    "Osc1 FM4": WAYV_OSC1_FM4,
    "Osc1 FM5": WAYV_OSC1_FM5,
    "Osc1 FM6": WAYV_OSC1_FM6,
    "Osc2 FM1": WAYV_OSC2_FM1,
    "Osc2 FM2": WAYV_OSC2_FM2,
    "Osc2 FM3": WAYV_OSC2_FM3,
    "Osc2 FM4": WAYV_OSC2_FM4,
    "Osc2 FM5": WAYV_OSC2_FM5,
    "Osc2 FM6": WAYV_OSC2_FM6,
    "Osc3 FM1": WAYV_OSC3_FM1,
    "Osc3 FM2": WAYV_OSC3_FM2,
    "Osc3 FM3": WAYV_OSC3_FM3,
    "Osc3 FM4": WAYV_OSC3_FM4,
    "Osc3 FM5": WAYV_OSC3_FM5,
    "Osc3 FM6": WAYV_OSC3_FM6,
    "Osc4 FM1": WAYV_OSC4_FM1,
    "Osc4 FM2": WAYV_OSC4_FM2,
    "Osc4 FM3": WAYV_OSC4_FM3,
    "Osc4 FM4": WAYV_OSC4_FM4,
    "Osc4 FM5": WAYV_OSC4_FM5,
    "Osc4 FM6": WAYV_OSC4_FM6,
    "Osc5 FM1": WAYV_OSC5_FM1,
    "Osc5 FM2": WAYV_OSC5_FM2,
    "Osc5 FM3": WAYV_OSC5_FM3,
    "Osc5 FM4": WAYV_OSC5_FM4,
    "Osc5 FM5": WAYV_OSC5_FM5,
    "Osc5 FM6": WAYV_OSC5_FM6,
    "Osc6 FM1": WAYV_OSC6_FM1,
    "Osc6 FM2": WAYV_OSC6_FM2,
    "Osc6 FM3": WAYV_OSC6_FM3,
    "Osc6 FM4": WAYV_OSC6_FM4,
    "Osc6 FM5": WAYV_OSC6_FM5,
    "Osc6 FM6": WAYV_OSC6_FM6,
    "Osc3 Attack": WAYV_ATTACK3,
    "Osc3 Decay": WAYV_DECAY3,
    "Osc3 Sustain": WAYV_SUSTAIN3,
    "Osc3 Release": WAYV_RELEASE3,
    "FM Macro 1": WAYV_FM_MACRO1,
    "FM Macro 2": WAYV_FM_MACRO2,
    "Osc4 Attack": WAYV_ATTACK4,
    "Osc4 Decay": WAYV_DECAY4,
    "Osc4 Sustain": WAYV_SUSTAIN4,
    "Osc4 Release": WAYV_RELEASE4,
    "Osc5 Attack": WAYV_ATTACK5,
    "Osc5 Decay": WAYV_DECAY5,
    "Osc5 Sustain": WAYV_SUSTAIN5,
    "Osc5 Release": WAYV_RELEASE5,
    "Osc6 Attack": WAYV_ATTACK6,
    "Osc6 Decay": WAYV_DECAY6,
    "Osc6 Sustain": WAYV_SUSTAIN6,
    "Osc6 Release": WAYV_RELEASE6,
    "Osc1 Delay": WAYV_ADSR1_DELAY,
    "Osc2 Delay": WAYV_ADSR2_DELAY,
    "Osc3 Delay": WAYV_ADSR3_DELAY,
    "Osc4 Delay": WAYV_ADSR4_DELAY,
    "Osc5 Delay": WAYV_ADSR5_DELAY,
    "Osc6 Delay": WAYV_ADSR6_DELAY,
    "Osc1 Hold": WAYV_ADSR1_HOLD,
    "Osc2 Hold": WAYV_ADSR2_HOLD,
    "Osc3 Hold": WAYV_ADSR3_HOLD,
    "Osc4 Hold": WAYV_ADSR4_HOLD,
    "Osc5 Hold": WAYV_ADSR5_HOLD,
    "Osc6 Hold": WAYV_ADSR6_HOLD,
}

RAYV_PORT_MAP = {
    "Attack": "2",
    "Decay": "3",
    "Sustain": "4",
    "Release": "5",
    "Filter Cutoff": "6",
    "Res": "7",
    "Dist": "8",
    "Attack Filter": "9",
    "Decay Filter": "10",
    "Sustain Filter": "11",
    "Release Filter": "12",
    "Noise Amp": "13",
    "Filter Env Amt": "14",
    "Dist Wet": "15",
    "Master Glide": "27",
    "Pitch Env Time": "29",
    "Pitch Env Amt": "30",
    "LFO Freq": "31",
    "LFO Amp": "33",
    "LFO Pitch": "34",
    "LFO Pitch Fine": RAYV_LFO_PITCH_FINE,
    "LFO Filter": "35"
}


MODULEX_PORT_MAP = {
    "FX0 Knob0": "4",
    "FX0 Knob1": "5",
    "FX0 Knob2": "6",
    "FX1 Knob0": "8",
    "FX1 Knob1": "9",
    "FX1 Knob2": "10",
    "FX2 Knob0": "12",
    "FX2 Knob1": "13",
    "FX2 Knob2": "14",
    "FX3 Knob0": "16",
    "FX3 Knob1": "17",
    "FX3 Knob2": "18",
    "FX4 Knob0": "20",
    "FX4 Knob1": "21",
    "FX4 Knob2": "22",
    "FX5 Knob0": "24",
    "FX5 Knob1": "25",
    "FX5 Knob2": "26",
    "FX6 Knob0": "28",
    "FX6 Knob1": "29",
    "FX6 Knob2": "30",
    "FX7 Knob0": "32",
    "FX7 Knob1": "33",
    "FX7 Knob2": "34",
    "Delay Feedback": "37",
    "Delay Dry": "38",
    "Delay Wet": "39",
    "Delay Duck": "40",
    "Delay LP Cutoff": "41",
    "Volume Slider": "43",
    "Reverb Wet": "45",
    "Reverb Dry": MODULEX_REVERB_DRY,
    "Reverb Color": "46",
    "Gate Wet": MODULEX_GATE_WET,
    "Glitch Time": MODULEX_GLITCH_TIME
}

EUPHORIA_PORT_MAP = {
    "Master Attack": "3",
    "Master Decay": "4",
    "Master Sustain": "5",
    "Master Release": "6",
    "ADSR2 Attack": "7",
    "ADSR2 Decay": "8",
    "ADSR2 Sustain": "9",
    "ADSR2 Release": "10",
    "LFO Pitch": "11",
    "LFO Pitch Fine": EUPHORIA_LFO_PITCH_FINE,
    "Master Glide": "13",
    "Pitch Env Time": "15",
    "LFO Freq": "16",
    "FX0 Knob0": "18",
    "FX0 Knob1": "19",
    "FX0 Knob2": "20",
    "FX1 Knob0": "22",
    "FX1 Knob1": "23",
    "FX1 Knob2": "24",
    "FX2 Knob0": "26",
    "FX2 Knob1": "27",
    "FX2 Knob2": "28",
    "FX3 Knob0": "30",
    "FX3 Knob1": "31",
    "FX3 Knob2": "32",
    #This one is kept for compatibility because it was once in here incorrectly
    #TODO:  Delete at PyDAWv5
    "zzDeprecated ignore": "83",
}

_euphoria_port_mins = (EUPHORIA_MONO_FX0_KNOB0_PORT_RANGE_MIN,
                       EUPHORIA_MONO_FX1_KNOB0_PORT_RANGE_MIN,
                       EUPHORIA_MONO_FX2_KNOB0_PORT_RANGE_MIN,
                       EUPHORIA_MONO_FX3_KNOB0_PORT_RANGE_MIN)

for f_fx in range(4):
    f_port_iter = _euphoria_port_mins[f_fx]
    for f_knob in range(3):
        for f_group in range(1, EUPHORIA_MAX_SAMPLE_COUNT + 1):
            f_group_str = str(f_group).zfill(3)
            f_label = "Mono FX{} Knob{} Group {}".format(f_fx, f_knob, f_group_str)
            EUPHORIA_PORT_MAP[f_label] = f_port_iter
            f_port_iter += 1
