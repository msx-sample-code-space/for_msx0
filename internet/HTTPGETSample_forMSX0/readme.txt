# HTTPGETSample_forMSX0
MSX0のソケット通信でHTTPのGETをしてSCREEN2の画像を表示します。 

LINK:https://github.com/IKATEN-X/HTTPGETSample_forMSX0 

BASICソース内に「YOURWWWADDRESS」という箇所が2か所あるので、FQDNかIPアドレスに打ち換えてください。  
（httpなどのスキームは必要ありません）  
50～90行はダウンロードするファイル名を指定しています。こちらにサンプルファイルとして置いていますので確認したいサーバーにアップロードしてください。  
210行目にルートからのリクエストパスを生成しているので、必要に応じて書き換えてください。  
  
注意：  
MSX0のSOCKET通信はSSL通信に対応していませんので、個人情報を含む通信を行い際にはご注意ください。  