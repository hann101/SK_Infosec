import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password= '',port=3306,db='mydb',charset='utf8')
cursor = conn.cursor()
import user_manager
import admin_manager


while True:

    #메 인화면
    print('#'*50)
    print('\n1. 회원 로그인    \n2. 관리자 로그인\n')
    print('#'*50)
    user = int(input('\n\n입력:'))

    #회원 로그인
    if user == 1:
        print('#'*50)
        print('\n1. 회원 로그인 화면\n ')
        print('#'*50)
        login_emial = str(input('Email:'))
        login_pwd = str(input('PWD:'))

       #회원 로그입 접속환경
       #모든 작업이 끝나면 여기로 복귀하고 로그 아웃화면 만들어야됨...
        
        if user_manager.user_login(login_emial,login_pwd) ==1:
                while True:
                    print('#'*50)
                    print('\n1. 상품목록 조회 \n2. 상품주문\n')
                    print('#'*50)
                    user_input = int(input('입력:'))
                    

                    #상품목록조회
                    if user_input == 1:
                        user_manager.product_list(login_emial)
                    elif user_input == 2:
                            
                        user_or_item_id = input('상품명:')
                        user_or_qty  = int(input('주문갯수:'))
                        # or_regist_order_price = int(input('주문가격:')) 
                        user_manager.product_order(login_emial, user_or_item_id, user_or_qty)    

    #관리자
    elif user == 2:
        print('#'*50)
        print('\n1. 관리자 로그인 화면\n')
        print('#'*50)
        login_admin = str(input('Email:'))
        login_adminpwd = str(input('PWD:'))

        if login_admin == 'admin' and login_adminpwd =='admin1234':
            print('\n접속허용')
            print('#'*50)

            #관리자화면
            while True:
                print('\n1. 회원관리 \n2. 주문관리 \n3. 상품관리\n')
                print('#'*50)
                admin_input = int(input('입력'))
                
                if admin_input == 1:
                    
                    print('#'*50)
                    print('\n회원관리\n \n1.등록 \n-2.수정 \n-3.삭제\n \n4.회원검색 \n5.전체회원목록\n')
                    print('#'*50)
                    sel_1 = int(input('\n실행:'))
                    
                    #등록
                    if sel_1 == 1:
                        ad_useremail = input('회원 Email:')
                        ad_userpwd = input('회원 PWD:')
                        admin_manager.ad_user_regist(ad_useremail,ad_userpwd)
                        print('회원등록완료')                        
 
                    #수정
                    elif sel_1 == 2:
                        repair_email = input('PWD수정(email 입력):')
                        repair_pwd = input('PWD수정(수정할 PWD입력):')
                        admin_manager.ad_user_repair(repair_email,repair_pwd)
                    
                    #삭제
                    elif sel_1 == 3:
                        del_email = input('삭제(Email입력):')
                        admin_manager.ad_user_delete(del_email)
                        print('회원이 삭제 되었습니다.')
           
                    #개인계정찾기
                    elif sel_1 == 4:
                        ad_search_user = input('Email 입력:')
                        admin_manager.ad_oneuser_search(ad_search_user)

                    #전체회원목록
                    elif sel_1 == 5:
                        
                        admin_manager.ad_alluser_search() 

                #주문관리
                elif admin_input == 2:
                    admin_input = 0
                    print('#'*50)
                    print('\n주문관리\n \n1.등록 \n2.수정 \n3.삭제 \n4.목록조회\n')
                    print('#'*50)
                    sel_2 = int(input('\n실행'))
                    
                    #주문등록
                    if sel_2 == 1:
                        or_regist_member_id = input('member_id:')
                        or_regist_item_id = input('item_id:')
                        or_regist_order_qty  = int(input('주문갯수:'))
                        or_regist_order_price = int(input('주문가격:'))
                        admin_manager.order_add(or_regist_member_id,or_regist_item_id,or_regist_order_qty,or_regist_order_price)
                    
                    #주문수정
                    elif sel_2 ==2:
                        or_reapair_email =input('Email:')
                        or_reapair_name = input('(수정)상품명:')
                        or_repair_price = input('(수정)상품가격:')
                        or_repair_qty  = input('(수정)상품갯수:')
                        admin_manager.order_update(or_reapair_email,or_reapair_name,or_repair_price,or_repair_qty)
                        
                    #주문삭제
                    elif sel_2 ==3:
                        or_delete_num = input("(삭제)주문번호:")
                        admin_manager.order_delete(or_delete_num)
                    #목록조회 
                    elif sel_2 ==4:
                        print('#'*50)
                        print('\n목록조회 \n1.전체주문목록 \n2.회원별 주문 목록 \n3.주/월별 최다 금액 주문자 \n4.주/월별 최다 주문상품\n')
                        print('#'*50)
                        sel_24 = int(input('\n입력:'))
                        #전체주문목록
                        if sel_24 == 1:
                            admin_manager.orderList_read()

                        #회원별 주문 목록
                        elif sel_24 ==2:
                            or_search_email =input('Email:')
                            admin_manager.orderMember_read(or_search_email)
                        
                        #   주/월별 최다 금액 주문자
                        elif sel_24 ==3:
                            print('#'*50)
                            print('\n2.회원별 주문 목록\n \n1.주별 최다 금액 주문자 \n2.월별 최다 금액 주문자\n')
                            print('#'*50)                               
                            sel_243 = int(input('입력:'))

                            #주별 최다 금액주문자
                            if sel_243 ==1: 
                                admin_manager.or_Weeklybuyer()

                            # 월별
                            # elif sel_243 ==2: 


                        # #주/월별 최다 주문상품
                        # elif sel_24 ==4:

                #상품관리
                elif admin_input == 3:

                    print('#'*50)
                    print('\n상품관리\n \n1.등록\n2.수정 \n3.삭제 \n')
                    print('#'*50)
                    sel_3 = int(input('입력:'))

                    #등록
                    if sel_3 ==1:
                        pd_regist_name = input('상품명:')
                        pd_regist_price = input('상품가격:')
                        pd_regist_qty  = input('상품갯수:')
                        admin_manager.item_add(pd_regist_name,pd_regist_price,pd_regist_qty)
                        admin_manager.itemList_select()
                    #수정
                    elif sel_3 ==2:
                        pd_reapair_name = input('상품명:')
                        pd_repair_price = input('(수정)상품가격:')
                        pd_repair_qty  = input('(수정)상품갯수:')
                        admin_manager.item_update(pd_repair_price,pd_repair_qty,pd_reapair_name)
                    #삭제               
                    elif sel_3 ==3:
                        pd_del_name = input('(삭제)상품명 입력:')
                        admin_manager.item_delete(pd_del_name)
                    
                    admin_input = 0

        else:
            print('접속불가')
