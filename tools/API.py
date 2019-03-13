# -*- coding: utf-8 -*-
'''
+-----------------------------------------------------------------------+
|Author: Cheng Wenfeng <277546922@qq.com>                               |
+-----------------------------------------------------------------------+
'''
import os,sys
pro_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append('%s/../libs' % pro_path)

import Global as gl
#定义初始目录
gl._init()
gl.set_value('wkdir','%s/../' % pro_path)
gl.set_value('confdir','%s/../config' % pro_path)
gl.set_value('certdir','%s/../certs' % pro_path)
gl.set_value('plgdir','%s/../plugins' % pro_path)
gl.set_value('tempdir','%s/../template' % pro_path)
gl.set_value('assets','%s/../assets' % pro_path)
gl.set_value('vwdir','%s/../views' % pro_path)
gl.set_value('logs','%s/../logs' % pro_path)

from Functions import getAPIData,netModule,wrtlog
netmod=netModule()
API=getAPIData()

if __name__ == '__main__' :
   if sys.argv[1] == 'API' and sys.argv[2] == 'getUserLineID':
      print API.getUserLineID(sys.argv[3])
   elif sys.argv[1] == 'API' and sys.argv[2] == 'wrtvpnlogin':
      print wrtlog(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
   elif sys.argv[1] == 'API' and sys.argv[2] == 'getgw':
      print netmod.getIfGW(sys.argv[3])
   elif sys.argv[1] == 'API' and sys.argv[2] == 'getniaddr':
      print netmod.getNiaddr(sys.argv[3])
   elif sys.argv[1] == 'API' and sys.argv[2] == 'getnetip':
      print netmod.NetIP()
   else:
      sys.exit()
