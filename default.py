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
import random
import datetime
import _strptime
import urllib

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
    self._daemon()

  def _init_vars(self):
    self.Player = MyPlayer()
    self.Monitor = MyMonitor()

  def _init_property(self):
    #self.RANDOMITEMS_UPDATE_METHOD = int(__addon__.getSetting("randomitems_method"))
    #self.RECENTITEMS_HOME_UPDATE = __addon__.getSetting("recentitems_homeupdate")
    #self.INPROGRESSITEMS_HOME_UPDATE = __addon__.getSetting("inprogressitems_homeupdate")
    pass

  def _daemon(self):
    while (not xbmc.abortRequested):
      # Do nothing
      xbmc.sleep(600)


class MyMonitor(xbmc.Monitor):
  def __init__(self):
    xbmc.Monitor.__init__(self)
    log('init monitor')

  def onScreensaverActivated(self):
    log('callback: monitor screensaver Activated')

  def onScreensaverDeactivated(self):
    log('callback: monitor screensaver DEactivated')

class MyPlayer(xbmc.Player):
  def __init__(self):
    xbmc.Player.__init__(self)
    log('init player')

  def onPlayBackStarted(self):
    log('callback: player started')

  def onPlayBackEnded(self):
    self.onPlayBackStopped()

  def onPlayBackStopped(self):
    log('callback: player stopped')

if (__name__ == "__main__"):
    log('script version %s started' % __addonversion__)
    Main()
    del MyPlayer
    del MyMonitor
    del Main
    log('script version %s stopped' % __addonversion__)
