import pymysql
from common.utils.read_config import read_config_ini

def connect_db(sql):
    try:
        r = read_config_ini()
        conn = pymysql.connect(host=r.get("mysql_config","db_host"),
                                              user=r.get("mysql_config","db_username"),
                                              passwd=r.get("mysql_config","db_passwd"),
                                              port=r.getint("mysql_config","db_port"),
                                              db=r.get("mysql_config","db_name"),
                                              charset='utf8',
                                              cursorclass=pymysql.cursors.DictCursor)
    except pymysql.err.OperationalError as e:
        print("MySQL Error %d:%s"%(e.args[0],e.args[1]))
    #sql_get_path_getBaseConfig = "select path from api_req_get where api_name='getBaseConfig'"
    with conn.cursor() as cursor:
        cursor.execute(sql)
        res = cursor.fetchall()
    conn.commit()
    return res