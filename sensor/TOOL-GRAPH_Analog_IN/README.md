Link:
[https://github.com/Ninune-wa/MSX0-Sensor-Utility/tree/main/TOOL-GRAPH_Analog_IN](https://github.com/Ninune-wa/MSX0-Sensor-Utility/tree/main/TOOL-GRAPH_Analog_IN)

.dsk:
[https://github.com/Ninune-wa/MSX0-Sensor-Utility/blob/main/MSX0-Sensor-Utility.dsk](https://github.com/Ninune-wa/MSX0-Sensor-Utility/blob/main/MSX0-Sensor-Utility.dsk)
## MSX0のPORT.B(Analog)の入力をグラフ化する動作確認用プログラムです。

- Analogの入力数値を、画面にグラフ表示します。
- デフォルトは、画面上部がHIGH(4095)、画面下部がLOW(0)です。
- LCD画面中央をタップするか、SPACEキーを押すと、上下が反転(上がLOW/下がHIGH)します。
- HIGH側中央に、現在の入力値が表示されます。
- LOW側中央に、描画済みの入力値の平均値が表示されます。
- 画面右側に、描画済み入力値の最大値と最小値が表示されます。
- 描画スピードはデフォルトx5です。LCD画面の左右をタップするか、カーソルキーの右左で、描画スピードを増減できます。(x1 - x20)


### BASICプログラム
- [ANLG_GL.BAS](https://github.com/Ninune-wa/MSX0-Sensor-Utility/blob/main/TOOL-GRAPH_Analog_IN/ANLG_GL.BAS)
