import chess
import chess.engine
from functools import lru_cache
import pathlib, os
from datetime import datetime, timedelta, date
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import namedtuple
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, csv

class Chess_hint:
    def __init__(self, url):
        self.board = chess.Board() # Создать новую шахматную доску (стандартную 8×8)
        self.url = url
        self.db = []

    def viewing_branch(self):

        
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome()
        driver.get(self.url)
        # Получаем элементы по тегам
        #i5z_elements = driver.find_elements(By.TAG_NAME, 'i5z')  # Находим все элементы <i5z>
        kwdb_elements = driver.find_elements(By.TAG_NAME, 'kwdb')  # Находим все элементы <kwdb>

        self.db = list(filter(lambda a: a!='', [gs.text for gs in kwdb_elements]))
        driver.quit()

        # Прогружаем историю доски
        for i in self.db:
            self.board.push_san(str(i)) 
  
        engine_path = 'stockfish/stockfish-windows-x86-64'  # Замените на путь к исполнителю Stockfish
        engine = chess.engine.SimpleEngine.popen_uci(engine_path)
        info_hint = engine.analyse(self.board, chess.engine.Limit(depth=20), multipv=1)

        return info_hint[0]['pv'][0]


        
