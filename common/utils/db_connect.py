from common.utils.UseDatabase import UseDatabase

def connect_db(sql):
    with UseDatabase("mysql_config","mysql") as cursor:
        cursor.execute(sql)
        res = cursor.fetchall()
    return res