import sqlite3 as sql
import pandas as pd
conn = sql.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table():
  query = 'CREATE TABLE IF NOT EXISTS tasktable(task_name TEXT,task_status TEXT,task_due_date DATE, task_area TEXT)'
  c.execute(query)


def add_task(task_name,task_status,task_due_date,task_area):
  query = 'Insert into tasktable (task_name,task_status,task_due_date,task_area) Values(?,?,?,?)'
  c.execute(query,(task_name,task_status,task_due_date,task_area))
  conn.commit()
  

def fetch_all_task():
  query = 'Select * from tasktable'
  c.execute(query)
  data = c.fetchall()
  return pd.DataFrame(data,columns=['task_name','task_status','task_due_date','task_area'])


def get_task_by_taskname(task_name):
  query= 'select * from tasktable where task_name = ?'
  data = c.execute(query,(task_name,))
  return pd.DataFrame(data,columns=['task_name','task_status','task_due_date','task_area'])
  

def get_task_by_taskdate(task_date):
  query= 'select * from tasktable where task_name = ?'
  data = c.execute(query,(task_date,))
  return pd.DataFrame(data,columns=['task_name','task_status','task_due_date','task_area'])
  


def update_task(task_name,task_status,task_due_date,task_area,old_task_name):
  query = 'update tasktable  set task_name = ? ,task_status = ?,task_due_date = ? ,task_area = ? where task_name = ?'
  c.execute(query,(task_name,task_status,task_due_date,task_area,old_task_name))
  conn.commit()
  
  
def delete_task_by_taskname(task_name):
    query= 'Delete from tasktable where task_name = ?'
    c.execute(query,(task_name,))
    conn.commit()
    
  
