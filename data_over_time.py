import plotly.express as px
import pandas as pd

# df = px.data.gapminder()
# df.to_csv("Device_ID_100422.csv", mode="a", header=True, index=False)
input_file = "Device_ID_100422.csv"
df = pd.read_csv(input_file)
df = df.drop_duplicates(["Captured Time"])
print(df)
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    # locations="iso_alpha",
    # color="continent",
    hover_name="Latitude",
    size="Value",
    animation_frame="Captured Time",
    projection="natural earth",
)
fig.show()
