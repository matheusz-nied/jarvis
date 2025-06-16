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

# Tenta importar pyautogui para automação de cliques
try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except ImportError:
    PYAUTOGUI_AVAILABLE = False
    print("[AVISO] PyAutoGUI não está instalado. Alguns recursos avançados de clique não estarão disponíveis.")
    print("Instale com: pip install pyautogui")


def tocar_musica(query: str):
    # Formata a URL para busca de vídeos no YouTube
    url_search = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}&sp=EgIQAQ%253D%253D"
    
    print(f"[MÚSICA] Tentando tocar: {query}")
    
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

# 💧 Exemplo de uso
comando = "Quero ouvir imagine dragons natural no YouTube"

tocar_musica(comando)
while True:
    comando = input("Eu: ")
    resposta = agent.run(comando)
    print(f"\n📢 Resposta do assistente: {resposta}")