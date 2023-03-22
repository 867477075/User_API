from dal.db_conn_helper import create_connection
conn = create_connection()
from flask import Flask,Response,request
import json

def insert_data(table_name, column, values):
    column = ",".join(column)
    values = "','".join(values)
    SQL_query = f"""INSERT INTO {table_name}({column}) values('{values}');"""
    conn = create_connection()
    with conn:
        with conn.cursor() as cursor: # cursor = conn.cursor()
            result = cursor.execute(SQL_query)

        conn.commit()

    return result


def delete_record(table_name,primary_value):

    SQL_query = f"""DELETE FROM {table_name} WHERE id={primary_value};"""
    cursor = conn.cursor()
    result = cursor.execute(SQL_query)
    conn.commit()
    cursor.close
    # conn.close()

    return result
