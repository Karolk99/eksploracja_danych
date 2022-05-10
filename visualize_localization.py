import pandas as pd
import plotly.express as px
from typing import List


class VisualizeLocalizations:
    @staticmethod
    def visualize(
        input_file: str,
    ) -> None:
        df = pd.read_csv(input_file)
        fig = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            hover_name="Device ID",
            hover_data=["Height"],
            color_discrete_sequence=["fuchsia"],
            zoom=3,
            height=900,
        )
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": "traces",
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ],
                }
            ],
        )
        # fig.update_layout(mapbox_style="open-street-map")
        # fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig.show()


if __name__ == "__main__":
    VisualizeLocalizations.visualize("locations_distinct.csv")
