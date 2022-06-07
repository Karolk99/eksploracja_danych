import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

if __name__ == "__main__":
    df = pd.read_csv('group_by_day.csv') \
        .sort_values(by='Captured Time') \
        .drop(['Latitude', 'Longitude', 'Device ID', 'Height'], axis=1) \
        .rename(columns={'Captured Time': 'ds', 'Value': 'y'})

    df = df[pd.to_datetime(df['ds']) > pd.to_datetime('2019-01-01')]
    df.to_csv('from2019.csv')

    print(df.head())

    m = Prophet()
    m.fit(df)

    future = m.make_future_dataframe(periods=365)
    print(future.tail())

    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

    fig1 = m.plot(forecast)
    # fig1.show()

    fig2 = m.plot_components(forecast)
    # fig2.show()

    plot_plotly(m, forecast).show()

    plot_components_plotly(m, forecast).show()
