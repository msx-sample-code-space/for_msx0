調査中または暫定的な情報へのリンクになります。
まだ情報整理中の物が多めです。

## IOT I/Oポート ACCESS周りの調査

https://github.com/uniskie/MSX_MISC_TOOLS/tree/main/for_MSX0

初回版の動作基準で、IOT命令をI/O操作で行うための情報まとめ。

その他、べーしっ君のちょっとしたTIPS等も入っています。


## openMSXでMSX0を動かせるかどうかの試み

https://github.com/uniskie/MSX_DOCUMENTS/tree/main/MSX0_for_openMSX

1. マシン構成ファイル
2. MSX0のスロット構成
3. MSX0からのROMの取り出し方法（手作業と補助ツール）
4. I/Oポートのエミュレーションについて
  
   I/Oポート読み書きをスクリプトの処理で乗っ取ることが可能ですが、  
   I2Cデバイスのエミュレーション（主に入出力）をどうするかが課題です。

   例えば、bindコマンドでマウスやキーのイベントハンドラを登録し、  
   I2Cデバイスが返す値に利用するなども考えられます。  
   他には、ソケット接続した外部プログラムと連携する方法も考えられます。

   openMSX組み込みのtcl/tkスクリプトエンジンで使用できる機能一覧  
   https://openmsx.org/manual/commands.html

   外部プログラムからソケット接続でopenMSXのスクリプトエンジンとやり取りする方法（コマンドの実行と各種イベントの取得）  
   https://openmsx.org/manual/openmsx-control.html

   - ノードリストは対応が簡単そう
   - ディスクイメージファイルやconfファイルはどこに置くか

   現状、MSX0拡張openMSXスクリプトは検討段階のままで止まっています。

   openMSX本体のソースコードを改造すれば何でもできますが、
   I2Cを介してやりたい事は多岐にわたるので、
   出来るだけ柔軟に対応できる方法が望ましいと思われます。
