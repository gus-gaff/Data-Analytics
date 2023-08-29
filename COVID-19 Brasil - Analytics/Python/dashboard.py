import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

basededados = pd.read_excel('base/COVID-19 Brasil - Analytics.xlsx')

st.set_page_config(
    page_icon="🇧🇷",
    page_title="COVID-19 - Brasil - Analytics",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'mailto:gustavocostasilva505@gmail.com',
        'Report a bug': "mailto:gustavocostasilva505@gmail.com",
        'About': "###### © 2023 Gustavo Costa Silva All Rights Reserved"
    }
)

st.sidebar.title("Filtrar por:")
st.sidebar.info("Ano + Mês")

Ano = st.sidebar.multiselect(
                                "Ano:",
                                options=basededados["Ano"].unique(),
                                default=basededados["Ano"].unique(),
                                placeholder="Selecione o ano",
                                key='ano_multiselect'
                                )

Mes = st.sidebar.multiselect(
                                "Mês:",
                                options=basededados["Mês"].unique(),
                                default=basededados["Mês"].unique(),
                                placeholder="Selecione o mês",
                                key='mes_multiselect'
                                )

basededados_filtro = basededados.query(
    "Ano == @Ano & Mês == @Mes"
)

st.title(":chart_with_upwards_trend: COVID-19 - Brasil - Analytics")
st.subheader("Impacto da COVID-19 no Brasil - Uma análise acumulativa (2020-2023)")

st.markdown("###")

left_column, center_column, right_column = st.columns(3)

casosconfirmados_icone = Image.open('images/casosconfirmados_icon.png')
left_column.image(casosconfirmados_icone, width=60)
obitos_icone = Image.open('images/obitos_icon.png')
center_column.image(obitos_icone, width=60)
casosrecuperados_icone = Image.open('images/casosrecuperados_icon.png')
right_column.image(casosrecuperados_icone, width=60)

kpi_casosconfirmados = (basededados_filtro["Casos Confirmados (Acumulativo)"].max())
kpi_obitos = (basededados_filtro["Óbitos (Acumulativo)"].max())
kpi_casosrecuperados = (basededados_filtro["Casos Recuperados (Acumulativo)"].max())

left_column, center_column, right_column = st.columns(3)

with left_column:
    st.markdown("##### Casos confirmados (acumulativo)")
    st.subheader(f'{kpi_casosconfirmados:,.0f}')
with center_column:
    st.markdown("##### Óbitos (acumulativo)")
    st.subheader(f'{kpi_obitos:,.0f}')
with right_column:
    st.markdown("##### Casos recuperados (acumulativo)")
    st.subheader(f'{kpi_casosrecuperados:,.0f}')

st.markdown("---")
st.markdown("###")

config_grafico_casosconfirmados = (
    basededados_filtro.groupby(by=["Ano"]).max()
)

config_grafico_obitos = (
    basededados_filtro.groupby(by=["Ano"]).max()
)

config_grafico_casosrecuperados = (
    basededados_filtro.groupby(by=["Ano"]).max()
)

grafico_casosconfirmados = px.bar(
    config_grafico_casosconfirmados,
    x=config_grafico_casosconfirmados.index,
    y="Casos Confirmados (Acumulativo)",
    text_auto=True,
    orientation="v",
    title="Casos confirmados (acumulativo)",
    color_discrete_sequence=["#032447"] * len(config_grafico_casosconfirmados),
)

grafico_casosconfirmados.update_layout(
    title_x=0.1,
    title_font_size=20,
    font=dict(size=18),
    xaxis=dict(tickmode="linear"),
    yaxis=(dict(showgrid=False)),
    plot_bgcolor="rgba(0,0,0,0)"
)

grafico_casosconfirmados.update_xaxes(
    title=None,
    showticklabels=True,
    tickfont_size=20
)

grafico_casosconfirmados.update_yaxes(
    title=None,
    showticklabels=False
)

grafico_obitos = px.bar(
    config_grafico_obitos,
    x=config_grafico_obitos.index,
    y="Óbitos (Acumulativo)",
    text_auto=True,
    orientation="v",
    title="Óbitos (acumulativo)",
    color_discrete_sequence=["#004811"] * len(config_grafico_obitos),
)

grafico_obitos.update_layout(
    title_x=0.3,
    title_font_size=20,
    font=dict(size=18),
    xaxis=dict(tickmode="linear"),
    yaxis=(dict(showgrid=False)),
    plot_bgcolor="rgba(0,0,0,0)",
)

grafico_obitos.update_xaxes(
    title=None,
    showticklabels=True,
    tickfont_size=20
)

grafico_obitos.update_yaxes(
    title=None,
    showticklabels=False
)

grafico_casosrecuperados = px.bar(
    config_grafico_casosrecuperados,
    x=config_grafico_casosrecuperados.index,
    y="Casos Recuperados (Acumulativo)",
    text_auto=True,
    orientation="v",
    title="Casos recuperados (acumulativo)",
    color_discrete_sequence=["#53004F"] * len(config_grafico_casosrecuperados),
)

grafico_casosrecuperados.update_layout(
    title_x=0.1,
    title_font_size=20,
    font=dict(size=18),
    xaxis=dict(tickmode="linear"),
    yaxis=(dict(showgrid=False)),
    plot_bgcolor="rgba(0,0,0,0)",
)

grafico_casosrecuperados.update_xaxes(
    title=None,
    showticklabels=True,
    tickfont_size=20
)

grafico_casosrecuperados.update_yaxes(
    title=None,
    showticklabels=False
)

left_column, center_column, right_column = st.columns(3)

left_column.plotly_chart(grafico_casosconfirmados, use_container_width=True)
center_column.plotly_chart(grafico_obitos, use_container_width=True)
right_column.plotly_chart(grafico_casosrecuperados, use_container_width=True)
