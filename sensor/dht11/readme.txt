===============================================================================
= ファイル名:
=   BATTERY.BAS
= 作者:
=   HRA!
= ライセンス:
=   MIT
===============================================================================
【詳細】
_IOTGET("dht/humidity",H)
_IOTGET("dht/temperature",T)

これで変数Hには湿度、変数Tには温度が返ってくるらしい。

ただし試作機と一緒に配られた Grove Beginner Kit for Arduino の
湿度・温度センサーは使えない。
DHT11 と呼ばれる水色のセンサーを付ける必要があるらしい。

センサーが付いていないと -1 が返ってくるようだ。

DHT11
https://jp.seeedstudio.com/Grove-Temperature-Humidity-Sensor-DHT11.html

私は持っていないので試せていない。
