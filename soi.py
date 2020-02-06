# -*- coding: utf-8 -*-

from time import sleep


def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!re'):
      whitelist = []
      with open('./plugins/pget/whitelist.json') as handle:
        for line in handle.readlines():
          whitelist.append(line.replace('\n','').replace('\r',''))
      if info.player in whitelist:
        server.stop()
        sleep(10)
        server.start()
      else:
        server.say('Permission denied')
    elif info.content.startswith('!!ed'):
      whitelist = []
      with open('./plugins/pget/whitelist.json') as handle:
        for line in handle.readlines():
          whitelist.append(line.replace('\n','').replace('\r',''))
      if info.player in whitelist:
        server.stop()
      else:
        server.say('Permission denied')
