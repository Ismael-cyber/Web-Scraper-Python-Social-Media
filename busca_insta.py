from playwright.sync_api import sync_playwright
import time
import os
from dotenv import load_dotenv
import logging

# Configuração básica dos logs do sistema
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Carregando variáveis
load_dotenv()

# Acesso as Variaveis
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PERFIL_BUSCADO = os.getenv("PERFIL_BUSCADO")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Entra no Perfil do Instagram
    page.goto("https://instagram.com/")
    logging.info("Iniciando navegação para Instagram")
    time.sleep(10)

    # Espera específica adicional
    page.wait_for_load_state("networkidle")

    # Fazer Login na Conta
    logging.info("Entrando na conta")
    page.get_by_label("Número de celular, nome de usuário ou email").fill(EMAIL)
    time.sleep(7)
    page.get_by_label("Senha").fill(PASSWORD)
    time.sleep(9)
    page.locator('span span:has-text("Entrar")').first.click()
    time.sleep(14)
    logging.info("Login realizado com sucesso")

    # Espera específica adicional
    page.wait_for_load_state("networkidle")

    # Entrar na barra de pesquisa
    logging.info("Entrando na barra de pesquisa, para realizar captação")    
    page.locator('span span:has-text("Pesquisa")').first.click()
    time.sleep(10)

    # Realizando pesquisa dos perfis
    page.locator('span:has-text("Pesquisar")').fill(PERFIL_BUSCADO)
    logging.info("Inserindo o nome do perfil do lead")
    time.sleep(5)

    # Escolhendo (Click do Mouse) o perfil do cliente
    page.locator('span:has-text("{PERFIL_BUSCADO}")').click()
    logging.info("Selecionado o perfil do cliente.")
    time.sleep(10) 

    # Captura da tela do perfil do Instagram
    page.screenshot(path="Sucess.png")
    logging.info("Captura da Vitória!")

    browser.close()