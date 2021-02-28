import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.family'] = 'Hiragino Sans'


#折線グラブ%%
url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/\
monthly_s3.php?prec_no=44&block_no=47662'

#データの抽出
dfs = pd.read_html(url)
df = dfs[0].dropna()

df.plot('年', '1月')


#散布図%%
url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/\
monthly_s3.php?prec_no=44&block_no=47662'

#データの抽出
dfs = pd.read_html(url)
df = dfs[0].dropna()

plt.scatter(df['年'], df['1月'])
