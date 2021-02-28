import matplotlib.pyplot as plt
import pandas as pd
from fbprophet import Prophet
plt.rcParams['font.family'] = 'Hiragino Sans'


url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/\
monthly_s3.php?prec_no=44&block_no=47662'

#データの抽出
dfs = pd.read_html(url)
df = dfs[0].dropna()


'''時系列予測'''
#学習データ
data = pd.DataFrame()
data['y'] = df['1月']
data['ds'] = df[['年']].apply(lambda x: '{}'.format(x[0]), axis=1)+ '-01-01'

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
