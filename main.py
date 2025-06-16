import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Certifique-se de que sua API Key do Google está configurada.
# Você pode fazer isso definindo uma variável de ambiente chamada GOOGLE_API_KEY
# Exemplo (NÃO FAÇA ISSO EM CÓDIGO DE PRODUÇÃO):
# os.environ["GOOGLE_API_KEY"] = "SUA_CHAVE_DE_API_AQUI"
# O ideal é usar um arquivo .env ou outra forma segura de gerenciar credenciais.

try:
    # load environment variables from .env file (requires `python-dotenv`)
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# 1. Inicialize o modelo Gemini 1.5 Flash
# Note a mudança do nome do modelo aqui para "gemini-1.5-flash"
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7) # temperature controla a aleatoriedade da resposta

# 2. Crie uma mensagem para enviar ao modelo
messages = [
    SystemMessage(content="Você é um assistente prestativo e criativo. Responda de forma concisa."),
    HumanMessage(content="Qual é a capital do Brasil e qual é a principal característica da sua arquitetura?"),
]

# 3. Invoque o modelo com a mensagem
print("Perguntando ao Gemini 1.5 Flash...")
response = llm.invoke(messages)

# 4. Imprima a resposta
print("\nResposta do Gemini 1.5 Flash:")
print(response.content)

# --- Exemplo de uma cadeia simples com o Gemini 1.5 Flash ---
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Defina um template de prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um especialista em história. Responda apenas sobre fatos históricos."),
    ("user", "Quem foi {personalidade} e qual a sua maior contribuição?"),
])

# 2. Crie uma cadeia usando o prompt, o modelo e um parser de saída
chain = prompt | llm | StrOutputParser()

# 3. Invoque a cadeia com o input
print("\nPerguntando novamente com uma cadeia (chain):")
response_chain = chain.invoke({"personalidade": "Albert Einstein"})

# 4. Imprima a resposta da cadeia
print("\nResposta da cadeia:")
print(response_chain)