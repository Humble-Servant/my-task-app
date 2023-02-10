import streamlit as st
import functions

tasks = functions.get_tasks()

st.set_page_config(layout="wide")

def add_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    functions.write_tasks(tasks)
    st.session_state["new_task"] = ""


st.title("My Task List")
st.subheader("This is my To-Do web app.")
st.write("Enter tasks and then check them off when <b>completed</b>.", unsafe_allow_html=True)

st.text_input(label=" ", placeholder="Enter a task...", on_change=add_task, key="new_task")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_tasks(tasks)
        del st.session_state[task]
        st.experimental_rerun()
        
        
