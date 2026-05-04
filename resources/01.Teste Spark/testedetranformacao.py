# %%
import sys, os, glob
os.environ["SPARK_HOME"] = "/usr/local/spark"

sys.path.append("/usr/local/spark/python")

sys.path.append("/usr/local/spark/python/lib/py4j-0.10.9.7-src.zip")

# %%
from pyspark.sql import SparkSession

# %%
spark = (SparkSession.builder
        .getOrCreate()
)

# %%
df = spark.read.csv("/data/storage/E-Commerce/Produto.csv", header=True, inferSchema=True)

# %%
df.show()

# %%
spark.stop()

# %%



