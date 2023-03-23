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


def upsert(table_name,data):

    all_column = [x for x in data]
    primary_key = all_column.pop(0)
    all_column = ",".join(all_column)
    all_value = [y for y in data.values()]
    primary_value = all_value.pop(0)
    all_value = "','".join(all_value) # 1 ',' 2 ',' 3 ','...n

    key_value = [f"{keys}='{values}'" for keys,values in data.items()] # [name='avc',city='pune'..]
    key_value = ",".join(key_value) # "name = 'avc' ,city = 'pune',"

    sql = f"""SELECT ID from {table_name} where {primary_key}={primary_value};"""
    Insert = f"""INSERT into {table_name}({primary_key},{all_column}) values({primary_value},'{all_value}');"""
    Update = f"""UPDATE {table_name} SET {key_value} where {primary_key}={primary_value};"""

    cursor = conn.cursor()
    status = cursor.execute(sql)

    if status == 0:
        result = cursor.execute(Insert)
        conn.commit()
        cursor.close()

        return result,status
    result = cursor.execute(Update)
    conn.commit()
    cursor.close()

    return result,status


def patch_record(table_name,data):

    primary_value = data.get("id")
    data = [f"{keys}='{values}'" for keys, values in data.items()]
    data = ",".join(data)

    update = f"""UPDATE {table_name} SET {data} WHERE id={primary_value};"""
    breakpoint()
    cursor = conn.cursor()
    result = cursor.execute(update)
    conn.commit()
    cursor.close()

    return result



