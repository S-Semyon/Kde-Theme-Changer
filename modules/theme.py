import subprocess
import os
from typing import List
from dataclasses import dataclass

HOME_DIR = os.getenv('HOME')
CONFIG_PATH = os.path.join(HOME_DIR, '.config')
DATA_PATH = os.path.join(HOME_DIR, '.local', 'share')
SAVE_PATH = os.path.join(CONFIG_PATH, 'kde_changer')

class ThemeNotExistException(Exception):
    def __init__(self, theme_name: str) -> None:
        super().__init__()
        self.theme_name = theme_name
    
    def __str__(self) -> str:
        return f'Theme "{self.theme_name}" is not exist!"'

@dataclass
class theme_data:
    name: str
    path_to_img: str
    path: str

def get_theme(theme_name: str):
    """Получить тему"""
    for f in os.scandir(SAVE_PATH):
        if not f.is_dir():
            continue
        if f.name == theme_name:
            return theme_data(f.name, f.path + "/screenshot.png", f.path)
    return None

def check_theme(theme_name: str):
    """Проверка темы"""
    listThemes = list_themes()
    themes = []
    for i in listThemes:
        if isinstance(i, theme_data):
            themes.append(i.name)
    if theme_name in themes:
        return True
    raise ThemeNotExistException(theme_name)

def load_theme(theme_name: str):
    """Установка темы"""
    check_theme(theme_name)
    SCRIPT_PATH = os.getenv('PATH_SCRIPT')
    path = os.path.join(SCRIPT_PATH, "scripts/load.sh")
    try:
        subprocess.run(['sh', path, CONFIG_PATH, SAVE_PATH, DATA_PATH, theme_name], check=True) # запуск sh скрипта
        print("Theme loaded")
    except subprocess.CalledProcessError:
       import traceback
       traceback.print_exc()

def save_theme(theme_name: str):
    """Сохранение темы"""
    CONFIGFOLDER = SAVE_PATH + "/" + theme_name
    SCRIPT_PATH = os.getenv('PATH_SCRIPT')
    path = os.path.join(SCRIPT_PATH, "scripts/save.sh")
    try:
        subprocess.run(['sh', path, CONFIG_PATH, CONFIGFOLDER, DATA_PATH], check=True) # запуск sh скрипта
        print("Theme saved")
    except subprocess.CalledProcessError:
       import traceback
       traceback.print_exc()

def del_theme(theme_name: str):
    check_theme(theme_name)
    CONFIGFOLDER = SAVE_PATH + "/" + theme_name
    subprocess.run([f"rm -Rf {CONFIGFOLDER}"], shell = True)
    
def list_themes() -> List[theme_data | None]:
    """Список тем"""
    try:
        themes = []
        for f in os.scandir(SAVE_PATH):
            if not f.is_dir():
                continue
            themes.append(theme_data(f.name, f.path + "/screenshot.png", f.path))
        return themes
    except FileNotFoundError:
        return []
