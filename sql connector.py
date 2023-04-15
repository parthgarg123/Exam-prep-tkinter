import mysql.connector
import pandas as pd

conn = mysql.connector.connect(host = 'localhost',user ='root',passwd = "Qseytak144469@",database='ques_data')
cur = conn.cursor()
cur.execute('use ques_data')
'''
cur.execute('select * from questions')
result = cur.fetchall()
for i in result:
    print(i)
'''



def select_sub(sub_code,sub_sec='',limit = 5):
    cur = conn.cursor()
    cur.execute('''
    select ques,opt1,opt2,opt3,opt4,ans from questions 
    where sub_code = %s and sub_sec= %s
    order by RAND() limit %s''',(sub_code,sub_sec,limit,))
    result = cur.fetchall()
    return result

result1 = select_sub(sub_code ="23MA",sub_sec='Calculus')
no_corr_ans = 0
for i in result1:
    print(i[0])
    for j in range(1,5):
        print(f'{j}. {i[j]}')
    corr_ans = i[5][-1]
    ans = input()
    if ans == corr_ans:
        print('Correct ans')
        no_corr_ans += 1
    else:
        print('Wrong ans')

print(f"Total Score: {no_corr_ans}/5")