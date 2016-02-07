# SORACOM SDK for Python
SORACOM SDK for Python は、株式会社 SORACOM の提供する IoT プラットフォームの API を Python プログラムからコールするためのライブラリとなります。

## ダウンロードとインストール
```bash
$ git clone https://github.com/YujiAzama/python-soracomclient.git
$ cd python-soracomclient/
$ sudo pip install -r requirements.txt
$ sudo python setup.py install
```

## 使用方法
```python
#!/usr/bin/env python
from soracomclient.v1_0.client import Client

client = Client("登録メールアドレス", "パスワード")

subscribers = client.list_subscribers()

print subscribers

groups = client.list_groups()

print groups
```
