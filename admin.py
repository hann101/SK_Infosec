#Database 불러오기
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password= '',port=3306,db='mydb',charset='utf8')
cursor = conn.cursor()




while True:
    print('*'*50 )
    print('1.회원관리 \n2.상품관리 \n3.주문관리' )
    print('*'*50 )
    menu = int(input("번호 입력:"))
    #회원관리
    if menu == 1:
        print('-'*10)
        sel_1 = int(input('회원관리\n \n1.등록/수정/삭제 \n2.검색 \n3.로그인 \n4.주문내역조회 \n실행:'))
        #로그인 없어도되고
        


        if sel_1 == 1:
            print('-'*10)
            num = int(input('-1.등록 \n-2.수정 \n-3.삭제 \n실행:'))
            
            #등록
            if num == 1:
                insertSql = """INSERT INTO member(num, email, pwd, created_at) VALUES(null, %s, %s, NOW()) """
                print('-'*10)
                email_input = input('Email:')
                pwd_input = input('Pass Word:')
                cursor.execute(insertSql,(email_input,pwd_input))
                conn.commit()
                #등록확인
                sql1 = 'SELECT num, email,pwd, created_at FROM member'
                cursor.execute(sql1)
                rows = cursor.fetchall()
                
                for row in rows:
                    print('No:{0}, Email:{1}, Password:{2}, Created On:{3}'.format(row[0], row[1], row[2], row[3]))
            
            #수정
            elif num == 2 :
                print('-'*10)
                repair_email = input('PWD수정(email 입력):')
                repair_pwd = input('PWD수정(수정할 PWD입력):')

                repair_sql = """ UPDATE member SET pwd= %s WHERE email=%s """
                cursor.execute(repair_sql,(repair_pwd,repair_email))
                conn.commit()
                print('변경되었습니다.')

            #삭제
            elif num == 3:
                print('-'*10)
                del_email = input('삭제(Email입력):')
                deleteSql = '''DELETE FROM member WHERE email = %s'''
                cursor.execute(deleteSql, (del_email))
                conn.commit()
                print('회원이 삭제 되었습니다.')
            
            sel = 0

        #검색 
        elif sel_1 == 2:
            search_email = str(input('검색(email):'))
            select_Sql = '''SELECT num, email, pwd, created_at FROM member WHERE email = %s'''
            cursor.execute(select_Sql,(search_email))
            while True:
                row = cursor.fetchone()
                if row == None:
                    break
                print('No:{0}, Email:{1}, PassWord:{2}, Created date:{3}'.format(row[0], row[1], row[2], row[3]))

        #로그인  
        elif sel_1 == 3:
            login_emial = str(input('로그인_Email:'))
            login_pwd = str(input('로그인_PWD:'))
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
                    #권한 부여
                    acceses = 1
                else:
                    print('비밀번호가 다릅니다.')

        #주문조회  x(주문을 해야됨 while문에 try except넣어주기)
        elif sel_1 == 4:       
            or_search_email = str(input('검색(email 입력):'))
            or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order WHERE email = %s'''
            cursor.execute(or_select_Sql,(or_search_email))
            while True:
                row = cursor.fetchone()
                if row == None:
                    break
                print('No:{0}, member_id:{1}, item_id:{2}, order_qty:{3},order_price:{4},created_at{5}'.format(row[0], row[1], row[2], row[3],row[4],row[5]))
        
        
            print('주문내역조회: 조회완료')

    #상품목록
    elif menu == 2:
        print('-'*10)
        sel_2 = int(input('상품목록\n \n1.등록/수정/삭제 \n2.검색' ))
        
        #상품_등록/수정/삭제
        if sel_2 == 1:
            print('-'*10)
            num_2 = int(input('-1.등록 \n-2.수정 \n-3.삭제 \n실행:'))
            
            #상품_등록
            if num_2 == 1:
                pd_insertSql = """INSERT INTO item(num, product_name, product_price, product_qty, created_at) VALUES(null, %s, %s, %s, NOW()) """
                print('-'*10)
                pd_regist_name = input('상품명:')
                pd_regist_price = input('상품가격:')
                pd_regist_qty  = input('상품갯수:')

                cursor.execute(pd_insertSql,(pd_regist_name, pd_regist_price, pd_regist_qty))
                conn.commit()
                #등록확인
                sql1 = 'Select num, product_name, product_price, product_qty, created_at FROM item'
                cursor.execute(sql1)
                rows = cursor.fetchall()
                
                for row in rows:
                    print('No:{0}, name:{1}, price:{2}, qty:{3},Created On:{4}'.format(row[0], row[1], row[2], row[3], row[4]))
            
            #상품_수정 
            elif num_2 == 2 :
                print('-'*10)
                pd_reapair_name = input('상품명:')
                pd_repair_price = input('(수정)상품가격:')
                pd_repair_qty  = input('(수정)상품갯수:')


                pd_repair_sql = """ UPDATE item SET product_price= %s, product_qty =%s WHERE product_name=%s """
                cursor.execute(pd_repair_sql,(pd_repair_price,pd_repair_qty,pd_reapair_name))
                conn.commit()
                print('변경되었습니다.')

            #상품_삭제 
            elif num_2 == 3:
                print('-'*10)
                pd_del_name = input('(삭제)상품명 입력:')
                pd_deleteSql = '''DELETE FROM item WHERE product_name = %s'''
                cursor.execute(pd_deleteSql, (pd_del_name))
                conn.commit()
                print('상품이 삭제 되었습니다.')
            
            sel = 0
        #상품_검색
        elif sel_2 == 2:
            pd_search_name = str(input('(검색)상품명:'))
            pd_select_Sql = '''SELECT num, product_name, product_price, product_qty, created_at FROM item WHERE product_name = %s'''
            cursor.execute(pd_select_Sql,(pd_search_name))
            while True:
                row = cursor.fetchone()
                if row == None:
                    break
                print('No:{0}, 상품명:{1}, 가격:{2}, 갯수:{3}, 등록날짜:{4}'.format(row[0], row[1], row[2], row[3], row[4]))
    
    #주문관리
    elif menu == 3:
        print('-'*10)
        sel_3 = int(input('주문관리\n \n1.등록/수정/삭제 \n2.검색 \n3.상품수량 \n입력>' ))


        if sel_3 == 1:
            print('-'*10)
            num_3 = int(input('1-1.등록 \n1-2.수정 \n1-3.삭제 \n입력>:'))
            
            #주문_등록(상품 주문하기)
            if num_3 == 1:
                or_insertSql = """INSERT INTO _order(num, member_id, item_id, order_qty, order_price,created_at) VALUES(null, %s, %s, %s, %s, NOW()) """
                print('-'*10)
                or_regist_member_id = input('member_id:')
                or_regist_item_id = input('item_id:')
                or_regist_order_qty  = int(input('주문갯수:'))
                or_regist_order_price = int(input('주문가격:'))
                cursor.execute(or_insertSql,(or_regist_member_id, or_regist_item_id, or_regist_order_qty, or_regist_order_price))
                conn.commit()
                #등록확인
                sql1 = 'Select num, member_id, item_id, order_qty, order_price, created_at FROM _order'
                cursor.execute(sql1)
                rows = cursor.fetchall()
                
                for row in rows:
                    print('num:{0}, member_id:{1}, item_id:{2}, order_qty:{3}, order_price:{4}, Created at:{5} '.format(row[0], row[1], row[2], row[3], row[4],row[5]))
                print('등록완료')
            
            #주문_수정(주문한 것을 수정한다.) 
            elif num_3 == 2 :
                print('-'*10)
                pd_reapair_name = input('상품명:')
                pd_repair_price = input('(수정)상품가격:')
                pd_repair_qty  = input('(수정)상품갯수:')


                pd_repair_sql = """ UPDATE item SET product_price= %s, product_qty =%s WHERE product_name=%s """
                cursor.execute(pd_repair_sql,(pd_repair_price,pd_repair_qty,pd_reapair_name))
                conn.commit()
                print('변경되었습니다.')

            #주문_삭제 (주문한 것을 취소)
            elif num_3 == 3:
                print('-'*10)
                pd_del_name = input('(삭제)상품명 입력:')
                pd_deleteSql = '''DELETE FROM item WHERE product_name = %s'''
                cursor.execute(pd_deleteSql, (pd_del_name))
                conn.commit()
                print('상품이 삭제 되었습니다.')
            
            sel = 0
        #주문_검색(자신이 주문한 것을 확인할 수 있다.)
        elif sel_3 == 2:
            #주문 내역확인
            or_search_email = str(input('검색(email 입력):'))
            or_select_Sql = '''SELECT num, member_id, item_id, order_qty, order_price,created_at FROM _order WHERE member_id = %s'''
            cursor.execute(or_select_Sql,(or_search_email))
            while True:
                row = cursor.fetchone()
                if row == None:
                    break
                print('No:{0}, member_id:{1}, item_id:{2}, order_qty:{3},order_price:{4},created_at{5}'.format(row[0], row[1], row[2], row[3],row[4],row[5]))

        #주문_상품수량 수정
        elif sel_3 == 3:
                print('-'*10)
                pd_reapair_name = input('상품명:')
                pd_repair_price = input('(수정)상품가격:')
                pd_repair_qty  = input('(수정)상품갯수:')


                pd_repair_sql = """ UPDATE item SET product_price= %s, product_qty =%s WHERE product_name=%s """
                cursor.execute(pd_repair_sql,(pd_repair_price,pd_repair_qty,pd_reapair_name))
                conn.commit()
                print('변경되었습니다.')

