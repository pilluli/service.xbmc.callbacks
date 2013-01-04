#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2012 Team-XBMC
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#    This script is based on script.randomitems & script.wacthlist
#    Thanks to their original authors

import os
import sys
import xbmc
import xbmcgui
import xbmcaddon
import subprocess

script_xbmc_starts = ''
script_player_starts = ''
script_player_stops = ''
script_screensaver_starts = ''
script_screensaver_stops = ''

__addon__        = xbmcaddon.Addon()
__addonversion__ = __addon__.getAddonInfo('version')
__addonid__      = __addon__.getAddonInfo('id')
__addonname__    = __addon__.getAddonInfo('name')

def log(txt):
    message = '%s: %s' % (__addonname__, txt.encode('ascii', 'ignore'))
    xbmc.log(msg=message, level=xbmc.LOGDEBUG)

class Main:
  def __init__(self):
    self._init_vars()
    self._init_property()
    global script_xbmc_starts
    if script_xbmc_starts:
      log('Going to execute script = "' + script_xbmc_starts + '"')
      subprocess.Popen([script_xbmc_starts])
    self._daemon()

  def _init_vars(self):
    self.Player = MyPlayer()
    self.Monitor = MyMonitor(update_settings = self._init_property)

  def _init_property(self):
    log('Reading properties')
    global script_xbmc_starts
    global script_player_starts
    global script_player_stops
    global script_screensaver_starts
    global script_screensaver_stops
    script_xbmc_starts = xbmc.translatePath(__addon__.getSetting("xbmc_starts"))
    script_player_starts = xbmc.translatePath(__addon__.getSetting("player_starts"))
    script_player_stops = xbmc.translatePath(__addon__.getSetting("player_stops"))
    script_screensaver_starts = xbmc.translatePath(__addon__.getSetting("screensaver_starts"))
    script_screensaver_stops = xbmc.translatePath(__addon__.getSetting("screensaver_stops"))
    log('script xbmc starts = "' + script_xbmc_starts + '"')
    log('script player starts = "' + script_player_starts + '"')
    log('script player stops = "' + script_player_stops + '"')
    log('script screensaver starts = "' + script_screensaver_starts + '"')
    log('script screensaver stops = "' + script_screensaver_stops + '"')

  def _daemon(self):
    while (not xbmc.abortRequested):
      # Do nothing
      xbmc.sleep(600)
    log('abort requested')


class MyMonitor(xbmc.Monitor):
  def __init__(self, *args, **kwargs):
    xbmc.Monitor.__init__(self)
    self.update_settings = kwargs['update_settings']

  def onSettingsChanged(self):
    self.update_settings()

  def onScreensaverActivated(self):
    log('screensaver starts')
    global script_screensaver_starts
    if script_screensaver_starts:
      log('Going to execute script = "' + script_screensaver_starts + '"')
      subprocess.Popen([script_screensaver_starts])

  def onScreensaverDeactivated(self):
    log('screensaver stops')
    global script_screensaver_stops
    if script_screensaver_stops:
      log('Going to execute script = "' + script_screensaver_stops + '"')
      subprocess.Popen([script_screensaver_stops])

class MyPlayer(xbmc.Player):
  def __init__(self):
    xbmc.Player.__init__(self)

  def onPlayBackStarted(self):
    log('player starts')
    global script_player_starts
    if script_player_starts:
      log('Going to execute script = "' + script_player_starts + '"')
      subprocess.Popen([script_player_starts])

  def onPlayBackEnded(self):
    self.onPlayBackStopped()

  def onPlayBackStopped(self):
    log('player stops')
    global script_player_stops
    if script_player_stops:
      log('Going to execute script = "' + script_player_stops + '"')
      subprocess.Popen([script_player_stops])

if (__name__ == "__main__"):
    log('script version %s started' % __addonversion__)
    Main()
    del MyPlayer
    del MyMonitor
    del Main
    log('script version %s stopped' % __addonversion__)
