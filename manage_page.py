import streamlit as st
import data as dt


def edit_task():
  data = dt.fetch_all_task()
  st.write(data)
  task_name = st.selectbox('Selection your Task',data['task_name'])
  selected_task = dt.get_task_by_taskname(task_name)
  if not selected_task.empty:
      col1, col2 = st.columns(2)
      
      with col1:
          new_task_name = st.text_input('Task Name', value=selected_task.iloc[0]['task_name'])
          new_task_status = st.selectbox('Task Status', ['To Do', 'Rejected', 'In Progress', 'UAT', 'Done'], index=['To Do', 'Rejected', 'In Progress', 'UAT', 'Done'].index(selected_task.iloc[0]['task_status']))
      
      with col2:
          new_task_due_date = st.date_input('Due Date', value=selected_task.iloc[0]['task_due_date'])
          new_task_area = st.text_area('Task Area', value=selected_task.iloc[0]['task_area'])
      
      if st.button('Update'):
        dt.update_task(new_task_name,new_task_status,new_task_due_date,new_task_area,task_name)
        st.success('Task has been updated')
        


def delete_task():
  data = dt.fetch_all_task()
  st.write(data)
  task_name = st.selectbox('Selection your delete Task',data['task_name'])
  selected_task = dt.get_task_by_taskname(task_name)
   
  if st.button('Delete'): 
    if not selected_task.empty:
      dt.delete_task_by_taskname(task_name)
      st.success('Your Task has been deleted')

