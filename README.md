# JARVIS - Assistente Pessoal com IA

Um assistente pessoal avançado baseado em IA que combina o poder do processamento de linguagem natural com automação para ajudar em tarefas diárias.

## 🌟 Funcionalidades

### ✅ Implementado

- **🎵 Controle de Música por Voz**

  - Tocar música: "Jarvis tocar [nome da música]" (abre o YouTube com a pesquisa)
  - Pausar: "Jarvis pausar" (clica no player para pausar)
  - Retomar: "Jarvis tocar" (sem nome da música, retoma a reprodução)
  - Parar: "Jarvis parar" (fecha o navegador)
  - Inteligência para reconhecer variações de comandos (ex: "para", "parar", "stop", etc)

- **🎙️ Reconhecimento de Voz**

  - Motor de reconhecimento usando Google Speech Recognition
  - Ajuste automático para ruído ambiente
  - Detecção de palavra-chave "Jarvis"

- **🤖 Interface de Linha de Comando**
  - Modo texto
  - Modo voz

### 🔜 A Implementar

- **🔍 Pesquisa na Internet**

  - Integração com mecanismos de busca
  - Funcionalidades avançadas de pesquisa web

- **📰 Últimas Notícias**

  - Integração com Brave API para buscar notícias atualizadas
  - Filtros por categoria e relevância

- **⏰ Informação de Horário e Data**

  - Verificar hora atual
  - Consultar datas e calendário

- **📅 Gerenciamento de Agenda**

  - Integração com Google Calendar
  - Agendamento e consulta de tarefas e compromissos

- **💬 Conversa Natural**
  - Interação conversacional usando IA avançada
  - Personalidade amigável e adaptável

## 🛠️ Tecnologias e Bibliotecas

### Principais

| Biblioteca            | Uso                                            | Alternativas                        |
| --------------------- | ---------------------------------------------- | ----------------------------------- |
| **LangChain**         | Framework de IA para criar aplicações com LLMs | LlamaIndex, Haystack                |
| **Gemini AI**         | Modelo de linguagem (LLM)                      | OpenAI GPT, Anthropic Claude, Llama |
| **SpeechRecognition** | Reconhecimento de voz                          | Whisper, DeepSpeech, Vosk           |
| **PyAutoGUI**         | Automação de cliques e controle de interface   | Pywinauto, AutoIt, RPA Framework    |

### Extras e Utilidades

| Biblioteca        | Uso                                        | Alternativas               |
| ----------------- | ------------------------------------------ | -------------------------- |
| **python-dotenv** | Carregamento de variáveis de ambiente      | os.environ, configparser   |
| **Selenium**      | Automação de navegador                     | Playwright, Puppeteer      |
| **subprocess**    | Execução de processos externos             | os.system, multiprocessing |
| **re**            | Expressões regulares para análise de texto | regex                      |

### APIs e Integrações

| API                           | Uso                     | Alternativas                              |
| ----------------------------- | ----------------------- | ----------------------------------------- |
| **Google Speech Recognition** | Reconhecimento de voz   | Mozilla DeepSpeech, Whisper API           |
| **Brave API**                 | Pesquisa e notícias     | Google Custom Search, News API            |
| **Google Calendar API**       | Gerenciamento de agenda | Microsoft Graph (Outlook), Apple Calendar |

## 🚀 Instalação

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/jarvis.git
cd jarvis

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env e adicione suas chaves de API
```

## 📋 Requisitos

- Python 3.8+
- Google Chrome ou Brave Browser
- Microfone (para modo de voz)
- Acesso à Internet
- Chave de API do Google (para o Gemini)
- Chave de API do Brave (para notícias)
- Permissões OAuth para Google Calendar

## ⚙️ Configuração

1. Obtenha uma chave de API do Google AI Studio para o Gemini
2. Configure suas credenciais no arquivo `.env`:
   ```
   GOOGLE_API_KEY=sua_chave_aqui
   BRAVE_API_KEY=sua_chave_brave_aqui
   ```
3. Para integração com Google Calendar, siga o [guia oficial](https://developers.google.com/calendar/api/quickstart/python)

## 💻 Uso

```bash
# Iniciar o JARVIS
python jarvis.py
```

## 🧩 Personalização

Você pode personalizar o JARVIS editando as seguintes configurações:

- Comandos de voz no arquivo `jarvis.py`
- Adicionar novas ferramentas e habilidades ao agente

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## 🙏 Agradecimentos

- Google AI por fornecer o modelo Gemini
- Contribuidores e mantenedores de todas as bibliotecas usadas

---

_Desenvolvido com ❤️ por [Seu Nome]_
