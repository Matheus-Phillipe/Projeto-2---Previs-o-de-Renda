import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
  page_title="Projeto Previsão de Renda",
  page_icon=":bar_chart:",
  layout="wide",
)

st.write('---')
st.write('---')
st.write('# :bar_chart: Análise exploratória da previsão de renda')
renda = pd.read_csv('./input/previsao_de_renda.csv')
st.write('---')
st.write('---')
st.write('Esse projeto tem como objetivo analisar as variáveis de um DataSet para determinar uma padrão de comportamento e prever a renda de cada cliente.')
st.write('Inicialmente foi gerado os gráficos analisando cada variável ao longo do tempo e em seguida as variáveis foram analisadas de forma bivariada, ou seja, colocadas diretamente contra a variável alvo: a renda')

# plots
fig, ax = plt.subplots(9, 1, figsize=(20, 120))
renda[['posse_de_imovel', 'renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')
ax[0].set_title('Frequencia dos valores de renda')
sns.lineplot(x='data_ref', y='renda',
       hue='posse_de_imovel', data=renda, ax=ax[1])
ax[1].set_title('Variação da renda pelo tempo em relação a posse de imóvel')
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda',
       hue='posse_de_veiculo', data=renda, ax=ax[2])
ax[2].set_title('Variação da renda pelo tempo em relação a posse de veículo')
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='qtd_filhos', data=renda, ax=ax[3])
ax[3].set_title('Variação da renda pelo tempo em relação a quantidade de filhos')
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='tipo_renda', data=renda, ax=ax[4])
ax[4].set_title('Variação da renda pelo tempo em relação ao tipo de renda')
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax[5])
ax[5].set_title('Variação da renda pelo tempo em relação ao grau de escolaridade')
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda, ax=ax[6])
ax[6].set_title('Variação da renda pelo tempo em relação ao estado civil')
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda',
       hue='tipo_residencia', data=renda, ax=ax[7])
ax[7].set_title('Variação da renda pelo tempo em relação ao tipo de residência')
ax[7].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref', y='renda',
       hue='sexo', data=renda, ax=ax[8])
ax[8].set_title('Variação da renda pelo tempo em relação ao sexo')
ax[8].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(8, 1, figsize=(20, 70))
sns.barplot(x='posse_de_imovel', y='renda', data=renda, ax=ax[0])
ax[0].set_title('Renda x Posse de imovel')
sns.barplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax[1])
ax[1].set_title('Renda x Posse de veiculo')
sns.barplot(x='qtd_filhos', y='renda', data=renda, ax=ax[2])
ax[2].set_title('Renda x Quantidade de filhos')
sns.barplot(x='tipo_renda', y='renda', data=renda, ax=ax[3])
ax[3].set_title('Renda x Tipo de renda')
sns.barplot(x='educacao', y='renda', data=renda, ax=ax[4])
ax[4].set_title('Renda x Escolaridade')
sns.barplot(x='estado_civil', y='renda', data=renda, ax=ax[5])
ax[5].set_title('Renda x Estado Civil')
sns.barplot(x='tipo_residencia', y='renda', data=renda, ax=ax[6])
ax[6].set_title('Renda x Tipo de residência')
sns.barplot(x='sexo', y='renda', data=renda, ax=ax[7])
ax[7].set_title('Renda x Sexo')

sns.despine()
st.pyplot(plt)


st.write('# 💡Insights')
st.write('Alguns das variaveis observadas inicialmente se mostraram realmente significantes quando olhamos para a renda. As variaveis que mais se destacaram foram o sexo, tempo_emprego, idade, pessoas com ensino superior completo e posse de veiculo. Das informaçoes que podemos afirmar que influenciam o individuo a ter uma renda superior é: Ser do sexo masculino, tem um tempo maior no emprego, consequentemente ter mais idade, possuir veiculo e ter pelo menos ensino superior completo.')

