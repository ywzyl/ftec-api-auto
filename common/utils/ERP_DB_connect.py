import pymssql
from common.utils.read_config import read_config_ini

def connect_ERP_db(sql):
    try:
        r = read_config_ini()
        conn = pymssql.connect(r.get("ERP_SQLServer_config","db_host"),r.get("ERP_SQLServer_config","db_username"),
                               r.get("ERP_SQLServer_config","db_passwd"),r.get("ERP_SQLServer_config","db_name"))
    except pymssql.OperationalError as e:
        print("SQLServer ERROR {}:{}".format(e.args[0],e.args[1]))
    with conn.cursor() as cursor:
        cursor.execute(sql)
        res = cursor.fetchone()
    conn.commit()
    return res