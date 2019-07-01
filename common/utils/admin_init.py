from common.utils.testDB_connect import connect_test_db

def admin_init():
    sql = """update f_user_info set account_no='13068281410' where open_id='eccbc87e4b5ce2fe28308fd9f2a7baf3'"""
    connect_test_db(sql)

def admin_clean():
    sql = """update f_user_info set account_no='admin' where open_id='eccbc87e4b5ce2fe28308fd9f2a7baf3'"""
    connect_test_db(sql)