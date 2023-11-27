100 DEFINTA-Z
110 SCREEN0:WIDTH40
120 _IOTGET("dht/humidity",H)
130 _IOTGET("dht/temperature",T)
140 PRINT"humidity:";H
150 PRINT"temperature:";T
