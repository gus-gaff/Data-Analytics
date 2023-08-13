from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel("COVID-19 Brasil - Analitico.xlsm")

grafico_casosconfirmados = (px.bar(df,
                    x="Ano",
                    y="Casos Confirmados (Acumulativo)",
                    orientation='v',
                    opacity=0.5,
                    barmode='relative',
                    text_auto=True,
                    color_discrete_sequence =['#BC00FF']*len(df),
                    width=500,
                    height=500,))

grafico_casosconfirmados.update_layout(
                    title='Casos Confirmados (Acumulativo)',
                    title_x=0.5,
                    title_font_size=20,
                    showlegend=False,
                    plot_bgcolor="#EAECEE",
                    paper_bgcolor="#D5D5D5",
                    xaxis=dict(visible=True),
                    yaxis=dict(visible=False),
                    bargap=(0.50))

grafico_casosconfirmados.update_xaxes(
                    dtick="M1",
                    tickformat="%b\n%Y",
                    ticklabelmode="period",
                    mirror=True,
                    ticks='outside',
                    showline=True,
                    linecolor='black',)

grafico_obitos = (px.bar(df,
                    x="Ano",
                    y="Óbitos (Acumulativo)",
                    orientation='v',
                    barmode='relative',
                    text_auto=True,
                    color_discrete_sequence =['#BC00FF']*len(df),
                    width=500,
                    height=500,))

grafico_obitos.update_layout(
                    title='Óbitos (Acumulativo)',
                    title_x=0.5,
                    title_font_size=20,
                    showlegend=False,
                    plot_bgcolor="#EAECEE",
                    paper_bgcolor="#D5D5D5",
                    xaxis=dict(visible=True),
                    yaxis=dict(visible=False),
                    bargap=(0.50))

grafico_obitos.update_xaxes(
                    dtick="M1",
                    tickformat="%b\n%Y",
                    ticklabelmode="period",
                    mirror=True,
                    ticks='outside',
                    showline=True,
                    linecolor='black',)

grafico_casosrecuperados = (px.bar(df,
                    x="Ano",
                    y="Casos Recuperados (Acumulativo)",
                    orientation='v',
                    barmode='relative',
                    text_auto=True,
                    color_discrete_sequence =['#BC00FF']*len(df),
                    width=500,
                    height=500,))

grafico_casosrecuperados.update_layout(
                    title='Casos Recuperados (Acumulativo)',
                    title_x=0.5,
                    title_font_size=20,
                    showlegend=False,
                    plot_bgcolor="#EAECEE",
                    paper_bgcolor="#D5D5D5",
                    xaxis=dict(visible=True),
                    yaxis=dict(visible=False),
                    bargap=(0.50),)

grafico_casosrecuperados.update_xaxes(
                    dtick="M1",
                    tickformat="%b\n%Y",
                    ticklabelmode="period",
                    mirror=True,
                    ticks='outside',
                    showline=True,
                    linecolor='black')

opcoes_ano = list(df['Ano'].unique())
opcoes_ano.sort()
opcoes_ano.append("Todos os anos")

app.layout = (
    html.Div(children=[
    html.H2(children='Impacto da COVID-19 no Brasil - Uma análise (2020-2023)', style={'textAlign': 'center'}),
    dcc.Dropdown(opcoes_ano, value='Todos os anos', id='lista_anos', style={'width': '40%'}),

    dcc.Graph(
        id='grafico_casosconfirmados',
        style={'display': 'inline-block'},
        figure=grafico_casosconfirmados
    ),
    dcc.Graph(
        id='grafico_obitos',
        style={'display': 'inline-block'},
        figure=grafico_obitos
    ),
    dcc.Graph(
        id='grafico_casosrecuperados',
        style={'display': 'inline-block'},
        figure=grafico_casosrecuperados
    )
]))

@app.callback(
    Output('grafico_casosconfirmados', 'figure'),
    Output('grafico_obitos', 'figure'),
    Output('grafico_casosrecuperados', 'figure'),
    Input('lista_anos','value'))

