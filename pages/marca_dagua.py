import streamlit as st
from PIL import Image, ImageFont, ImageDraw

st.markdown('''
# Adicionar marca d'água
''')

def textOnImage(imagem, texto, cor, tamanho_fonte):
    img = Image.open(imagem)
    font = ImageFont.truetype('fonts/PlaypenSans-Regular.ttf', tamanho_fonte)
    draw = ImageDraw.Draw(img)
    
    iw, ih = img.size
    fw, fh = font.getsize(texto)
    
    draw.text(
        ((iw - fw) / 2, (ih - fh) / 2), 
        texto, 
        fill=cor, 
        font=font)
    img.save('imagem_final.jpg')
    

imagem = st.file_uploader(
    'Suba seu imagem aqui',
    type=['jpeg', 'jpg']
)

if imagem:
    texto = st.text_input('Sua marca d\'água')
    cor = st.color_picker('Cor da sua marca')
    tamanho_fonte = st.number_input('Tamanho da fonte', min_value=50)
    result = st.button(
        'Aplicar',
        type='primary',
        on_click=textOnImage,
        args=(imagem, texto, cor, tamanho_fonte)
    )
    if result:
        st.image('imagem_final.jpg')
        with open('imagem_final.jpg', 'rb') as file:
            st.download_button(
                'Baixe agora mesmo',
                file_name='imagem_com_marc.jpg',
                data = file,
                mime='image/jpg'
            )

else:
    st.error('Ainda não tenho imagem')