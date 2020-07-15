import pandas as pd
from sqlalchemy import create_engine
from math import sqrt
import numpy as np
import streamlit as st
from datetime import datetime,timedelta,date

#import different visions
## VDE
## Viagem de Short
## Viagem de LONG
## %Viagem de LONG
## VDE real/previsto
from verificar_socio import ver_socio
from disponibilidade import ver_disponibilidade
from reserva import reservar_sala


st.title('Projeto Academia')
st.subheader('Acesse o Menu ao Lado')



analysis = st.sidebar.multiselect(
     'Escolha uma das opções',
     ['Ver Disponibilidade de Sala',
      'Fazer Reserva de Sala',
      'Ver reservas de um sócio']
    )

## Analysis Display

if 'Ver Disponibilidade de Sala' in analysis:
    start_period = st.date_input(label='Dia de início das análises',
                                 value=date(2020, 3, 2))
    ver_disponibilidade(start_period)


if 'Ver reservas de um sócio' in analysis:
    socio_id = st.text_input(label='Digite o ID do sócio')
    ver_socio(socio_id)

if 'Fazer Reserva de Sala' in analysis:
    sala = st.text_input(label = 'Digite o Número da Sala')
    socio_id = st.text_input(label='Digite o ID do sócio')
    socio_id2 = st.text_input(label='Digite o ID do segundo sócio')
    start_period = st.date_input(label='Data da Reserva',
                                 value=date(2020, 3, 2))
    observacao = st.text_input(label='Observação ou motivo da reserva')

    reservar_sala(sala,socio_id,socio_id2,start_period,observacao)



from PIL import Image
image = Image.open('cross-fit-rope-workout.jpg')


st.image(image, caption='SE LIGA NO TREINO!',
      use_column_width=True)
