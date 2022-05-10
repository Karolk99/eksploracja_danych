from cupshelpers import Device
from visualize_localization import VisualizeLocalizations
from filter_data import FilterData
from datetime import datetime

import pandas as pd

# VisualizeLocalizations.visualize("locations_distinct.csv")
input_file = "only_cpm_locations.csv"
memory_available: int = 1000000000
df = pd.read_csv(input_file, nrows=100)
nrows = 10
df_sample = pd.read_csv(
    input_file,
    nrows=nrows,
)
start_date = "2022-04-16"
print(datetime.strptime(start_date, '%Y-%m-%d'))
# end_date = "2022-04-16"
# after_start_date = df_sample["Captured Time"] >= start_date

# before_end_date = df_sample["Captured Time"] <= end_date

# between_two_dates = after_start_date & before_end_date

# filtered_dates = df_sample.loc[between_two_dates]
# print(filtered_dates)
# df_sample_size = df_sample.memory_usage(index=True).sum()
# chunk_size = (memory_available / df_sample_size) / nrows

# csv_iterator = pd.read_csv(
#     input_file,
#     iterator=True,
#     chunksize=int(chunk_size),
# )

# first_iteration = True
# for chunk in csv_iterator:
#     chunk["Captured Time"] = pd.to_datetime(
#         chunk["Captured Time"], errors="coerce"
#     ).dt.date
#     chunk = df.drop_duplicates(["Captured Time", "Latitude"])
#     chunk.to_csv(
#         "3xfiltered_data_cpm.csv", mode="a", header=first_iteration, index=False
#     )
#     first_iteration = False if first_iteration else first_iteration
# df["Captured Time"] = pd.to_datetime(df["Captured Time"]).dt.date
# print(df.drop_duplicates(["Captured Time", "Value"]))
# df = df[df["Unit"] == "cpm"]

# df.to_csv("only_cpm_locations.csv", mode="a", header=True, index=False)
# FilterData.filter_cpm_rows("filtered_data.csv")

# df = pd.read_csv("only_cpm_locations.csv")


# device_ids = df["Device ID"].to_list()

# df = df[df["Device ID"].isin(device_ids)]
# df.to_csv("siema.csv", mode="a", header=True, index=False)
