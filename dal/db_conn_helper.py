import pymysql


def create_connection():
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="8080", database="userdb"
    )
    return conn


if __name__ == "__main__":
    conn_object = create_connection()

    # with conn_object.cursor() as cursor:
    #     sql_query = """Create table user_entry(id int(10),email varchar(120),first_name varchar(120),
    #     last_name varchar(120),avtar varchar(120),primary key(id));"""
    #     cursor.execute(sql_query)
    #     cursor.close()
