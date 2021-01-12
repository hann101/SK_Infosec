import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password= '',port=3306,db='mydb',charset='utf8')
cursor = conn.cursor()

#사용자 로그인 화면
def user_login(login_emial,login_pwd):
    #db에서 입력한 id 찾고 
    select_Sql = '''SELECT num, email, pwd, created_at FROM member WHERE email = %s'''
    cursor.execute(select_Sql,(login_emial))
    #해당 pwd랑 이매치시켜서 맞으면 통과
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        #검색 >일치
        if row[2] == login_pwd:
            print('로그인 성공!')
            permit = 1
            return permit
            #권한 부여
        else:
            print('비밀번호가 다릅니다.')

#상품목록 조회
def product_list(login_emial):
  
    sql1 = 'Select num, product_name, product_price, product_qty, created_at FROM item'
    cursor.execute(sql1)
    rows = cursor.fetchall()
    for row in rows:
        print('No:{0}, Email:{1}, Price:{2}, qty:{3},Created On:{4}'.format(row[0], row[1], row[2], row[3], row[4]))

#상품주문
def product_order(login_emial,user_or_item_id,user_or_qty):
    #주문 갯수 만큼 기존 주문리스트 재고에서 빼준다,

    #이게 error만듬 (%s빼먹음 ->)
    or_select_Sql = 'Select num, product_name, product_price, product_qty, created_at FROM item WHERE product_name = %s '
    cursor.execute(or_select_Sql,(user_or_item_id))
    while True:
            row = cursor.fetchone()
            if row == None:
                break
            user_or_price = row[2] *user_or_qty
    
    
    
    #주문등록
    or_insertSql = """INSERT INTO _order(num, member_id, item_id, order_qty, order_price,created_at) VALUES(null, %s, %s, %s, %s, NOW()) """
    #값을 안넣고 싶으면 null을 넣는다! None값이 들어감...
    sql1 = 'Select num, member_id, item_id, order_qty, order_price, created_at FROM _order'
    cursor.execute(sql1)
    cursor.execute(or_insertSql,(login_emial, user_or_item_id, user_or_qty, user_or_price))
    conn.commit()
    #등록확인(없어도됨)
    sql1 = 'Select num, member_id, item_id, order_qty, order_price, created_at FROM _order'
    cursor.execute(sql1)
    rows = cursor.fetchall()
    
    for row in rows:
        print('주문번호:{0}, 회원 Email:{1}, 상품명:{2}, 주문갯수:{3}, 주문 총액:{4}, 주문시간:{5} '.format(row[0], row[1], row[2], row[3], row[4],row[5]))
    print('등록완료')
    