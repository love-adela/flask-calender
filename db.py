import psycopg2

# 전역 connection 객체
conn = psycopg2.connect('dbname=calenderdb user=adela')
cursor = conn.cursor()
cursor.execute('''
        create table if not exists account(
        id serial primary key, 
        username text not null,
        password_hash text not null,
        password_salt text not null
        );
        create index if not exists ix_account_username on account(username);
  ''')

cursor.close()
conn.commit()
