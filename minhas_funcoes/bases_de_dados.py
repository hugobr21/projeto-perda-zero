from dataclasses import dataclass, field
from google_api_functions import get_values, update_values
import pandas as pd
import datetime
import re
import numpy as np
import os

@dataclass
class baseDeDadosGoogle:
    """Classe para lidar com interações com bases de planilhas do Google"""

    idBaseAssistente: list[str] = field(default_factory=list)
    idBaseAnalista: list[str] = field(default_factory=list)

    def subir_base_assistente(self, tabela) -> None:
        """Sobe dados manipulados pelo assistente de inventário"""

        update_values(self.idBaseAssistente, "'Base Assistente'!A2:T", "USER_ENTERED", tabela)