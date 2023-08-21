import pandas as pd
import streamlit as st
import plotly.express as px

basededados = pd.read_excel('COVID-19 Brasil - Analytics.xlsx')

st.set_page_config(
    page_title="COVID-19 - Brasil - Analytics",
    page_icon="🇧🇷",
    layout="wide",
)

st.sidebar.header("Filtrar por:")

Ano = st.sidebar.multiselect(
                                "Ano:",
                                options=basededados["Ano"].unique(),
                                default=basededados["Ano"].unique()
                            )

Mes = st.sidebar.multiselect(
                                "Mês:",
                                options=basededados["Mês"].unique(),
                                default=basededados["Mês"].unique()
                            )

basededados_filtro = basededados.query(
    "Ano == @Ano & Mês == @Mes"
)

st.title(":chart_with_upwards_trend: COVID-19 - Brasil - Analytics")
st.subheader("Impacto da COVID-19 no Brasil - Uma análise (2020-2023)")

st.markdown("###")

kpi_casosconfirmados = (basededados_filtro["Casos Confirmados (Acumulativo)"].max())
kpi_obitos = (basededados_filtro["Óbitos (Acumulativo)"].max())
kpi_casosrecuperados = (basededados_filtro["Casos Recuperados (Acumulativo)"].max())

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.markdown("##### Casos Confirmados (acumulativo)")
    st.subheader(f'{kpi_casosconfirmados:,.0f}')
with middle_column:
    st.markdown("##### Óbitos (acumulativo)")
    st.subheader(f'{kpi_obitos:,.0f}')
with right_column:
    st.markdown("##### Casos Recuperados (acumulativo)")
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
    y="Casos Confirmados (Acumulativo)",
    x=config_grafico_casosconfirmados.index,
    text_auto=True,
    orientation="v",
    title="Casos Confirmados (acumulativo)",
    color_discrete_sequence=["#e4f570"] * len(config_grafico_casosconfirmados),
    template="plotly_white",
    )

grafico_casosconfirmados.update_layout(
    title_x=0.1,
    title_font_size=20,
    xaxis=dict(tickmode="linear"),
    yaxis=(dict(showgrid=False)),
    plot_bgcolor="rgba(0,0,0,0)",
)

grafico_casosconfirmados.update_xaxes(
    title=None,
    showticklabels=True
)

grafico_casosconfirmados.update_yaxes(
    title=None,
    showticklabels=False
)

grafico_obitos = px.bar(
    config_grafico_obitos,
    y="Óbitos (Acumulativo)",
    x=config_grafico_obitos.index,
    text_auto=True,
    orientation="v",
    title="Óbitos (acumulativo)",
    color_discrete_sequence=["#82d581"] * len(config_grafico_obitos),
    template="plotly_white",
    )

grafico_obitos.update_layout(
    title_x=0.3,
    title_font_size=20,
    xaxis=dict(tickmode="linear"),
    yaxis=(dict(showgrid=False)),
    plot_bgcolor="rgba(0,0,0,0)",
    )

grafico_obitos.update_xaxes(
    title=None,
    showticklabels=True
)

grafico_obitos.update_yaxes(
    title=None,
    showticklabels=False
)

grafico_casosrecuperados = px.bar(
    config_grafico_casosrecuperados,
    y="Casos Recuperados (Acumulativo)",
    x=config_grafico_casosrecuperados.index,
    text_auto=True,
    orientation="v",
    title="Casos Recuperados (acumulativo)",
    color_discrete_sequence=["#2cae8f"] * len(config_grafico_casosrecuperados),
    template="plotly_white",
)

grafico_casosrecuperados.update_layout(
    title_x=0.1,
    title_font_size=20,
    xaxis=dict(tickmode="linear"),
    yaxis=(dict(showgrid=False)),
    plot_bgcolor="rgba(0,0,0,0)",
)

grafico_casosrecuperados.update_xaxes(
    title=None,
    showticklabels=True
)

grafico_casosrecuperados.update_yaxes(
    title=None,
    showticklabels=False
)

left_column, middle_column, right_column = st.columns(3)

left_column.plotly_chart(grafico_casosconfirmados, use_container_width=True)
middle_column.plotly_chart(grafico_obitos, use_container_width=True)
right_column.plotly_chart(grafico_casosrecuperados, use_container_width=True)
