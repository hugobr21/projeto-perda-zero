from dataclasses import dataclass
from dataclasses import field
import json

@dataclass
class setupPrograma:
    """Classe para lidar com configurações do programa"""

    perfilFirefox1: str = ''
    perfilFirefox2: str = ''
    caminhoFirefox: str = ''

    def configurar_parametros(self) -> None:
        """Define os parâmetros do programa"""

        self.perfilFirefox1 = input('Insira o caminho da pasta de perfil do Firefox: ').strip()
        self.perfilFirefox2 = input('Insira o caminho da pasta de perfil do Firefox: ').strip()
        self.caminhoFirefox = input('Insira o caminho do executável do Firefox: ').strip()
        self.salvar_parametros()

    def carregar_parametros(self) -> None:
        """Carrega parametros existentes de configuração do programa"""
    
        try:
            with open("parametros.json", "r") as infile:
                parametros = json.load(infile)
            self.perfilFirefox1 = parametros["perfilFirefox2"]
            self.perfilFirefox2 = parametros["perfilFirefox1"]
            self.caminhoFirefox = parametros["caminhoFirefox"]
        except:
            self.configurar_parametros()

    def salvar_parametros(self) -> None:
        """Salvar arquivo em JSON com parâmetros"""

        parametros = {
        "perfilFirefox1": self.perfilFirefox1,
        "perfilFirefox2": self.perfilFirefox2,
        "caminhoFirefox": self.caminhoFirefox
        }

        with open("parametros.json", "w") as outfile:
                json.dump(parametros, outfile)

    def mostrar_parametros(self) -> None:
        """Mostrar parâmetros atuais"""

        print('','\n',
        "Caminho da pasta de perfil 1 do Firefox: ", self.perfilFirefox1,'\n',
        "Caminho da pasta de perfil 2 do Firefox: ", self.perfilFirefox2,'\n',
        "Caminho do executável do Firefox: ",self.caminhoFirefox,'\n')