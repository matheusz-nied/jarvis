import getpass
import os
import subprocess
import time
from langchain.agents import Tool, initialize_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
from langchain.agents.agent_types import AgentType

from test_interface import JarvisInterface
try:
    # load environment variables from .env file (requires `python-dotenv`)
    from dotenv import load_dotenv
    print("Loading environment variables from .env file...")

    load_dotenv()
except ImportError:
    pass
# 🔐 Chave da API Google Gemini
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# ⚙️ Inicializa o modelo Gemini
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# 🔧 Ferramenta de pesquisa simulada
def pesquisar_web(query: str) -> str:
    print(f"[PESQUISA] Simulando busca por: {query}")
    return f"Resultado simulado para: {query}"

# 🎵 Ferramenta para tocar música no YouTube com Brave e Selenium
import subprocess
import time
import os
import shutil
import platform
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shutil import which

import getpass
import os
import subprocess
import time
from langchain.agents import Tool, initialize_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
from langchain.agents.agent_types import AgentType

# 🔐 Chave da API Google Gemini
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# ⚙️ Inicializa o modelo Gemini
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# 🔧 Ferramenta de pesquisa simulada
def pesquisar_web(query: str) -> str:
    print(f"[PESQUISA] Simulando busca por: {query}")
    return f"Resultado simulado para: {query}"

# 🎵 Ferramenta para tocar música no YouTube com Selenium (usando Google Chrome)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from shutil import which
import signal  # Para enviar sinais de terminação a processos

# Tenta importar pyautogui para automação de cliques
try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except ImportError:
    PYAUTOGUI_AVAILABLE = False
    print("[AVISO] PyAutoGUI não está instalado. Alguns recursos avançados de clique não estarão disponíveis.")
    print("Instale com: pip install pyautogui")


# Variável global para armazenar o processo do navegador atual
chrome_process = None