def atualizar_graficos_(value):

    if value == 'Todos os anos':

        grafico_casosconfirmados = (px.bar(df,
            x="Ano",
            y="Casos Confirmados (Acumulativo)",
            orientation='v',
            opacity=0.5,
            barmode='relative',
            text_auto=True,
            color_discrete_sequence=['#BC00FF'] * len(df),
            width=500,
            height=500,))

        grafico_casosconfirmados.update_layout(
            title='Casos Confirmados (Acumulativo)',
            title_x=0.5,
            title_font_size=20,
            showlegend=False,
            plot_bgcolor="#EAECEE",
            paper_bgcolor="#D5D5D5",
            xaxis=dict(visible=True),
            yaxis=dict(visible=False),
            bargap=(0.50))

        grafico_casosconfirmados.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y",
            ticklabelmode="period",
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',)

        grafico_obitos = (px.bar(df,
            x="Ano",
            y="Óbitos (Acumulativo)",
            orientation='v',
            barmode='relative',
            text_auto=True,
            color_discrete_sequence=['#BC00FF'] * len(df),
            width=500,
            height=500,))

        grafico_obitos.update_layout(
            title='Óbitos (Acumulativo)',
            title_x=0.5,
            title_font_size=20,
            showlegend=False,
            plot_bgcolor="#EAECEE",
            paper_bgcolor="#D5D5D5",
            xaxis=dict(visible=True),
            yaxis=dict(visible=False),
            bargap=(0.50))

        grafico_obitos.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y",
            ticklabelmode="period",
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',)

        grafico_casosrecuperados = (px.bar(df,
            x="Ano",
            y="Casos Recuperados (Acumulativo)",
            orientation='v',
            barmode='relative',
            text_auto=True,
            color_discrete_sequence=['#BC00FF'] * len(df),
            width=500,
            height=500,))

        grafico_casosrecuperados.update_layout(
            title='Casos Recuperados (Acumulativo)',
            title_x=0.5,
            title_font_size=20,
            showlegend=False,
            plot_bgcolor="#EAECEE",
            paper_bgcolor="#D5D5D5",
            xaxis=dict(visible=True),
            yaxis=dict(visible=False),
            bargap=(0.50),)

        grafico_casosrecuperados.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y",
            ticklabelmode="period",
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black')

    else:

            filtro_ano = df.loc[df['Ano'] == value, :]

            grafico_casosconfirmados = (px.bar(filtro_ano,
            x="Ano",
            y="Casos Confirmados (Acumulativo)",
            orientation='v',
            opacity=0.5,
            barmode='relative',
            text_auto=True,
            color_discrete_sequence=['#BC00FF'] * len(df),
            width=500,
            height=500,))

            grafico_casosconfirmados.update_layout(
            title='Casos Confirmados (Acumulativo)',
            title_x=0.5,
            title_font_size=20,
            showlegend=False,
            plot_bgcolor="#EAECEE",
            paper_bgcolor="#D5D5D5",
            xaxis=dict(visible=True),
            yaxis=dict(visible=False),
            bargap=(0.50))

            grafico_casosconfirmados.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y",
            ticklabelmode="period",
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',)

            grafico_obitos = (px.bar(filtro_ano,
            x="Ano",
            y="Óbitos (Acumulativo)",
            orientation='v',
            barmode='relative',
            text_auto=True,
            color_discrete_sequence=['#BC00FF'] * len(df),
            width=500,
            height=500,))

            grafico_obitos.update_layout(
            title='Óbitos (Acumulativo)',
            title_x=0.5,
            title_font_size=20,
            showlegend=False,
            plot_bgcolor="#EAECEE",
            paper_bgcolor="#D5D5D5",
            xaxis=dict(visible=True),
            yaxis=dict(visible=False),
            bargap=(0.50))

            grafico_obitos.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y",
            ticklabelmode="period",
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black',)

            grafico_casosrecuperados = (px.bar(filtro_ano,
            x="Ano",
            y="Casos Recuperados (Acumulativo)",
            orientation='v',
            barmode='relative',
            text_auto=True,
            color_discrete_sequence=['#BC00FF'] * len(df),
            width=500,
            height=500, ))

            grafico_casosrecuperados.update_layout(
            title='Casos Recuperados (Acumulativo)',
            title_x=0.5,
            title_font_size=20,
            showlegend=False,
            plot_bgcolor="#EAECEE",
            paper_bgcolor="#D5D5D5",
            xaxis=dict(visible=True),
            yaxis=dict(visible=False),
            bargap=(0.50), )

            grafico_casosrecuperados.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y",
            ticklabelmode="period",
            mirror=True,
            ticks='outside',
            showline=True,
            linecolor='black')

    return grafico_casosconfirmados, grafico_obitos, grafico_casosrecuperados,

if __name__ == '__main__':
    app.run(debug=True)