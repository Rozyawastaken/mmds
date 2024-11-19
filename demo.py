import time
import cloudpickle

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, BooleanType


SCHEMA = StructType(
    [
        StructField("title", StringType(), True),
        StructField("title_url", StringType(), True),
        StructField("user", StringType(), True),
        StructField("bot", StringType(), True)
    ]
)


def get_bloom_filter():
    with open('bloom_filter.pkl', 'rb') as f:
        bitarray, hashes = cloudpickle.load(f)
    return bitarray, hashes


def blacklist(bitarray, hashes):
    @F.udf(returnType=BooleanType())
    def f(username):
        if not isinstance(username, str):
            return None

        bot = True
        for i in range(0, len(hashes)):
            k = hashes[i](username)
            if bitarray[k] == 0:
                bot = False
        return bot
    return f


def main():
    stream_df = (
        spark.readStream
        .format("socket")
        .option("host", "localhost")
        .option("port", 9999)
        .load()
    )

    bitarray, hashes = get_bloom_filter()

    stream_df = (
        stream_df.filter(F.col("value").startswith("data: {"))
        .select(F.trim(F.substring(F.col("value"), 7, 10_000)).alias("json_string"))
        .select(F.from_json(F.col("json_string"), SCHEMA).alias("parsed"))
        .select("parsed.*")
        .withColumn("blacklisted", blacklist(bitarray, hashes)(F.col("user")))
    )

    query = (
        stream_df.writeStream
        .trigger(processingTime="2 seconds")
        .outputMode("append")
        .format("console")
        .start()
    )
    time.sleep(60)
    query.stop()


if __name__ == '__main__':
    spark = SparkSession.builder.getOrCreate()  # Initialize Spark session
    main()
    spark.stop()