def tocar_musica(query: str):
    # Formata a URL para busca de vídeos no YouTube
    url_search = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}&sp=EgIQAQ%253D%253D"
    
    print(f"[MÚSICA] Tentando tocar: {query}")
    
    # Verifica se já existe um processo Chrome aberto e o fecha
    global chrome_process
    if chrome_process:
        print("[INFO] Já existe um navegador aberto. Fechando antes de abrir nova música...")
        parar_musica()
    
    driver = None 
    # try:
    #     print("[INFO] Tentando abrir YouTube com Google Chrome e clicar no primeiro vídeo...")
    #     service = Service("/usr/local/bin/chromedriver-linux64/chromedriver")

    #     # Configurações para o Google Chrome
    #     options = Options()
    #     options.add_argument("--user-data-dir=/home/kaizen/chrome-selenium-profile")
    #     options.add_argument("--profile-directory=Default")  # ou "Profile 1", "Profile 2", etc
    #     options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #     options.add_experimental_option('useAutomationExtension', False)
    #     # Outras flags recomendadas
    #     options.add_argument("--no-sandbox")
    #     options.add_argument("--disable-dev-shm-usage")
    #     # --- Definir o binary_location para o Google Chrome ---
    #     # Tenta encontrar o google-chrome no PATH ou no caminho comum
    #     chrome_executable = "/usr/bin/brave-browser"
    #     if not chrome_executable:
    #         if not os.path.exists(chrome_executable):
    #             print(f"[ERRO] Executável do Google Chrome não encontrado em {chrome_executable} e não está no PATH.")
    #             return f"Erro: Google Chrome não encontrado. Não foi possível tocar '{query}'."

    #     options.binary_location = chrome_executable
    #     print(f"[INFO] Definindo binary_location para: {chrome_executable}")

    #     # Inicializa o Chrome WebDriver
    #     try:
    #         # Use Service() se chromedriver estiver no PATH
    #         # Se não estiver, especifique o caminho: Service(executable_path="/caminho/do/seu/chromedriver")
    #         driver = webdriver.Chrome(service=service, options=options)
    #         print(f"[✅] WebDriver (Google Chrome) iniciado com sucesso")
    #     except Exception as e:
    #         print(f"[ERRO] Não foi possível iniciar o WebDriver: {str(e)[:200]}")
    #         raise Exception(f"Falha ao iniciar WebDriver: {str(e)[:100]}")
        
    #     # Abre a página de busca do YouTube
    #     driver.get(url_search)
    #     print("[INFO] Página de busca do YouTube aberta")
        
    #     # Espera até 10 segundos pelos resultados da busca carregarem
    #     wait = WebDriverWait(driver, 10)
        
    #     # Agora vamos focar especificamente no seletor para o elemento id="video-title"
    #     try:
    #         print("[INFO] Aguardando e procurando pelo elemento com id='video-title'...")
            
    #         # Primeiro, esperamos até que os resultados carreguem
    #         wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer")))
            
    #         # Especificamente procuramos pelo link com id="video-title"
    #         video_title_selector = "#video-title"
    #         video_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, video_title_selector)))
            
    #         # Rola a página até o elemento
    #         driver.execute_script("arguments[0].scrollIntoView()", video_element)
    #         time.sleep(1)
            
    #         # Tenta clicar com JavaScript (mais confiável)
    #         driver.execute_script("arguments[0].click();", video_element)
            
    #         # Verifica se o clique funcionou (se estamos na mesma página, tenta clique normal)
    #         if driver.current_url == url_search:
    #             video_element.click()
                
    #         print(f"[✅] Clicou no vídeo com sucesso usando seletor {video_title_selector}!")
            
    #         # Espera um pouco para o vídeo carregar
    #         time.sleep(3)
                
    #         # Agora tenta garantir que o vídeo está sendo reproduzido
    #         # clicando no botão de play, se necessário
    #         try:
    #             # Seletores para o botão de play no YouTube
    #             play_button_selectors = [
    #                 ".ytp-play-button", # Botão padrão de play/pause
    #                 ".ytp-large-play-button", # Botão grande de play que aparece quando vídeo está parado
    #                 "#movie_player", # Clica no player diretamente
    #                 ".html5-video-container" # Container do vídeo
    #             ]
                
    #             for play_selector in play_button_selectors:
    #                 try:
    #                     print(f"[INFO] Tentando clicar no botão play com seletor: {play_selector}")
    #                     play_button = WebDriverWait(driver, 5).until(
    #                         EC.element_to_be_clickable((By.CSS_SELECTOR, play_selector))
    #                     )
    #                     driver.execute_script("arguments[0].click();", play_button)
    #                     print(f"[✅] Clicou no botão de play!")
    #                     break
    #                 except Exception as e:
    #                     print(f"[INFO] Não conseguiu clicar no botão com seletor {play_selector}")
    #                     continue
    #         except Exception as e:
    #             print(f"[INFO] Erro ao tentar clicar no play: {str(e)[:100]}")
    #             print("[INFO] O vídeo pode iniciar automaticamente ou pode ser necessário clicar manualmente")
            
    #         # Importante: NÃO fechamos o driver para que a música continue tocando
    #         print("[✅] Mantendo o navegador aberto para continuar a reprodução")
            
    #         # A página do vídeo foi aberta e provavelmente está tocando
    #         return f"Música '{query}' está sendo reproduzida no YouTube! O navegador permanecerá aberto para continuar a reprodução."
    #     except Exception as e:
    #         print(f"[INFO] Não foi possível clicar no elemento com id='video-title': {str(e)[:100]}")
        
    #     # Se chegou aqui e não conseguiu clicar no vídeo, fecha o driver e tenta com subprocess
    #     print("[ALERTA] Não conseguiu clicar no vídeo. Fechando WebDriver.")
    #     try:
    #         driver.quit()
    #     except Exception as e:
    #         print(f"[INFO] Erro ao fechar o driver: {str(e)[:100]}")
    
    # except Exception as e: # Este catch é para erros do Selenium
    #     print(f"[ERRO] Erro ao usar Selenium: {str(e)[:150]}")
    #     print("[INFO] Tentando método alternativo com subprocess...")
    
    # --- Parte do subprocess (método de backup, agora usando Google Chrome) ---
    chrome_subprocess_path = shutil.which("google-chrome")
    if not chrome_subprocess_path:
        chrome_subprocess_path = "/usr/bin/google-chrome" 
        if not os.path.exists(chrome_subprocess_path):
            print(f"[ERRO] Executável do Google Chrome para subprocess não encontrado em {chrome_subprocess_path} e não está no PATH.")
            return f"Não foi possível abrir um navegador para reproduzir '{query}'. Verifique se o Google Chrome está instalado."


    try:
        # Abre o Google Chrome diretamente com a URL de busca
        print(f"[INFO] Tentando abrir {url_search} com {chrome_subprocess_path} via subprocess...")
        process = subprocess.Popen([chrome_subprocess_path, url_search])
        # Armazena o processo atual para poder encerrá-lo depois
        chrome_process = process
        print(f"[✅] Sucesso! URL aberta com {chrome_subprocess_path}")
        
        # Pausamos o script por alguns segundos para a página carregar completamente
        time.sleep(5)
        
        # Tenta usar o PyAutoGUI para clicar no primeiro resultado se disponível
        if PYAUTOGUI_AVAILABLE:
            try:
                print("[INFO] Tentando usar PyAutoGUI para clicar no primeiro resultado...")
                
                script_dir = os.path.dirname(os.path.abspath(__file__))
                ref_image = os.path.join(script_dir, "youtube_video_title.png")
                
                if os.path.exists(ref_image):
                    try:
                        print("[INFO] Buscando referência visual do título do vídeo...")
                        location = pyautogui.locateOnScreen(ref_image, confidence=0.7)
                        if location:
                            center_x, center_y = pyautogui.center(location)
                            pyautogui.click(center_x, center_y)
                            print(f"[✅] Clicou no primeiro resultado usando referência visual!")
                            time.sleep(2)
                            return f"Música '{query}' está sendo reproduzida no YouTube!"
                    except Exception as e:
                        print(f"[INFO] Não conseguiu encontrar referência visual: {str(e)[:100]}")
                
                print("[INFO] Tentando clicar em posição estimada para o primeiro resultado...")
                pyautogui.click(x=500, y=400)  
                time.sleep(0.5)
                # pyautogui.moveTo(x=500, y=450, duration=0.5)
                pyautogui.click()
                print("[✅] Tentou clicar no primeiro resultado usando posição estimada")
                
                time.sleep(3)
                
                return f"Música '{query}' está sendo reproduzida no YouTube (via clique automático)!"
            except Exception as e:
                print(f"[INFO] Erro ao tentar clicar com PyAutoGUI: {str(e)[:100]}")
        
        print("[INFO] Navegador aberto, mas clique manual necessário")
        return f"Música '{query}' está sendo carregada no YouTube. Você precisa clicar no vídeo para reproduzir."
    except FileNotFoundError:
        print(f"[ERRO] Navegador {chrome_subprocess_path} não foi encontrado no sistema")
    except Exception as e:
        print(f"[ERRO] Erro ao tentar abrir {chrome_subprocess_path} com {url_search}: {e}")
            
    try:
        print("[INFO] Tentando abrir com o navegador padrão do sistema...")
        import webbrowser
        url_final = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        webbrowser.open(url_final)
        time.sleep(1)
        return f"Música '{query}' está sendo carregada no navegador padrão. Clique no vídeo para reproduzir se necessário."
    except Exception as e:
        print(f"[ERRO] Erro ao tentar abrir o navegador padrão: {e}")
    
    return f"Não foi possível abrir um navegador para reproduzir '{query}'. Verifique se o Google Chrome está instalado."

