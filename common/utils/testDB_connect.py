from common.utils.UseDatabase import UseDatabase

def connect_test_db(sql):
    with UseDatabase("test_mysql_config","mysql") as cursor:
        cursor.execute(sql)
        res = cursor.fetchall()
    return res

