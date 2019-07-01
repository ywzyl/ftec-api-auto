from common.utils.testDB_connect import connect_test_db
from common.utils.db_connect import connect_db

def clean_product_data(api_name: str) -> None:
    sql1 = """select data from api_req_post where api_name='{}'""".format(api_name)
    res = connect_db(sql1)
    name = res[0]['data'].split()[-3].split('"')[1]
    sql2 = """delete from f_institution_product where name ='{}'""".format(name)
    connect_test_db(sql2)

