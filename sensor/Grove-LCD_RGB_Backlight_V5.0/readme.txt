■概要
MSX IoT BASICを使用し、Grove-LCD RGB Backlight V5.0というLCDモジュールへ文字を表示する際に調査した内容を記載しています。
データシートを確認すればわかる内容ですが、主に使いそうな部分を日本語でメモしましたので、ここに共有します。
実際に使用する際は「■初期化」セクションから読んで頂ければ十分かと思います。

■Grove-LCD RGB Backlight V5.0
2行16桁の文字を表示できるLCDモジュール。
バックライトは、RGBそれぞれ0～255の値が設定できる。
制御はI2Cプロトコルで行う。

LCDを制御するコマンドの送信と、LCDに表示するデータの送信がある。
どちらも、LCD_ADDRESSに対して送信する。

LCDを制御するコマンドの送信は、&H80+コマンドデータを送信する。
LCDに表示するデータの送信は、&H40+表示データを送信する。

LCDバックライトの制御は上記と別コマンドで、RGB_ADDRESS_V5に対して送信する。
バックライトのON/OFFや色変更はこちらのコマンドで行う。

■デバイスツリー
// Device I2C Arress
// Version 5.0用です。以前のVersionから変更されています。
LCD_ADDRESS     0x3E	//MSX IoT BASICのデバイスツリーは"device/i2c_a/3E"
RGB_ADDRESS_V5  0x30	//MSX IoT BASICのデバイスツリーは"device/i2c_a/30"

■LCD制御コマンド
// commands
// LCDを制御するコマンド
// このコマンドと、制御用ビットを組み合わせて使用する。
LCD_CLEARDISPLAY    0x01	// 本コマンドのみで使用
LCD_RETURNHOME      0x02	// 本コマンドのみで使用
LCD_ENTRYMODESET    0x04
LCD_DISPLAYCONTROL  0x08
LCD_CURSORSHIFT     0x10
LCD_FUNCTIONSET     0x20
LCD_SETCGRAMADDR    0x40
LCD_SETDDRAMADDR    0x80

■制御用ビット
// flags for display entry mode
// LCD_ENTRYMODESET(&H04)と各ビットを加算して使用
// LCD_ENTRYRIGHT+LCD_ENTRYSHIFTINCREMENTの組み合わせで、右から左への横書きに対応
LCD_ENTRYRIGHT           0x00	//文字を右から左に出力する
LCD_ENTRYLEFT            0x02	//文字を左から右に出力する
LCD_ENTRYSHIFTINCREMENT  0x01	//文字出力後カーソルを左方向に移動する
LCD_ENTRYSHIFTDECREMENT  0x00	//文字出力後カーソルを右方向に移動する

// flags for display on/off control
// LCD_DISPLAYCONTROL(&H08)と各ビットを加算して使用
LCD_DISPLAYON    0x04	//画面表示
LCD_DISPLAYOFF   0x00	//画面非表示(出力済の文字列データは残る)
LCD_CURSORON     0x02	//カーソル'_'が表示される
LCD_CURSOROFF    0x00	//カーソル非表示
LCD_BLINKON      0x01	//カーソル位置が反転表示で点滅する
LCD_BLINKOFF     0x00	//カーソル位置が点滅しない

// flags for display/cursor shift
// LCD_CURSORSHIFT(&H10)とビットを加算して使用
LCD_DISPLAYMOVE  0x08
LCD_CURSORMOVE   0x00
LCD_MOVERIGHT    0x04
LCD_MOVELEFT     0x00

// flags for function set
// LCD_FUNCTIONSET(&H20)と各ビットを加算して使用
LCD_8BITMODE  0x10
LCD_4BITMODE  0x00
LCD_2LINE     0x08
LCD_1LINE     0x00
LCD_5x10DOTS  0x04
LCD_5x8DOTS   0x00


■初期化
【1】LCDの初期化
デバイスツリーLCD_ADDRESS(&H3E)に対して、下記を送信する。

1) CHR$(&H80)+CHR$(LCD_FUNCTIONSET(&H20)+LCD_2LINE(&H08)) 	//表示領域を2行に設定
2) CHR$(&H80)+CHR$(LCD_DISPLAYCONTROL(&H08)+LCD_DISPLAYON(&H04))	//ディスプレイON+カーソルOFF+点滅OFF
3) CHR$(&H80)+CHR$(LCD_CLEARDISPLAY(&H01))	//画面消去+カーソルを0位置に移動
4) CHR$(&H80)+CHR$(LCD_ENTRYMODESET(&H04)+LCD_ENTRYLEFT(&H02))	//左から右に出力+出力後カーソル右移動

【2】バックライトLED(RGBチップ)の初期化
デバイスツリーRGB_ADDRESS_V5(&H30)に対して、下記を送信する。

1) CHR$(&H00)+CHR$(&H07)	//RGBチップのリセット
2) CHR$(&H04)+CHR$(&H15)	//LED全てON

■文字列の表示
デバイスツリーLCD_ADDRESS(&H3E)に対して、下記を送信する。

※カーソル位置指定：X=0～15,Y=0～1
1) CHR$(80)+CHR$((&H40*Y)+&H80+X)	//カーソル位置を指定しない場合は不要
2) CHR$(80)+CHR$(&H40)+"文字列"		//CHR$(&H40)を省略した場合、先頭1文字が出力されない

■バックライトLEDカラーの指定
デバイスツリーRGB_ADDRESS_V5(&H30)に対して、下記を送信する。
※RGBの値：R=0～255,G=0～255,B=0～255

1) CHR$(&H06)+CHR$(R)	//赤色の値
2) CHR$(&H07)+CHR$(G)	//緑色の値
3) CHR$(&H08)+CHR$(B)	//青色の値


■参考
Grove - 16X2 LCD RGB Backlight - Seeed Studio
https://www.seeedstudio.com/Grove-LCD-RGB-Backlight.html

Datasheet
https://files.seeedstudio.com/wiki/Grove-LCD_RGB_Backlight/Grove-LCD_RGB_Backlight_V5.0_Datasheet.pdf

X(Twitter)
https://twitter.com/S_Okue/status/1727990927170691142