# 🎙️ Módulo de reconhecimento de voz
import speech_recognition as sr
import re

def escutar_comando():
    """Escuta o microfone e retorna o texto reconhecido"""
    # Se tivermos interface gráfica, atualiza o estado
    global interface
    if interface:
        interface.start_listening()
    
    recognizer = sr.Recognizer()
    
    # Ajusta o recognizer para o ruído ambiente
    with sr.Microphone() as source:
        print("\n🔊 Ajustando para ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎧 Ouvindo...")
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("🔍 Reconhecendo...")
            
            # Atualiza estado da interface
            if interface:
                interface.stop_listening()
                interface.start_thinking()
            
            # Usando o Google Speech Recognition
            texto = recognizer.recognize_google(audio, language="pt-BR")
            print(f"🗣️ Você disse: {texto}")
            return texto.lower()
        except sr.WaitTimeoutError:
            if interface:
                interface.stop_listening()
            return ""
        except sr.UnknownValueError:
            if interface:
                interface.stop_listening()
            print("❓ Não entendi o que você disse")
            return ""
        except sr.RequestError as e:
            if interface:
                interface.stop_listening()
            print(f"❌ Erro na requisição ao serviço de reconhecimento: {e}")
            return ""

def detectar_jarvis(texto):
    """Verifica se o texto contém a palavra de ativação 'Jarvis'"""
    return bool(re.search(r"\bjarvis\b", texto, re.IGNORECASE))

