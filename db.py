import psycopg2

# 전역 connection 객체
conn = psycopg2.connect('dbname=calenderdb user=adela')
cursor = conn.cursor()
cursor.execute('''
        create table if not exists account(
        id serial primary key, 
        username text not null,
        password text not null
        );
  ''')

cursor.close()
conn.commit()
