# JSONReceiveSample_forMSX0
MSX0でJSONデータを受信してBASICで使用するサンプルです。  

Link:https://github.com/IKATEN-X/JSONReceiveSample_forMSX0

MSX0のHTTP通信のサンプルをベースに、JSONを受信するようにしています。  
JSONデータの解析と値の取得は、[MSX JSON Parser](https://github.com/ricbit/msxjson)を利用していて、その中のJSON.BINが必要となります。  

JSON.BINが&HD000から配置されます。  
Parserがデータを解析するための格納アドレスを&H9000としています。  
また、BASICでも文字列をたくさん使うのでCLEAR文で&HB000からとしています。  
この辺りは扱うデータの大きさで調整をするのが良いかと思います。  
  
本サンプルは、BASICであまり大きなメモリが使用できないので、小さな天気データがを取得できる[Open-Meteo](https://open-meteo.com/)を利用しています。  
JSONで得たいデータのクエリ文字列は[API Docs](https://open-meteo.com/en/docs)で組み立てることができます。  
具体的な使い方などは[こちら](https://paiza.hatenablog.com/entry/2021/11/04/130000)をご覧いただくのが早いかと思います。  
  
またMSX0の不具合なのか、リクエストの方法が間違っているのか、MSX0起動後、最初のHTTPリクエストが失敗します。  
一応リカバリ処理は入れていますのでエラーにはならない様にしています。  
HTTP 1.1では、サーバー側がContent-Lengthを送ってこない場合、Transfer-Encoding: chunked のモードになりBodyデータが小さく区切られ、その区切り毎の最初に16進のサイズデータが付加されて送られてきますが、BASICで解析が面倒なので、リクエスト時にHTTP 1.0を宣言しています。  
  
目視できるようにPRINT文を多用していますが、最小限にすればもう少し早くはなるかと思います。  

最後に...  
実際に使った例としてグラフィカルなものも用意したかったのですが、天気アイコンが多くて、止めました(^-^;
