# -*- coding: utf-8 -*-

import os
import json
import time

worldpath = './server/world'
savepath = './savelib'

class mcsave(object):
  def __init__(self, savepath, meta = {}):
    self.path = savepath
    with open(self.path + '/meta.json', 'w') as handler:
      handler.write(json.dumps(meta))
  
  def backup(self, meta = {}, writeTime = True):
    if writeTime:
      clock = time.strftime('%Y%m%d',time.localtime()) + '-' + time.strftime('%H%M%S',time.localtime())
    targetpath = savepath + '/' + clock
    os.system('mkdir ' + targetpath)
    result = os.system('cp -r ' + worldpath + ' ' + targetpath)
    if result == 0:
      meta['time'] = clock
    return meta

  def readMeta(self):
    with open(self.path + '/meta.json', 'r') as handler:
      return json.loads(handler.read())
  
  def writeMeta(self, meta):
    with open(self.path + '/meta.json', 'w') as handler:
      handler.write(json.dumps(meta))