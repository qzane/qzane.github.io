---
layout: post
title: Speaker-For-Stardict
---
read and decrypt Chrome Cookies on Windows

# source
https://github.com/qzane/ChromeCookiesReader

# about:nothing
不想背GRE的间歇，写了个在windows下解密ChromeCookies文件的东西
(因为FF是明文存的没什么好写的，IE没用数据库比较奇葩不想研究), 
网上搜了搜有C#版本和powershell的就是找不到Python的你敢信！！！
自己写的过程中发现要用ctypes，第一次接触这货，心理历程如下:
（看Py文档)好像很方便容易的样子->(看MS接口文档)这是一坨啥...->（尝试开始写)XXX
个中滋味真是...不被虐过一遍感受不到，不过好在最后还是调成功了。

# some tools with cookies
Firefox: [Web Developer](https://addons.mozilla.org/en-us/firefox/addon/web-developer/) </br>
Chrome : [Edit This Cookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg) </br>
IE: [IECookiesView](http://www.nirsoft.net/utils/iecookies.html) </br>
ALL: [Fiddler](https://www.telerik.com/download/fiddler) </br>