def detectar_comando_parar(texto):
    """Verifica se o texto contém comando para parar a música"""
    # Lista de padrões que indicam comando para parar
    padroes_parar = [
        r"\bparar\b",  
        r"\bpara\b", 
        r"\bpare\b", 
        r"\bstop\b", 
        r"\bcancela\b",
        r"\bfecha\b", 
        r"\bencerra\b",
        r"\bdesliga\b", 
        r"\bsilencia\b"
    ]
    
    # Lista de palavras de contexto relacionadas a música/audio
    contexto_musica = [
        r"\bmúsica\b", 
        r"\bsom\b", 
        r"\báudio\b", 
        r"\btítulo\b", 
        r"\bcanção\b", 
        r"\byoutube\b", 
        r"\bnavegador\b"
    ]
    
    # Verifica se há algum padrão de parada
    for padrao in padroes_parar:
        if re.search(padrao, texto, re.IGNORECASE):
            # Se encontrou um padrão de parada, verifica se há contexto de música
            for contexto in contexto_musica:
                if re.search(contexto, texto, re.IGNORECASE):
                    return True
            
            # Mesmo sem o contexto explícito, assume que é para parar
            return True
    
    return False

def detectar_comando_pausar(texto):
    """Verifica se o texto contém comando para pausar a música"""
    # Lista de padrões que indicam comando para pausar
    padroes_pausar = [
        r"\bpausar\b",
        r"\bpausa\b",
        r"\bpause\b",
        r"\besperar\b",
        r"\bespera\b",
        r"\bcongelar\b"
    ]
    
    # Verifica se há algum padrão de pausa
    for padrao in padroes_pausar:
        if re.search(padrao, texto, re.IGNORECASE):
            return True
    
    return False

def detectar_comando_tocar(texto):
    """Verifica se o texto contém comando para resumir/tocar a música"""
    # Lista de padrões que indicam comando para resumir/tocar
    padroes_tocar = [
        r"\btocar\b",
        r"\btoca\b",
        r"\bcontinuar\b",
        r"\bcontinua\b",
        r"\bresume\b",
        r"\bresumír\b",
        r"\bresume\b",
        r"\bplay\b",
        r"\bseguir\b"
    ]
    
    # Verifica se há algum padrão de tocar/resumir
    for padrao in padroes_tocar:
        if re.search(padrao, texto, re.IGNORECASE):
            return True
    
    return False

def extrair_comando_musica(texto):
    """Extrai o comando de música do texto"""
    # Padrões comuns para pedidos de música
    padrao_tocar = r"(tocar|ouvir|escutar|coloca|coloque|põe|bota)\s+(a música|música|a canção|canção|o som|som)?\s*(.+)"
    
    # Procura padrões de pedido de música no texto
    match = re.search(padrao_tocar, texto, re.IGNORECASE)
    if match:
        return match.group(3)
    
    # Se não encontrou padrões específicos, remove apenas o "jarvis" do texto
    return re.sub(r"\bjarvis\b", "", texto, flags=re.IGNORECASE).strip()

