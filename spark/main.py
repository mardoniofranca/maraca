#/opt/spark/bin/pyspark

from pyspark import SparkContext

sc = SparkContext.getOrCreate()

text_file = sc.textFile("/home/mardoniofranca/work/rive/desafio/github/maraca/data/text/text_cl_sa.txt")

counts = text_file.flatMap(lambda line: line.split(" ")) \
...              .map(lambda word: (word, 1)) \
...              .reduceByKey(lambda a, b: a + b)

counts.saveAsTextFile("/home/mardoniofranca/work/rive/desafio/github/maraca/data/text/result/dic_cl_sc.txt")