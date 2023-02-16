from dataclasses import dataclass, field
from google_api_functions import get_values, update_values, ultima_linha
import pandas as pd
import datetime
import re
import numpy as np
import os

@dataclass
class baseDeDadosGoogle:
    """Classe para lidar com interações com bases de planilhas do Google"""

    idBaseAssistente: list[str] = field(default_factory=list)

    def subir_base_assistente(self, tabela) -> None:
        """Sobe dados manipulados pelo assistente de inventário"""
        ultima_linha_colunaA = ultima_linha(self.idBaseAssistente,"'Base Assistente'!A:A")
        update_values(self.idBaseAssistente, f"'Base Assistente'!A{ultima_linha_colunaA}:Z", "USER_ENTERED", tabela)