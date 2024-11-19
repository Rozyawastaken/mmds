import time
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType


SCHEMA = StructType(
    [
        StructField("title", StringType(), True),
        StructField("title_url", StringType(), True),
        StructField("comment", StringType(), True),
        StructField("user", StringType(), True),
        StructField("bot", StringType(), True),
        StructField("parsedcomment", StringType(), True)
    ]
)


def main():
    stream_df = (
        spark.readStream
        .format("socket")
        .option("host", "localhost")
        .option("port", 9999)
        .load()
    )
    # stream_df = spark.readStream.format("rate").option("rowsPerSecond", 3).load()

    stream_df = (
        stream_df.filter(F.col("value").startswith("data: {"))
        .select(F.trim(F.substring(F.col("value"), 7, 1_000_000)).alias("json_string"))
        .select(F.from_json(F.col("json_string"), SCHEMA).alias("parsed"))
        .select("parsed.*")
    )

    query = (
        stream_df.writeStream
        .trigger(processingTime="1 seconds")
        .outputMode("append")
        .format("console")
        .start()
    )
    time.sleep(5)
    query.stop()


if __name__ == '__main__':
    spark = SparkSession.builder.getOrCreate()  # Initialize Spark session
    main()
    spark.stop()
