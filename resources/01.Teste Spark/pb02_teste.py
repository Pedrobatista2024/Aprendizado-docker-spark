# %%
import sys, os, glob

#aponta para a instalação do spark da imagem
os.environ["SPARK_HOME"] = "/usr/local/spark"

#adicionando diretorio dp pyspark ao sys.path
sys.path.append("/usr/local/spark/python")

#adiciobabdo o diretorio py4j do pyspark ao sys.path
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
df.printSchema()

# %%
spark.stop()


