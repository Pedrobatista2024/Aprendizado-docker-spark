

from pyspark.sql import SparkSession
spark = (SparkSession.builder
        .getOrCreate()
)


df = spark.read.csv("/data/storage/E-Commerce/Produto.csv" , header=True, inferSchema=True)
df.show()

spark.stop()


