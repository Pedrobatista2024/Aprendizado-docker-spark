# %%
import sys, os, glob


# Aponta para a instalação do Spark da imagem
os.environ["SPARK_HOME"] = "/usr/local/spark"

# Adiciona o diretório do PySpark ao sys.path
sys.path.append("/usr/local/spark/python")

#Adiciona o diretório py4j do PySpark ao sys.path
sys.path.append("/usr/local/spark/python/lib/py4j-0.10.9.7-src.zip")

# %%



# %%
from pyspark.sql import SparkSession

# %%
spark = (SparkSession.builder
        .getOrCreate()
)

# %%
df = spark.read.csv("/data/storage/E-Commerce/Vendas.csv" , header=True, inferSchema=True)

# %%
df.show()

# %%
#tratar dados ELT
df.printSchema()

# %%
#inserir em um banco de dados ou storage em nuvem 


# %%
spark.stop()


