import duckdb
import pandas as pd
from DB_connect import db
from handlers import logger, JSONResponse
import numpy as np


def write_embeddings(descriptions: list, predict: list, predict_quality: list, dataframe: pd.DataFrame,
                     embeddings: list):
    try:
        con = duckdb.connect()
        con.query('CREATE TABLE DB_DUCK AS SELECT * FROM DB')
        con.query('SELECT * FROM DB_DUCK')
        error_values = []
        for values1, values2, values3, values4 in zip(predict, predict_quality, descriptions, embeddings):
            Brand_val = dataframe[dataframe.id == int(values1)].Brand.iloc[0]
            Category_val = dataframe[dataframe.id == int(values1)].Category.iloc[0]
            df_shape = dataframe.shape[0] + 1
            if values3 in np.unique(dataframe.Description).tolist():
                error_values.append(values3)
            else:
                con.query(
                    f'INSERT INTO DB_DUCK("Description", "Brand", "Category", "Embeddings", "id", "Predict_quality") '
                    f'VALUES(\'{values3}\', \'{Brand_val}\', \'{Category_val}\', \'{values4}\' , \'{df_shape}\', '
                    f'\'{values2}\')')
            data_new = con.query('SELECT * FROM DB_DUCK').to_df()
            db.create_table("Embeddings_db", data=data_new, mode="overwrite")
            if len(error_values) == 0:
                return print(str(f'DATABASE REWROTE SUCCESSFULLY'))
            else:
                return print(str(f'DATABASE WAS REWRITTEN WITHOUT NON-UNIQUE VALUES:{error_values}'))

    except Exception as e:
        logger.exception(str(e))
        return str(JSONResponse(status_code=500, content={'message': str(e)}))
