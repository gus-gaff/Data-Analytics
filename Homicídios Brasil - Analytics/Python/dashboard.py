import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

basededados = pd.read_excel('base/Homicidios Brasil - Analytics.xlsx')

basededados['Ano + Qtd. Homicídios (soma)'] = (
    basededados['Ano'].astype(str)
    + '<br>' +
    basededados['Qtd. Homicídios (soma)'].astype(str)
)

st.set_page_config(
    page_icon="🇧🇷",
    page_title="Homicídios - Brasil - Analytics",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'mailto:gustavocostasilva505@gmail.com',
        'Report a bug': "mailto:gustavocostasilva505@gmail.com",
        'About': "###### © 2023 Gustavo Costa Silva All Rights Reserved"
    }
)

st.sidebar.title("Filtrar por:")
st.sidebar.info("Ano")

Ano = st.sidebar.multiselect(
                                "Ano:",
                                options=basededados["Ano"].unique(),
                                default=basededados["Ano"].unique(),
                                placeholder="Selecione o ano",
                                key='ano_multiselect'
                                )

basededados_filtro = basededados.query(
    "Ano == @Ano"
)

st.title(":chart_with_upwards_trend: Homicídios - Brasil - Analytics")
st.subheader("Uma análise realizada abordando o período de (1989-2019)")

st.markdown("###")

left_column, center_column = st.columns(2)

qtdhomicidios_icone = Image.open('images/qtdhomicidios_icon.png')
left_column.image(qtdhomicidios_icone, width=60)
mediahomicidios_icone = Image.open('images/mediahomicidios_icon.png')
center_column.image(mediahomicidios_icone, width=60)

kpi_qtdhomicidios = (basededados_filtro["Qtd. Homicídios (soma)"].sum())
kpi_mediahomicidios = (basededados_filtro["Qtd. Homicídios (média)"].mean())

left_column, center_column = st.columns(2)

with left_column:
    st.markdown("##### Qtd. Homicídios")
    st.subheader(f'{kpi_qtdhomicidios:,.0f}')
with center_column:
    st.markdown("##### Média Homicídios")
    st.subheader(f'{kpi_mediahomicidios:,.0f}')

st.markdown("---")
st.markdown("###")

config_grafico_qtdhomicidios = (
    basededados_filtro.groupby(by=["Ano"]).sum()
)

grafico_qtdhomicidios = px.line(
    config_grafico_qtdhomicidios,
    x=config_grafico_qtdhomicidios.index,
    y='Qtd. Homicídios (soma)',
    text='Ano + Qtd. Homicídios (soma)',
    title="Qtd. Homicídios no Brasil (1989-2019)",
    color_discrete_sequence=["#FF0017"] * len(config_grafico_qtdhomicidios)
)

grafico_qtdhomicidios.update_layout(
    height=800,
    width=1100,
    title_x=0.3,
    title_font_size=20,
    font=dict(size=10),
    plot_bgcolor="rgba(0,0,0,0)"
)

grafico_qtdhomicidios.update_traces(
    textposition='top center'
)

grafico_qtdhomicidios.update_xaxes(
    title=None,
    showticklabels=False,
    showgrid=False

)

grafico_qtdhomicidios.update_yaxes(
    title=None,
    showticklabels=False,
    showgrid=False
)

left_column, center_column = st.columns(2)

left_column.plotly_chart(grafico_qtdhomicidios)
