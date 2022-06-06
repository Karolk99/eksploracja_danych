import plotly.graph_objects as go


def time_chart(df):
    i = 0
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df['Captured Time'],
            y=df['Value'],
            name='Fokushima',
            visible=(i == 0)
        )
    )

    fig.update_layout(hovermode="x unified")
    fig.update_layout(
        autosize=False,
        width=1000,
        height=800
    )

    fig.update_xaxes(
        rangeslider_visible=True
    )

    fig.show()
