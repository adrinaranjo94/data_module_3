import dask.dataframe as dd

# 1. Leer múltiples ficheros Parquet
#   Reading multiple Parquet files
df_parquet = dd.read_parquet("data/*.parquet")

# 2. Leer múltiples ficheros Feather
#   Reading multiple Feather files
#   A veces se utiliza read_parquet con engine="pyarrow" para leer Feather.
#   De forma más reciente, se podría usar dd.read_feather (dependiendo de la versión de Dask).
df_feather = dd.read_parquet("data_feather/*.feather", engine="pyarrow")

# 3. Unir ambos DataFrame
df_combined = dd.concat([df_parquet, df_feather])

# 4. Filtrar datos (por ejemplo, filas donde 'valor' > 100)
df_filtered = df_combined[df_combined["valor"] > 100]

# 5. Realizar una agregación simple (por ejemplo, contar filas)
count_result = df_filtered.shape[0].compute()
print("Número de filas filtradas:", count_result)

# 6. Escribir a múltiples ficheros Parquet
df_filtered.to_parquet("output_data/filtered_", write_index=False, engine="pyarrow")
