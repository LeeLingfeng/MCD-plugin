# -*- coding: utf-8 -*-

from savelib import mcsave
import time

helpmsg = '''
wtf is this shit
'''

autoBackupEnabled = False
autoBackupInterval = 24 #in hours
skipIfSave = True
savepath = './savelib'
makebackup = mcsave(savepath)
times = 5

def onServerStartup(server):
  while autoBackupEnabled:
    time.sleep(autoBackupInterval * 3600)
    if not hasSaved:
      hasSaved = False


def onServerInfo(server, info):
  if (info.isPlayer == 1) and (info.content.startswith('!!bp')):
    args = info.content.split(' ')
    if (len(args) == 1):
      a = times
      while a > 0:
        server.say('服务器' + str(a) + '秒后开始备份')
        time.sleep(1)
        a -= 1
      server.say('开始备份')
      meta = makebackup.backup()
      if meta == {}:
        server.say('备份失败')
      else :
        server.say('备份成功')
        makebackup.writeMeta(meta)
    elif (len(args) == 2) and (args[1]=='help'):
      for line in helpmsg.splitlines():
        server.tell(info.player, line)