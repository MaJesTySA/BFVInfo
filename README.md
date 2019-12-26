# BFVInfo WeChat App
微信战地5战绩查询小程序，目前已经上线。微信搜索`BFVInfo`或者扫码即可。

<div align='center'><img src='https://raw.githubusercontent.com/MaJesTySA/BFVInfo/master/imgs/bfvinfo.png' width=50% /></div>

数据是从[BF Tracker](https://battlefieldtracker.com/)爬的，提取了一部分。暂时还未考虑过多请求，导致被`BF Tracker`BAN IP的情况，加入IP池的话，速度会很慢。

前端基于微信API，没怎么做（主要是`css`不太会）。后端用的`flask`，毕竟轻量。

因为微信要求请求地址必须备案，而`BF Tracker`是国外网站，所以不得不用后端来请求，不然直接用前端`js`处理数据即可。

<div align='center'><img src='https://raw.githubusercontent.com/MaJesTySA/BFVInfo/master/imgs/1.jpg' width=30% /></div>

<div align='center'><img src='https://raw.githubusercontent.com/MaJesTySA/BFVInfo/master/imgs/2.jpg' width=30% /></div>

<div align='center'><img src='https://raw.githubusercontent.com/MaJesTySA/BFVInfo/master/imgs/3.jpg' width=30% /></div>

<div align='center'><img src='https://raw.githubusercontent.com/MaJesTySA/BFVInfo/master/imgs/4.jpg' width=30% /></div>

