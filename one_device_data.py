import pandas as pd

# VisualizeLocalizations.visualize("locations_distinct.csv")
input_file = "filtered_data_cpm.csv"
memory_available: int = 1000000000
df = pd.read_csv(input_file, nrows=100)
nrows = 10
df_sample = pd.read_csv(
    input_file,
    nrows=nrows,
)

df_sample_size = df_sample.memory_usage(index=True).sum()
chunk_size = (memory_available / df_sample_size) / nrows

csv_iterator = pd.read_csv(
    input_file,
    iterator=True,
    chunksize=int(chunk_size),
)

first_iteration = True
for chunk in csv_iterator:
    chunk["Captured Time"] = pd.to_datetime(
        chunk["Captured Time"], errors="coerce"
    ).dt.date
    chunk = chunk.loc[
        chunk["Device ID"] == 100422
    ]  # df.drop_duplicates(["Captured Time", "Latitude"])
    chunk.to_csv(
        "Device_ID_100422.csv", mode="a", header=first_iteration, index=False
    )
    first_iteration = False if first_iteration else first_iteration
