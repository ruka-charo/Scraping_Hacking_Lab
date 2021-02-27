import pandas as pd


#%%
url = 'https://info.finance.yahoo.co.jp/ranking/?kd=45'

#データの抽出
df = pd.read_html(url)
#必要な部分のみ抽出
#df[0][['順位','コード','市場','名称','平均年収（千円）','従業員数（単独）']]

#csvとして保存
df[0].to_csv('data.csv')
#xlsxとして保存
#df[0].to_excel('data.xlsx')

#%%
url_1 = 'https://info.finance.yahoo.co.jp/ranking/?kd=45'
url_2 = 'https://info.finance.yahoo.co.jp/ranking/?kd=4'

#データの抽出
df_1 = pd.read_html(url_1)
df_2 = pd.read_html(url_2)

#xlsxとしてシートを分けて保存
with pd.ExcelWriter('data.xlsx') as writer:
    df_1[0].to_excel(writer, sheet_name='平均年収ランキング')
    df_2[0].to_excel(writer, sheet_name='時価総額ランキング')
