# kenkyutool2
研究に用いたスクリプトその2です。これだけ付属ディレクトリがあるため別にしています。

## 3d.py
#### ./data/ColorのRGB画像と./data/Depthにある距離画像(深度画像)を基に3Dグラフを作成します。
#### ※距離画像の拡張子をsys.argv[1]で設定してください
#### ※RGB画像の拡張子はPNGにしてください
#### ※距離画像は8bit[0,255]のグレースケールにしてください
#### ※距離画像とRGB画像のファイル名は同じにしてください(例：RGB画像「000000.png」　距離画像「000000.o.png」(sys.argv[1]=.o.png))
