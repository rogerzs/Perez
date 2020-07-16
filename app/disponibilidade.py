# import pyodbc
import pandas as pd
import streamlit as st
import datetime
from datetime import date
import pyodbc





server = '191.209.82.193,61112'
database = 'fit'
username = 'robinson'
password = 'SuperEACH!2020'
connection_string = 'Driver={FreeTDS};Server=' + server + ';Database=' + database+ ';UID=' + username + ';PWD=' + password + ';'
cnxn = pyodbc.connect(connection_string)
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


global proximo_id
query = 'SELECT max(id_reserva) as ultimo FROM tb_reserva_salasquash'+ '\n'
df = pd.read_sql(query,cnxn)
proximo_id = df['ultimo']
proximo_id = proximo_id + 1


def ver_disponibilidade(data):

    st.write("Estas são as salas e horários já reservados \n")
    query = """
                         SELECT id_sala, dthr_reserva, observacao
                         FROM tb_reserva_salasquash
                         WHERE CAST(dthr_reserva as DATE) = '{}'
                         """.format(data) + '\n'

    df = pd.read_sql(query, cnxn)

    st.write(df)
