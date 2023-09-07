import requests

# お菓子のキーワード入力結果の格納
keyword = input('お菓子のキーワードを入力してね：')

# 取得に行くapiのURL
url = "https://sysbird.jp/toriko/api/"

# パラメータの設定
param = {"apikey": "guest", "format": "json", "keyword": keyword }

# 取得したデータの格納
data = requests.get(url, param).json()

# 出力
for i in data["item"]:
  print(i["name"])