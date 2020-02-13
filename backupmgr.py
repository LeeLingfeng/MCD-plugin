# -*- coding: utf-8 -*-

from savelib import mcsave
import time
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

helpmsg = '''
wtf is this shit
'''

autoBackupEnabled = False
autoBackupInterval = 24 #in hours
skipIfSave = True
savepath = './savelib'
worldpath = './server/world'
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
      server.tell(info.player,'输入!!bp help查看帮助')
    elif (len(args) == 2) and (args[1] == 'help'):
      for line in helpmsg.splitlines():
        server.tell(info.player, line)
    elif (len(args) == 3) and (args[1] == 'name'):
      meta = {}
      meta['name'] = args[2]
      a = times
      while a > 0:
        server.say('服务器' + str(a) + '秒后开始备份')
        time.sleep(1)
        a -= 1
      server.say('开始备份')
      meta = makebackup.backup(meta)
      if meta['time'] == " ":
        server.say('备份失败')
      else :
        server.say('备份成功')
        makebackup.writeMeta(meta)
    elif (len(args) == 2) and (args[1] == 'last'):
      meta = makebackup.readMeta()
      lastmsg = '最后一次备份时间是：' + meta['time'] + '，备注为：' + meta['name'] + ' '
      server.tell(info.player,lastmsg)
    elif (len(args) == 2) and (args[1] == 'restore'):
      meta =  makebackup.readMeta()
      if len(meta) == 2:
        server.say('服务器即将还原备注为' + meta['name'] + '的备份')
        a = times
        while a > 0:
          server.say('服务器' + str(a) + '秒后开始还原')
          time.sleep(1)
          a -= 1
        server.say('开始还原')
        server.stop()
        time.sleep (5)
        result = makebackup.restore(meta)
        if result == 0:
          server.start()
      else:
        server.say('备份记录有问题，请检查！')