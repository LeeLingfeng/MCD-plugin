# -*- coding: utf-8 -*-

from time import sleep

times = 5

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!re'):
      whitelist = []
      with open('./plugins/pget/whitelist.json') as handle:
        for line in handle.readlines():
          whitelist.append(line.replace('\n','').replace('\r',''))
      if info.player in whitelist:
        a = times
        while a > 0:
          server.say('服务器' + str(a) + '秒后重启')
          sleep(1)
          a -= 1
        server.say('服务器重启')
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
        a = times
        while a > 0:
          server.say('服务器' + str(a) + '秒后关闭')
          sleep(1)
          a -= 1
        server.say('服务器关闭')
        server.stop()
      else:
        server.say('Permission denied')
