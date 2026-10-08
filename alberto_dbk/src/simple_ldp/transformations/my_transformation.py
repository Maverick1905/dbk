from pyspark import pipelines as dp 

@dp.table 
def cr_t():
    return spark.range(10)