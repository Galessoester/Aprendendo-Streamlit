import streamlit as st
from pandas import read_csv

st.markdown('''
# Exibidor de arquivos
            
## Suba seus arquivos e vejamos o que acontece
''')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui',
    type=['jpg','png','py', 'mp4', 'csv', 'json']
)

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'image', _:
            st.image(arquivo)
        case 'video', 'mp4':
            st.video(arquivo)
        case 'text', 'csv':
            df = read_csv(arquivo)
            st.dataframe(df)
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
else:
    st.error('Ainda não tenho arquivo')