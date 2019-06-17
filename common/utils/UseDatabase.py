import pymysql,pymssql
from common.utils.read_config import read_config_ini

class UseDatabase:
    def __init__(self,db_config: str,dbtype: str) -> None:
        r = read_config_ini()
        self.host=r.get(db_config,"db_host")
        self.user=r.get(db_config,"db_username")
        self.passwd=r.get(db_config,"db_passwd")
        self.port=r.getint(db_config,"db_port")
        self.db=r.get(db_config,"db_name")
        self.dbtype = dbtype

    def __enter__(self) -> 'cursor':
        if self.dbtype=='mysql':
            try:
                self.conn = pymysql.connect(host=self.host,
                                            user=self.user,
                                            passwd=self.passwd,
                                            port=self.port,
                                            db=self.db,
                                            charset='utf8',
                                            cursorclass=pymysql.cursors.DictCursor)
            except pymysql.err.OperationalError as e:
                print("MySQL Error %d:%s" % (e.args[0], e.args[1]))
            self.cursor = self.conn.cursor()
            return self.cursor
        elif self.dbtype=='sqlserver':
            try:
                self.conn = pymssql.connect(host=self.host,
                                            user=self.user,
                                            passwd=self.passwd,
                                            db=self.db,
                                            charset='utf8')
            except pymssql.err.OperationalError as e:
                print("SQLServer ERROR {}:{}".format(e.args[0],e.args[1]))
            self.cursor = self.conn.cursor()
            return self.cursor
        else:
            raise RuntimeError("Database is incorrect type")

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()