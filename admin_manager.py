import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password= '',port=3306,db='mydb',charset='utf8')
cursor = conn.cursor()
import user_manager

def ad_user_regist(ad_useremail,ad_userpwd):
    #등록
    insertSql = """INSERT INTO member(num, email, pwd, created_at) VALUES(null, %s, %s, NOW()) """
    cursor.execute(insertSql,(ad_useremail,ad_userpwd))
    conn.commit()
    #등록확인
    sql1 = 'SELECT num, email,pwd, created_at FROM member WHERE email = %s'
    cursor.execute(sql1,(ad_useremail))
    #db에서 등록된 이메일만 출력한다.
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, Email:{1}, Password:{2}, Created On:{3}'.format(row[0], row[1], row[2], row[3]))

def ad_user_repair(repair_email,repair_pwd):
    #수정
    repair_sql = """ UPDATE member SET pwd= %s WHERE email=%s """
    cursor.execute(repair_sql,(repair_pwd,repair_email))
    conn.commit()

    #수정확인
    sql1 = 'SELECT num, email,pwd, created_at FROM member WHERE email = %s'
    cursor.execute(sql1,(repair_email))
    #db에서 등록된 이메일만 출력한다.
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, Email:{1}, Password:{2}, Created On:{3}'.format(row[0], row[1], row[2], row[3]))

    print('PWD이 변경되었습니다.')

def ad_user_delete(del_email):
    deleteSql = '''DELETE FROM member WHERE email = %s'''
    cursor.execute(deleteSql, (del_email))
    conn.commit()

#회원 한명검색
def ad_oneuser_search(user_email):
    sql1 = 'SELECT num, email,pwd, created_at FROM member WHERE email = %s'
    cursor.execute(sql1,(user_email))
    #db에서 등록된 이메일만 출력한다.
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, Email:{1}, Password:{2}, Created On:{3}'.format(row[0], row[1], row[2], row[3]))

#  전체회원목록조ㅗ히  member search
def ad_alluser_search():
    sql1 = 'SELECT num, email,pwd, created_at FROM member'
    cursor.execute(sql1)
    rows = cursor.fetchall()
    
    for row in rows:
        print('No:{0}, Email:{1}, Password:{2}, Created On:{3}'.format(row[0], row[1], row[2], row[3]))

#해당 이메일 정보 출력    
def searchemail(email):
    
    sql1 = 'SELECT num, email,pwd, created_at FROM member WHERE email = %s'
    cursor.execute(sql1,(email))
    #db에서 등록된 이메일만 출력한다.
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, Email:{1}, Password:{2}, Created On:{3}'.format(row[0], row[1], row[2], row[3]))

    print('PWD이 변경되었습니다.')



def item_add(pd_regist_name,pd_regist_price,pd_regist_qty):
    pd_insertSql = """INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, %s, %s, %s, NOW()) """
    cursor.execute(pd_insertSql,(pd_regist_name, pd_regist_price, pd_regist_qty))
    conn.commit()

def itemList_select():
    sql1 = 'Select num, product_name, product_price, product_qty, created_at FROM item'
    cursor.execute(sql1)
    rows = cursor.fetchall()
    
    for row in rows:
        print('No:{0}, name:{1}, price:{2}, qty:{3},Created On:{4}'.format(row[0], row[1], row[2], row[3], row[4]))

def item_update(price,repair_qty,reapair_name):

    pd_repair_sql = """ UPDATE item SET product_price= %s, product_qty =%s WHERE product_name=%s """
    cursor.execute(pd_repair_sql,(price,repair_qty,reapair_name))
    conn.commit()
    print('변경되었습니다.')

def item_delete(name):
    pd_deleteSql = '''DELETE FROM item WHERE product_name = %s'''
    cursor.execute(pd_deleteSql, (name))
    conn.commit()
    print('상품이 삭제 되었습니다.')


def orderList_select():
    sql1 = 'Select num, member_id, item_id, order_qty, order_price, created_at FROM _order'
    cursor.execute(sql1)
    rows = cursor.fetchall()
    for row in rows:
        print('No:{0}, member_id:{1}, item_id:{2}, order_qty:{3},order_price:{4},created_at{5}'.format(row[0], row[1], row[2], row[3],row[4],row[5]))
    print('주문내역조회: 조회완료')

def order_add(member_id,item_id,order_qty,order_price):
    or_insertSql = """INSERT INTO _order(num, member_id, item_id, 
    order_qty, order_price,created_at) VALUES(null, %s, %s, %s, %s, NOW()) """
    cursor.execute(or_insertSql,(member_id, item_id, order_qty, order_price))
    conn.commit()

def order_update(member_id, item_id, order_qty, order_price):
    pd_repair_sql = """ UPDATE _order SET item_id= %s, order_qty =%s,order_price=%s WHERE member_id=%s """
    cursor.execute(pd_repair_sql,(item_id,order_qty,order_price,member_id))
    conn.commit()
    print('변경되었습니다.')

def order_delete(num):
    or_deleteSql = '''DELETE FROM _order WHERE num = %s'''
    cursor.execute(or_deleteSql, (num))
    conn.commit()
    print('상품이 삭제 되었습니다.')

def orderList_read():
    or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order '''
    cursor.execute(or_select_Sql)
    rows = cursor.fetchall()
    for row in rows:
        print('No:{0}, member_id:{1}, item_id:{2}, order_qty:{3},order_price:{4},created_at{5}'.format(row[0], row[1], row[2], row[3],row[4],row[5]))
    print('주문내역조회: 조회완료')

# 회원별 주문목록? 아이디로 찾아
def orderMember_read(member_id):
    
    or_search_sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order WHERE member_id = %s'''
    cursor.execute(or_search_sql,(member_id))
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print('No:{0}, member_id:{1}, item_id:{2}, order_qty:{3},order_price:{4},created_at{5}'.format(row[0], row[1], row[2], row[3],row[4],row[5]))

# def orderBestbuyer():
