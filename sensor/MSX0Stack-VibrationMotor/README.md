[https://github.com/Ninune-wa/MSX0-Sensor-Utility/tree/main/MSX0Stack-VibrationMotor](https://github.com/Ninune-wa/MSX0-Sensor-Utility/tree/main/MSX0Stack-VibrationMotor)
## MSX0Stackの内蔵振動モーターの動作確認用プログラムです。

内蔵振動モーターを2秒間振動させます。

### 振動モーターに関する仕様
MSX0Stackの振動モーターは、AXP192のLDO3に接続されています。[AXP192 Dataseet](https://github.com/m5stack/M5-Schematic/blob/master/Core/AXP192%20Datasheet_v1.1_en_draft_2211.pdf)
- AXP192 I2C Address: ０x３４
- LDO3の制御レジスター: 12H
- LDO3の制御: Bit3(0:disable 1:enable)

### BASICプログラム
- [MSX0VIBE.BAS](https://github.com/Ninune-wa/MSX0-Sensor-Utility/blob/main/MSX0Stack-VibrationMotor/MSX0VIBE.BAS)

### Ex.コマンドライン(ワンライナー)
コマンドラインにコピペして動作を確認できます。

※MSX0起動後に１度CALL IOTFINDを実行してデバイスツリーにI2Cデバイスを認識させておく必要があります。


- IOTFIND
```
DT$="device/i2c_i":_IOTFIND(DT$,C)
```


- 振動ON
```
DT$="device/i2c_i/34":RG$=CHR$(&H12):_IOTPUT(DT$,RG$):_IOTGET(DT$,GI):_IOTPUT(DT$,RG$+CHR$(GI OR &B00001000))
```

- 振動OFF
```
DT$="device/i2c_i/34":RG$=CHR$(&H12):_IOTPUT(DT$,RG$):_IOTGET(DT$,GI):_IOTPUT(DT$,RG$+CHR$(GI AND &B11110111))
```

- 振動ON/OFF（トグル）
```
DT$="device/i2c_i/34":RG$=CHR$(&H12):_IOTPUT(DT$,RG$):_IOTGET(DT$,GI):_IOTPUT(DT$,RG$+CHR$(GI XOR &B00001000))
```
