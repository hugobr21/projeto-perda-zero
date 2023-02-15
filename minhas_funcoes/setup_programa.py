from dataclasses import dataclass
from dataclasses import field
import os

@dataclass
class setupPrograma:
    """Classe para lidar com configurações do programa"""

    caminhoPasta: str = ''

    def gerar_arquivo_arquivos_bat(self) -> None:
        """Gera o arquivo batch para atualizar tabela do excel"""

        self.caminhoPasta = os.getcwd()

        codigo = f"""Chcp 65001\ncall C:\\Users\\%USERNAME%\\Anaconda3\\Scripts\\activate.bat\ncd {self.caminhoPasta}\nC:\\Users\\%USERNAME%\\Anaconda3\\python.exe "%CD%\\subir_tabela_assistente.py"""

        with open("subir_tabela_assistente.bat", "w",encoding='utf-8') as outfile:
            outfile.write(codigo)

    