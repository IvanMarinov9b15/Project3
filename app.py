import streamlit as st

st.title("Streamlit Упражнения - Версия със Слайдъри")

st.header("1. Отношение към Python")
answer1 = st.radio("Обичаш ли Python?", ("да", "не"))

if answer1 == "да":
    st.success("Супер!")
else:
    st.info("Ще го харесаш!")

st.divider()

st.header("2. Проверка на число")
num = st.slider("Избери число:", min_value=0, max_value=20, value=0)

if num > 10:
    st.write(f"Числото {num} е **голямо**.")
else:
    st.write(f"Числото {num} е **малко**.")

st.divider()import streamlit as st

st.title("Streamlit Упражнения")

st.header("1. Отношение към Python")
answer1 = st.radio("Обичаш ли Python?", ("да", "не"))

if answer1 == "да":
    st.success("Супер!")
else:
    st.info("Ще го харесаш!")

st.divider()

st.header("2. Проверка на число")
num = st.number_input("Въведи число:", step=1)

if num > 10:
    st.write(f"Числото {num} е **голямо**.")
else:
    st.write(f"Числото {num} е **малко**.")

st.divider()

st.header("3. Математически тест")
math_answer = st.number_input("Колко е 5 × 5?", step=1, value=0)

if st.button("Провери"):
    if math_answer == 25:
        st.success("Вярно! Точно 25.")
    else:
        st.error(f"Грешно. Опитай пак.")
