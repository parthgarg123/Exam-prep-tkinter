import pymysql
import pandas as pd

conn = pymysql.connect(host = 'localhost',user ='root',passwd = "Qseytak144469@",database='ques_data')
cur = conn.cursor()
cur.execute('use ques_data')
df= pd.read_excel('EXAM PREP.xlsx')
cur.execute('''CREATE TABLE IF NOT EXISTS QUESTIONS(
STD varchar(10),
SUB_CODE varchar(20),
SUB_SEC varchar(20),
QUES varchar(500),
OPT1 varchar(300),
OPT2 varchar(300),
OPT3 varchar(300),
OPT4 varchar(300),
ANS varchar(5)
);
''')
length = len(df)
for i in range(1, length):
    record = tuple(df.loc[i])
    sentence1 = 'INSERT INTO QUESTIONS (STD,SUB_CODE,SUB_SEC,QUES,OPT1,OPT2,OPT3,OPT4,ANS) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    sentence1 = sentence1.replace('nan','null').replace('None','null').replace('none','null')
    cur.executemany(sentence1,[record])

cur.close()
conn.commit()
conn.close()





'''
engine = create_engine('mysql+pymysql://root:Qseytak144469@localhost:3306/ques_data')
df.to_sql('QUESTIONS',con=engine, if_exists='append',index = False)
'''