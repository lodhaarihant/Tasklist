import streamlit as st
import home_page as hp
import manage_page as mp
import post_page as pp
import data as dt



def main():
  st.write('Welcome to TaskManager')
  menu = ['Home','Edit Task','Delete Task','Search Task','Analytics','About']
  choice = st.sidebar.selectbox('Menu',menu)
  
  
  if choice == 'Home':
    st.divider()
    st.write('Add Task')
    hp.home_page()
  elif choice == 'Edit Task':
    st.write('Edit Task')
    mp.edit_task()
  elif choice == 'Delete Task':
    st.write('DeleteTask')
    mp.delete_task()
  elif choice == "Analytics": 
    st.write('Analytics')
    pp.analytics()
  elif choice == "Search Task": 
    hp.search_task()
  
    
  elif choice == 'About':
    st.write('Made with Love')
  
  
if __name__ == '__main__':
  main()
  
  