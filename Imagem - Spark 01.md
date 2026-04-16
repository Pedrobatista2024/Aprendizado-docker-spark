

D:\00. Cursos - Novos\13.Docker\Material Para Download\Project-001\storage
D:\00. Cursos - Novos\13.Docker\Material Para Download\Project-001\resources


https://hub.docker.com/r/jupyter/pyspark-notebook/tags

```bash
docker pull jupyter/pyspark-notebook:x86_64-spark-3.5.0
docker pull spark
docker pull spark:3.5.5
########
docker images
```

Criando container a partir de uma imagem 
 ```bash
docker run -d --name spark-aula -p 8888:8888 -v "D:\00. Cursos - Novos\13.Docker\Material Para Download\Project-001:/data" -w /data --user root 425f90dd2da7

#git bash
docker run -d --name spark-aula -p 8888:8888 -v "/$(pwd)://data" -w //data --user root 3159c3aa2e9a


```
  - `-d`: modo em segundo plano (detached).
  - `--name spark-aula`: Define o nome do container.
  - `-p 8888:8888`: Mapeia a porta 8888 do container para a 8888 do host (acesso ao Jupyter Lab).
  - `-v "CAMINHO_DO_WINDOWS:/data"`: Monta uma pasta do seu computador dentro do container no diretório /data.
Assim o Spark consegue acessar seus arquivos CSV, JSON, Parquet etc.
  - Substitua `D:\00. Cursos - Novos\13.Doc.............` pelo caminho completo no seu computador.
  - `-w /data`:Define /data como diretório de trabalho inicial no container.
  - `user root`: Inicia o container como usuário root (permissões liberadas).
  - `425f90dd2da7`: ID da imagem Spark que você está rodando (pode ser o nome da imagem tambem).

```bash
#acessar spark no navegador
docker logs spark-aula
docker logs 459f8326bbe9


http://459f8326bbe9:8888/lab?token=6a91e861c94cc07baed48dc442dcf259a2cf69c8137dd0b2
http://127.0.0.1:8888/lab?token=6a91e861c94cc07baed48dc442dcf259a2cf69c8137dd0b2
```
ver containers e startar 
```bash'
docker ps -a
docker start 4d9467065829
dokcer stop 4d9467065829

```

deletar container
```bash
docker rm spark-aula-3.5 
docker rm b88de8e9536b

```


Entrar no container (abrir terminal dentro dele)

```bash
docker exec -it spark-aula bash
docker exec -it 4d9467065829 bash 
pyspark

ou 
exit()
spark-submit --version

```
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.5.0
      /_/


ver pastas  e criar uma nova pasta em storage e carregar um arquivo SCV 

cd = entra nas pastas
ls = lista pastas/ arquivos

```bash

#Ir para a sua pasta inicial (root):
cd /
cd ~


ls /data
ls /data/storage
ls "/data/storage/Arquivos CSV" #Lista somente o conteúdo da pasta.
readlink -f Produto.csv
readlink -f *


```
-------- ver spark funcionado no terminal

```bash
pyspark
df = spark.read.csv("/data/storage/E-Commerce/Vendas.csv" , header=True, inferSchema=True)
df.show()
```


```bash
spark-submit "/data/resources/01.Teste Spark/01.teste spark.py"
```


--- Agora vamos  sair do terminal baixar extensao dev container e atuar com arquivos e scripts direto no vscode dentro do container

1. Baixar extensao docker 
2. Aperte Ctrl + Shift + P
3. Digite: Dev Containers: Attach to Running Container
4. Clique no container:
4d9467065829
ou o nome que aparece, como:
spark, pyspark-notebook, etc.

5. Pronto janela vscode é aberta dentro do container 

 -> Abrir a raiz do container (para ver TUDO)

No VS Code (dentro do Dev Container):
Vá em File
Clique em Open Folder…
Digite: / 



```bash
exit()
which python
which pyspark
```

→ Isso mostra duas coisas importantes:
✔ /opt/conda/bin/python

pasta principal do spark
✔ /usr/local/spark/bin/pyspark


Conclusão:
Seu Jupyter já está com PySpark instalado e configurado, mas o notebook nao encherga o SPARK

sys.path é uma lista de diretórios onde o Python procura módulos para importar.

Quando você faz:

```bash
import pyspark

```

O Python vai procurar o pacote pyspark dentro de todos os caminhos que estão no sys.path.
Se o diretório onde o PySpark está instalado não estiver no sys.path, o Python não consegue importar.

Por isso você fez:

```bash
sys.path.append("/usr/local/spark/python")
sys.path.append("/usr/local/spark/python/lib/py4j-0.10.9.7-src.zip")

```
>>>>> Isso "ensina" o Python a encontrar PySpark e Py4J.



####  resumo para entendimento 

O Kernel do Jupyter é o motor que executa o código Python dentro do notebook.
É apenas um processo Python separado, responsável por:

Rodar cada célula de código
Manter variáveis na memória
Manter o estado do notebook
Receber comandos do Jupyter
Enviar o resultado de volta para a tela


Jupyter Notebook = O caderno
Kernel = O cérebro que faz a conta

O notebook mostra o resultado.
O kernel calcula o resultado.

Obs:
O kernel Python NÃO entende Spark.
Ele só entende Python.

Quando você faz:

```bash
df.show()
```

O kernel Python não executa esse comando.
Ele manda isso para o Spark Driver executar.

O kernel é só o tradutor.