from common.utils.UseDatabase import UseDatabase

def connect_ERP_db(sql):
    with UseDatabase("ERP_SQLServer_config","sqlserver") as cursor:
        cursor.execute(sql)
        res = cursor.fetchone()
    return res