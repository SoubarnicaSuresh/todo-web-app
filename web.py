import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my to-do app with a list of my to-dos.")
st.write("This app will increase your productivity!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter here: ", placeholder="Add new to-do:",
              on_change=add_todo, key='new_todo')
