import matplotlib.pyplot as plt
import pandas as pd
from fbprophet import Prophet
plt.rcParams['font.family'] = 'Hiragino Sans'


#折線グラブ%%
csv = '/Users/rukaoide/Library/Mobile Documents/\
com~apple~CloudDocs/Documents/Python/Scraping_Hacking_Lab/Pandas/data.csv'

#データの抽出
dfs = pd.read_csv(csv)
df = dfs.dropna()

df.plot('年', '年の値')


'''時系列予測'''
#学習データ
data = pd.DataFrame()
data['y'] = df['年の値']
data['ds'] = df[['年']].apply(lambda x: '{}'.format(x[0]), axis=1)


#モデル構築
model = Prophet(daily_seasonality=True, weekly_seasonality=True,
yearly_seasonality=True)
model.fit(data)

#予測
future_data = model.make_future_dataframe(periods=100, freq='y')
forecast_data = model.predict(future_data)

#プロットして可視化
model.plot(forecast_data)
model.plot_components(forecast_data)
plt.show()