def parar_musica():
    """Para a reprodução de música fechando o processo do navegador"""
    global chrome_process
    
    if chrome_process:
        print("[INFO] Tentando encerrar o navegador usando subprocess.terminate()")
        try:
            if chrome_process.poll() is None:
                chrome_process.terminate()
                try:
                    chrome_process.wait(timeout=2)
                    print("[INFO] Navegador encerrado com sucesso")
                    chrome_process = None
                    return True
                except subprocess.TimeoutExpired:
                    print("[INFO] Tempo expirado ao tentar encerrar o navegador, usando kill()")
                    chrome_process.kill()
                    chrome_process = None
                    return True
            else:
                print("[INFO] O navegador já está fechado")
                chrome_process = None
                return False
        except Exception as e:
            print(f"[ERRO] Erro ao tentar encerrar o navegador: {e}")
            chrome_process = None
            return False
    else:
        print("[INFO] Não há navegador aberto para ser fechado")
        return False

def pausar_musica():
    """Pausa a reprodução de música clicando na posição do player"""
    global chrome_process
    
    if chrome_process and chrome_process.poll() is None:
        try:
            # Clica na posição do player para pausar
            print("[INFO] Tentando pausar a música com um clique...")
            pyautogui.click(x=400, y=600)
            print("[✅] Tentativa de pausar a música executada")
            return True
        except Exception as e:
            print(f"[ERRO] Erro ao tentar pausar a música: {e}")
            return False
    else:
        print("[INFO] Não há navegador aberto para pausar a música")
        return False

def retomar_musica():
    """Retoma a reprodução de música clicando na posição do player"""
    global chrome_process
    
    if chrome_process and chrome_process.poll() is None:
        try:
            # Clica na posição do player para retomar
            print("[INFO] Tentando retomar a música com um clique...")
            pyautogui.click(x=400, y=600)
            print("[✅] Tentativa de retomar a música executada")
            return True
        except Exception as e:
            print(f"[ERRO] Erro ao tentar retomar a música: {e}")
            return False
    else:
        print("[INFO] Não há navegador aberto para retomar a música")
        return False

def processar_comando_voz():
    """Processa o comando de voz e retorna o texto processado ou comandos especiais"""
    texto = escutar_comando()
    
    # Se não reconheceu nenhum texto, retorna vazio
    if not texto:
        return ""
    
    # Verifica se o texto contém a palavra-chave "jarvis"
    if not detectar_jarvis(texto):
        print("❌ Comando não começou com 'Jarvis'")
        return ""
    
    # Verifica comandos de controle de música
    if detectar_comando_parar(texto):
        parar_musica()
        # Mostra uma expressão feliz brevemente depois de executar o comando
        global interface
        if interface:
            interface.be_happy(1500)
        return "[COMANDO_EXECUTADO]"  # Sinaliza que o comando foi executado
    
    if detectar_comando_pausar(texto):
        pausar_musica()
        # Mostra uma expressão feliz brevemente depois de executar o comando
        if interface:
            interface.be_happy(1500)
        return "[COMANDO_EXECUTADO]"  # Sinaliza que o comando foi executado
    
    if detectar_comando_tocar(texto):
        # Verifica se é comando para retomar música atual ou tocar nova música
        comando_musica = extrair_comando_musica(texto)
        if comando_musica:
            # Comando para tocar nova música
            tocar_musica(comando_musica)
        else:
            # Comando para retomar música atual
            retomar_musica()
        
        # Mostra uma expressão feliz brevemente depois de executar o comando
        if interface:
            interface.be_happy(1500)
            
        return "[COMANDO_EXECUTADO]"  # Sinaliza que o comando foi executado
    
    # Remove a palavra "jarvis" do comando para processamento
    texto = texto.replace("jarvis", "").strip()
    
    return texto  # Retorna o comando para ser processado pelo agente

