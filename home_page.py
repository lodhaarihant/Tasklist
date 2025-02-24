import streamlit as st
import data as dt


def home_page():
  dt.create_table()
  
  col1,col2 = st.columns(2)
  with col1:
    task_name = st.text_input('Task Sub')
    task_status = st.selectbox('Select your Status',['To Do','Rejected','In Progress','UAT','Done'])
   
  with col2:
    task_due_date = st.date_input('Task Date')
    task_area = st.text_area('Enter your Text')
    
  if st.button('Submit'):
    dt.add_task(task_name, task_status, task_due_date, task_area)
    st.success('Task:{} has been created'.format(task_name))
    data = dt.fetch_all_task()
    st.write(data)
    
    
def search_task():
  st.subheader("Search Task")
  search_term = st.text_input("Search Term")
  search_choice = st.radio("Field To Search",("Task Name","Task Date"))
  if st.button("Search"):
    if search_choice == "Task Name":
        search_result = dt.get_task_by_taskname(search_term)
        st.write(search_result)
    else:
        search_result = dt.get_task_by_taskdate(search_term)
        st.write(search_result)
   