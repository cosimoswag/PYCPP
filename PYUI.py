import CPPCLASS
import streamlit as st

# App title
st.title("CALCOLATRICE")
cppC = CPPCLASS.FUNCT()
# Input field


# Button with action
if st.button("Process"):
    if input:
        st.success(f"Processed: {input.upper()}")
    else:
        st.warning("Perfavore, immetti un numero.")


# Additional widget examples

colonne1,colonne2,colonne3 = st.columns([10,10,10])
col1, col2, col3 = st.columns(3)

with colonne1:
    if st.button("    7   "):
        st.text("7")

with colonne2:
    number = st.button('    8   ')
with colonne3:
    number = st.button('    9   ')
with colonne1:
    number = st.button('    4   ')
with colonne2:
    number = st.button('    5   ')
with colonne3:
    number = st.button('    6   ')
with colonne1:
    number = st.button('    1   ')
with colonne2:
    number = st.button('    2   ')
with colonne3:
    number = st.button('    3   ')

