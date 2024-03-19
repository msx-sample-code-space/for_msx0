Link:
[https://github.com/Ninune-wa/MSX0-Sensor-Utility/tree/main/MSX0Stack-LED(PowerIndicatorLight)](https://github.com/Ninune-wa/MSX0-Sensor-Utility/tree/main/MSX0Stack-LED(PowerIndicatorLight))

.dsk:
[https://github.com/Ninune-wa/MSX0-Sensor-Utility/blob/main/MSX0-Sensor-Utility.dsk](https://github.com/Ninune-wa/MSX0-Sensor-Utility/blob/main/MSX0-Sensor-Utility.dsk)
## MSX0StackのPower Indicator Light(Green LED)の動作確認用プログラムです。

0.5秒間隔でLEDを点灯/消灯します。

### Power Indicator Lightに関する仕様
- MSX0StackのPower Indicator Lightは、AXP192のGPIO1に接続されています。[AXP192 Dataseet](https://github.com/m5stack/M5-Schematic/blob/master/Core/AXP192%20Datasheet_v1.1_en_draft_2211.pdf)
- AXP192 I2C Address: ０x３４
- GPIO1の制御レジスター: 94H
- GPIO1の制御: Bit1(1:disable 0:enable)

### BASICプログラム
- [MSX0LED.BAS](https://github.com/Ninune-wa/MSX0-Sensor-Utility/blob/main/MSX0Stack-LED(PowerIndicatorLight)/MSX0LED.BAS)

### Ex.コマンドライン(ワンライナー)
コマンドラインにコピペして動作を確認できます。

※MSX0起動後に１度CALL IOTFINDを実行してデバイスツリーにI2Cデバイスを認識させておく必要があります。


- IOTFIND
```
DT$="device/i2c_i":_IOTFIND(DT$,C)
```

- LED ON
```
DT$="device/i2c_i/34":RG$=CHR$(&H94):_IOTPUT(DT$,RG$):_IOTGET(DT$,GI):_IOTPUT(DT$,RG$+CHR$(GI AND &B11111101))
```

- LED OFF
```
DT$="device/i2c_i/34":RG$=CHR$(&H94):_IOTPUT(DT$,RG$):_IOTGET(DT$,GI):_IOTPUT(DT$,RG$+CHR$(GI OR &B00000010))
```

- LED ON/OFF（トグル）
```
DT$="device/i2c_i/34":RG$=CHR$(&H94):_IOTPUT(DT$,RG$):_IOTGET(DT$,GI):_IOTPUT(DT$,RG$+CHR$(GI XOR &B00000010))
```
