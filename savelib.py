# -*- coding: utf-8 -*-

import os
import json
import time

worldpath = './server/world'
savepath = './savelib'

class mcsave(object):
  def __init__(self, savepath):
    self.path = savepath
  
  def backup(self, meta = {}, writeTime = True):
    if writeTime:
      clock = time.strftime('%Y%m%d',time.localtime()) + '-' + time.strftime('%H%M%S',time.localtime())
    targetpath = self.path + '/' + clock
    os.system('mkdir ' + targetpath)
    result = os.system('cp -r ' + worldpath + ' ' + targetpath)
    if result == 0:
      meta['time'] = clock
    else:
      meta['time'] = " "
    return meta

  def restore(self, meta):
    targetpath = self.path + '/' + meta['time'] + '/world'
    os.system('rm -rf ' + worldpath)
    result = os.system('cp -r ' + targetpath + ' ' + './server/')
    return result

  def readMeta(self):
    with open(self.path + '/meta.json', 'r') as handler:
      return json.loads(handler.read())
  
  def writeMeta(self, meta):
    with open(self.path + '/meta.json', 'w') as handler:
      handler.write(json.dumps(meta))