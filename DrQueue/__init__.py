# -*- coding: utf-8 -*-

"""DrQueue module"""

import platform
from client import Client
from job import Job


def get_rendertemplate(renderer):
    """Return template filename from renderer name"""
    filename = ""
    if renderer == '3delight':
        filename = '3delight_sg.py'
    if renderer == '3dsmax':
        filename = '3dsmax_sg.py'
    if renderer == 'aftereffects':
        filename = 'aftereffects_sg.py'
    if renderer == 'aqsis':
        filename = 'aqsis_sg.py'
    if renderer == 'blender':
        filename = 'blender_sg.py'
    if renderer == 'cinema4d':
        filename = 'cinema4d_sg.py'
    if renderer == 'general':
        filename = 'general_sg.py'
    if renderer == 'lightwave':
        filename = 'lightwave_sg.py'
    if renderer == 'luxrender':
        filename = 'luxrender_sg.py'
    if renderer == 'mantra':
        filename = 'mantra_sg.py'
    if renderer == 'maya':
        filename = 'maya_sg.py'
    if renderer == 'mentalray':
        filename = 'mentalray_sg.py'
    if renderer == 'nuke':
        filename = 'nuke_sg.py'
    if renderer == 'pixie':
        filename = 'pixie_sg.py'
    if renderer == 'shake':
        filename = 'shake_sg.py'
    if renderer == 'terragen':
        filename = 'terragen_sg.py'
    if renderer == 'turtle':
        filename = 'turtle_sg.py'
    if renderer == 'vray':
        filename = 'vray_sg.py'
    if renderer == 'xsi':
        filename = 'xsi_sg.py'
    return filename 


def get_osname():
    """Return operating system name"""
    osname = platform.system()
    if osname == 'Darwin':
        osname = 'OSX'
    return osname


def run_script_with_env(script, env_dict):
    """Create variables and template script on engine"""
    # load variables from dict
    locals().update(env_dict)
    return execfile(script)


def run_dummy():
    import time
    time.sleep(1)
    return True

