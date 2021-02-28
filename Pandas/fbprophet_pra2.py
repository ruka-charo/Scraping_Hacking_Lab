import matplotlib.pyplot as plt
import pandas as pd
from fbprophet import Prophet
plt.rcParams['font.family'] = 'Hiragino Sans'


csv = '/Users/rukaoide/Library/Mobile Documents/\
com~apple~CloudDocs/Documents/Python/Python_intro_pra/\
data/data_sample/death_valley_2018_simple.csv'

dfs = pd.read_csv(csv)
df = dfs.dropna()


'''時系列予測'''
#学習データ
data = pd.DataFrame()
data['y'] = df['TMAX']
data['ds'] = df['DATE']

#モデル構築
model = Prophet(daily_seasonality=True, weekly_seasonality=True,
yearly_seasonality=True)
model.fit(data)

#予測
future_data = model.make_future_dataframe(periods=365, freq='d')
forecast_data = model.predict(future_data)

#プロットして可視化
model.plot(forecast_data)
model.plot_components(forecast_data)
plt.show()
