import streamlit as st
from datetime import datetime, timedelta

st.title('Formulário')

st.text_input('Email')
st.text_input('Senha', type='password', max_chars=12)

data_atual = datetime.today().date()
data_minima = data_atual - timedelta(days=365*100)
st.date_input('Aniversário', max_value=data_atual, min_value=data_minima, format='DD/MM/YYYY',)