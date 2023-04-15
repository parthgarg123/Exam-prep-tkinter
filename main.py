from openpyxl import workbook,load_workbook
import pandas as pd
import random
excel_file='EXAM PREP.xlsx'
wb= load_workbook(excel_file)
ws= wb.active
df = pd.read_excel(excel_file, header=1)
new_json = df.to_json()

no_corr_ans = 0
for i in range(5):
    j = random.randint(0,55)
    print(df['QUES'][j])
    for i in range(1,5):
        string1 = f'OPT{i}'
        print(f'{i}. {df[string1][j]}')
    corr_ans = df['ANS'][j]
    ans = input()
    if ans == corr_ans[-1]:
        print('Correct ans')
        no_corr_ans+=1
    else:
        print('Wrong ans')

print(f"Total Score: {no_corr_ans}/5")