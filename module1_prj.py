import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password= '',port=3306,db='mydb',charset='utf8')
cursor = conn.cursor()
import user_manager

while True:

    #메 인화면
    print('#'*50)
    print('\n1. 회원 로그인    \n2. 관리자 로그인\n')
    print('#'*50)
    user = int(input('\n\n입력:'))

    #회원 로그인
    if user == 1:
        print('#'*50)
        print('\n1. 회원 로그인 화면\n')
        print('#'*50)
        login_emial = str(input('Email:'))
        login_pwd = str(input('PWD:'))

       #회원 로그입 접속환경
       #모든 작업이 끝나면 여기로 복귀하고 로그 아웃화면 만들어야됨...
        if user_manager.user_login(login_emial,login_pwd) ==1:
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


        

    else:
        print('d')
    #     print('1. 상품목록 조회 \n2.상품주문')
    #     if select == 1:
    #         print('상품목록 조회')
    #     elif select == 2 :
    #         print('상품주문')1