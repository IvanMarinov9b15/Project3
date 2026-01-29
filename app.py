import streamlit as st

# Заглавие на цялото приложение
st.title("Streamlit Упражнения - Пълен пакет")

st.header("1. Отношение към Python")
answer1 = st.radio("Обичаш ли Python?", ("да", "не"))

if answer1 == "да":
    st.success("Супер!")
else:
    st.info("Ще го харесаш!")

st.divider() 

st.header("2. Проверка на число")
num = st.number_input("Въведи число:", value=0)

if num > 10:
    st.write("Голямо число")
else:
    st.write("Малко число")

st.divider()

st.header("3. Математически тест")
math_answer = st.number_input("Колко е 5 × 5?", step=1)

if st.button("Провери"):
    if math_answer == 25:
        st.success("Вярно!")
    else:
        st.error("Грешно. Опитай пак")
