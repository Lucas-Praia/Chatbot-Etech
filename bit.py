import streamlit as st
import time
import string
from streamlit_chat import message as msg
import re

st.title("Bit Etech")

respostas = {
    'Olá': 'Olá! Como posso te ajudar?',
    'Oi': 'Olá! Como posso te ajudar?',
    'Bom dia': 'Bom dia! Como posso te ajudar?',
    'Boa tarde': 'Boa tarde! Como posso te ajudar?',
    'Boa noite': 'Boa noite! Como posso te ajudar?',
    'O que é a FPF Tech?': 'A FPF Tech é um Centro tecnológico premiado em software e hardware, reconhecido por cinco anos como uma das Melhores Empresas em TI & Telecom no Brasil. '
                           'Destaca-se por investir em treinamentos e ter uma equipe jovem.',

    'FPF Tech foi fundada': 'A FPF Tech foi fundada em 1998.',

    'Qual o ramo que a FPF atua?': 'A FPF Tech é uma instituição de Pesquisa e Desenvolvimento, sem fins lucrativos, '
                    'focada na geração de soluções inovadoras, serviços e cases de sucesso globais nas áreas de'
                             ' Automação Industrial, Tecnologias Móveis e Assistivas, Internet, Qualidade de Software e Capacitação Tecnológica.',

    'Qual é a missão da FPF Tech?': 'A missão da FPF Tech é criar soluções inovadoras entregando valor aos seus '
                                    'clientes e à sociedade, com a colaboração de pessoas notáveis.',
    'É de Manaus mesmo essa escola?': 'Sim, a Etech é de Manaus e está localizada no endereço.....',
}


def remover_acentos(texto):
    texto = texto.lower()
    acentos = {
        'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u',
        'ç': 'c'
    }

    for caracter, substituto in acentos.items():
        texto = texto.replace(caracter, substituto)

    return texto.lower()

def encontrar_melhorResposta(msg, respostas):
    melhor_resposta = 'Desculpa, não entendi sua pergunta!'
    melhor_pontuacao = 0

    for pergunta, resposta in respostas.items():

        pergunta_formatada = remover_acentos(pergunta)

        palavras_pergunta = set(re.findall(r'\b\w+\b', pergunta_formatada))
        palavras_msg = set(re.findall(r'\b\w+\b', msg.lower()))

        pontuacao = len(palavras_pergunta.intersection(palavras_msg))

        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_resposta = resposta

    return melhor_resposta

pergunta = st.text_area("Olá! Sou o Bit Etech, como posso te ajudar?")
btn_enviar = st.button('Enviar pergunta')

if btn_enviar and pergunta:
    pergunta_formatada = remover_acentos(pergunta)
    resposta = encontrar_melhorResposta(pergunta_formatada, respostas)
    with st.chat_message("user"):
        st.write ("Você:", pergunta)
    time.sleep(1.0)
    with st.chat_message("assistant"):
        st.write("Bit Etech:", resposta)
