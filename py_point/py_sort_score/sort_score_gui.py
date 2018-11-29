import PySimpleGUI as sg
import xlrd
import sqlite3
import numpy as np
import pandas as pd

'''
conn = sqlite3.connect(':memory:')
c = conn.cursor()

'''

# 考号,姓名,班级,成绩
rows = [
    [sg.Text('请选择原始数据文件...')],
    [sg.InputText(),sg.FileBrowse('浏览...')],
    [sg.Submit('提交'), sg.Cancel('取消')]
]

(button, (source_file,)) = sg.Window('选择文件').Layout(rows).Read()

data = xlrd.open_workbook(filename=source_file, encoding_override="cp936")
table = data.sheets()[0]


nrows = table.nrows
#print(nrows)
row_vals = []
for i in range(nrows):
    rv = table.row_values(i, start_colx=0, end_colx=None)
    rv_tup = tuple(rv)
    row_vals.append(rv_tup)

row_vals.sort(key=lambda student: student[3], reverse=True)

'''
c.executemany('INSERT INTO scores (student_no, name, class, score) VALUES (?,?,?,?)', row_vals)


conn.commit()
rank = {}
for res in c.execute('SELECT score FROM scores GROUP BY score ORDER BY score DESC'):
    print(res)
    


for res in c.execute('SELECT * FROM scores'):
    print(res)

conn.close()
'''


