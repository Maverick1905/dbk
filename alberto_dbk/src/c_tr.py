from pyspark.sql.functions import lower, trim

class CustomTransform:
    def __init__(self, column_to_clean: str):
        self.column_to_clean = column_to_clean

    def transform(self, df):
        return df.withColumn(
            self.column_to_clean,
            lower(trim(df[self.column_to_clean]))
        )