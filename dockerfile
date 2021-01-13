FROM python:slim

WORKDIR /usr/src/app

COPY module1.py .
COPY user_manager.py .
COPY admin_manager.py .

RUN pip install pymysql

ENTRYPOINT [ "python","./module1.py" ]
