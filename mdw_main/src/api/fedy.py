from pyspark.sql import SparkSession
from pyspark.sql.functions import when

# Start your Spark session (skip if already started)
spark = SparkSession.builder.getOrCreate()

# Example loading tables (replace with your actual DataFrames if already loaded)
# Assuming you already have the 3 tables loaded as DataFrames:
# - stock_df
# - product_configurations_df
# - product_df

# Example schemas (for your information):
# stock_df: [id, product_config_id, depot_id, quantity]
# product_configurations_df: [id, product_id, variant]
# product_df: [id, name]

# Perform the joins
joined_df = stock_df \
    .join(product_configurations_df, stock_df.product_config_id == product_configurations_df.id) \
    .join(product_df, product_configurations_df.product_id == product_df.id)

# Select needed columns and create 'is_available' column
result_df = joined_df.select(
    product_df.name.alias("product_name"),
    product_configurations_df.variant,
    stock_df.depot_id,
    stock_df.quantity,
    when(stock_df.quantity > 0, True).otherwise(False).alias("is_available")
)

# Show the result
result_df.show(truncate=False)