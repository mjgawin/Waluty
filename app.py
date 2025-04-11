import streamlit as st
import program

st.title("Witaj!")


iso = st.text_input("Podaj walutę: [Kod ISO waluty]")
if iso:
    st.write(f"Wpisany tekst: {iso}")

dzien = st.text_input("Podaj datę (RRRR-MM-DD): ")
if dzien:
    st.write(f"Wybrana data: {dzien}")

if st.button("Podaj kurs NBP"):
    if iso and dzien:
        kurs = program.pobierz_kurs(iso, dzien)
    st.write(f"Kurs {iso} na dzień {dzien} to: {kurs}")

