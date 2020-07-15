import pyodbc
import pandas as pd
import streamlit as st
import datetime
from datetime import date
pyodbc.drivers()


server = '191.209.82.193,61112'
database = 'fit'
username = 'robinson'
password = 'SuperEACH!2020'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def ver_socio(socio_id):
    analysis_type = st.multiselect(
        'Escolha o tipo de visualização',
        ['Ver Histórico de Reservas',
         'Ver Data Específica']
    )


    if 'Ver Histórico de Reservas' in analysis_type:
        query_historical(socio_id)
    if 'Ver Data Específica' in analysis_type :
        query_date(socio_id)





def query_historical(socio_id):
    query = """
                        SELECT *
                        FROM tb_reserva_salasquash
                        WHERE (id_socio1 = '{0}' OR id_socio2 = '{0}')
                """.format(socio_id)

    df = pd.read_sql(query, cnxn)
    st.write(df)


def query_date(socio_id):
    start_time = st.date_input(label='Escolha a Data',
                                 value=date(2020, 3, 2))

    query = """
                    SELECT *
                    FROM tb_reserva_salasquash
                    WHERE (id_socio1 = '{0}' or id_socio2 = '{0}')  and CAST(dthr_reserva as DATE) = '{1}'
            """.format(socio_id,start_time)
    df = pd.read_sql(query, cnxn)
    st.write(df)