def modo_voz():
    """Inicia o assistente no modo de comandos por voz."""
    global interface
    print("\n🎙️ Modo de Voz iniciado - diga 'Jarvis' seguido do seu comando.")
    print("Digite 'sair' para encerrar.")
    
    import pygame
    while True:
        try:
            # Mantém a interface responsiva
            if interface:
                pygame.event.pump()
            # Processa o comando de voz
            comando = processar_comando_voz()
            
            # Se não foi reconhecido um comando válido, continua
            if not comando:
                continue
            
            # Se foi um comando específico que já foi tratado
            if comando == "[COMANDO_EXECUTADO]":
                continue
            
            # Chama o agente com o comando
            print(f"\n🤖 Processando: '{comando}'")
            
            # Atualiza a interface para mostrar que está pensando
            if interface:
                interface.start_thinking()
                pygame.event.pump()
                
            # Processa a resposta
            resposta = agent.run(comando)
            
            # Atualiza a interface para mostrar que está respondendo
            if interface:
                interface.start_talking()
                pygame.event.pump()
                
            print(f"\n🧠 Jarvis: {resposta}")
            
            # Adiciona um pequeno delay para permitir que a animação de fala seja vista
            time.sleep(len(resposta) * 0.05)  # Tempo proporcional ao tamanho da resposta
            
            # Volta para o estado neutro
            if interface:
                interface.stop_talking()
                pygame.event.pump()
            
        except KeyboardInterrupt:
            print("\n👋 Encerrando o modo de voz...")
            if interface:
                interface.stop()
            return
        except Exception as e:
            print(f"\n❌ Erro: {str(e)}")
            if interface:
                interface.stop_talking()

# Configuração do agente
tools = [
    Tool(
        name="Pesquisa na Web",
        func=pesquisar_web,
        description="Ferramenta para pesquisar na web por informações"
    ),
    Tool(
        name="Reproduzir Música",
        func=tocar_musica,
        description="Ferramenta para tocar música no YouTube"
    )
]

# Inicialização do agente
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    system_message=SystemMessage(content="""Você é o Jarvis, um assistente de IA avançado.
    Seu objetivo é ajudar o usuário com suas tarefas diárias, responder perguntas e entretenimento.
    Você tem acesso a ferramentas para pesquisar na web e reproduzir músicas no YouTube.""")
)

def modo_texto():
    """Inicia o assistente no modo de comandos por texto."""
    global interface
    print("\n⌨️ Modo de Texto iniciado - digite seu comando ou 'sair' para encerrar.")
    
    import pygame
    while True:
        if interface:
            pygame.event.pump()
        comando = input("\n🔤 Digite seu comando: ").strip().lower()
        
        if comando == "sair":
            print("\n👋 Encerrando o modo de texto...")
            if interface:
                interface.stop()
            return
        
        try:
            # Atualiza a interface para mostrar que está pensando
            if interface:
                interface.start_thinking()
                pygame.event.pump()
                
            # Processa a resposta
            resposta = agent.run(comando)
            
            # Atualiza a interface para mostrar que está respondendo
            if interface:
                interface.start_talking()
                pygame.event.pump()
                
            print(f"\n🧠 Jarvis: {resposta}")
            
            # Adiciona um pequeno delay para permitir que a animação de fala seja vista
            time.sleep(len(resposta) * 0.05)  # Tempo proporcional ao tamanho da resposta
            
            # Volta para o estado neutro
            if interface:
                interface.stop_talking()
                pygame.event.pump()
                
        except Exception as e:
            print(f"\n❌ Erro: {e}")
            if interface:
                interface.stop_talking()

# Variável global para a interface gráfica
interface = None

# Interface de linha de comando simples
if __name__ == "__main__":
    print("\n🤖 JARVIS - Assistente Pessoal")
    
    # Inicializa a interface gráfica
    try:
        interface = JarvisInterface()
        interface.start()
        print("✅ Interface gráfica iniciada.")
    except Exception as e:
        print(f"⚠️ Não foi possível iniciar a interface gráfica: {e}")
        interface = None
    
    # Inicia o assistente no modo de voz
    modo_voz()