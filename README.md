# MCD-plugin
一些自己写的MCDaemon的插件，以及为了满足自己需求改写的插件
# 相关链接
[MCDaemon](https://github.com/kafuuchino-desu/MCDaemon)

[MCD插件](https://github.com/TISUnion)
# 插件说明
## soi.py
重启或者关闭服务器的插件
### 指令
!!re 重启服务器

!!ed 关闭服务器
### 注意
指令必须白名单中的玩家才可以使用，与pget插件共用同一个白名单
## savelib.py
[原插件地址](https://github.com/TISUnion/savelib)

为适应自己进行些改写

使用标签记得创建./savelib/meta.json文件
## backupmgr.py
[原插件地址](https://github.com/TISUnion/backupMgr)

对插件进行补全，满足基本需求
### 指令
!!bp name 名字

备份并备注“名字”

!!bp last

查看最近一次备份

!!bp restore

还原
