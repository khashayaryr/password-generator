import streamlit as st
from password_generator import PinPassword, RandomPassword, MemorablePassword


st.image("src/data/banner.jpg", use_container_width=True)
st.title(":key: Password Generator")

st.write("Within this app, you can create strong passwords. "
"Below, you can switch between different tabs to generate a PIN code, "
"a random strong password, or a memorable password made up of meaningful words.")

tab1, tab2, tab3 = st.tabs(["PIN Code", "Random Password", "Memorable Password"])

with tab1:
    length = st.slider("Length", min_value=4, max_value=12, value=4)
    generator = PinPassword(length)
    password = generator.generate()
    button = st.button("Generate", key='pin', type="primary")
    if button:
        st.code(password, language=None)

with tab2:
    length = st.slider("Length", min_value=8, max_value=32, value=12)
    numbers = st.toggle("Include Numbers")
    special_chars = st.toggle("Include Symbols",)
    generator = RandomPassword(length=length, numbers=numbers, special_chars=special_chars)
    password = generator.generate()
    button = st.button("Generate", key='random', type="primary")
    if button:
        st.code(password, language=None)


with tab3:
    words_num = st.slider("Number of Words", min_value=2, max_value=16, value=6)
    separator = st.text_input("Separator", value='-')
    capitalize = st.toggle("Capitalized Words")
    generator = MemorablePassword(words_num=words_num, separator=separator, capitalize=capitalize)
    password = generator.generate()
    button = st.button("Generate", key='memorable', type="primary")
    if button:
        st.code(password, language=None)
