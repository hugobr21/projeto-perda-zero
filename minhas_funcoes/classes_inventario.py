from dataclasses import dataclass
from dataclasses import field
import time
import os

@dataclass
class pacotes:
    """Classe para lidar com pacotes"""

    ids: list[str] = field(default_factory=list)
    idsconsultados: list[str] = field(default_factory=list)
    status: list[str] = field(default_factory=list)
    usuarioResponsavel: list[str] = field(default_factory=list)
    historicoSemUsuario: list[str] = field(default_factory=list)
    contagemProgresso: int = 0


    def tranformar_historico_em_tabela(self,pd):
        """Transforma historico logistics em tabela"""

        tabela_historico = pd.DataFrame({'ID':[],'Histórico':[]})
        time_agora = time.strftime('%d_%m_%Y %H_%M_%S')

        for id_,j in self.historicoSemUsuario:
            historico = []
            indices = []            
            for i in range(len(j)):
                if j[i] == '/':
                    indices.append(i-2)
            for i in range(len(indices)):
                try:
                    historico.append(j[indices[i]:indices[i+1]])
                except:
                    historico.append(j[indices[i]:])
            historico_corrente = pd.DataFrame({'Histórico':historico})
            historico_corrente['ID'] = id_
            tabela_historico = pd.concat([tabela_historico,historico_corrente])

        tabela_historico['Histórico'].str.split('|',expand = True)
        tabela_historico['Data'] = tabela_historico['Histórico'].str.split().str[0]
        tabela_historico['Hora'] = tabela_historico['Histórico'].str.split().str[1]
        tabela_historico['Evento'] = tabela_historico['Histórico'].str.split('|').str[1].str.split('\n').str[1]
        tabela_historico['ID'] = tabela_historico['ID'].astype('int64')
        self.historicoSemUsuario = tabela_historico

    def mostrar_progresso(self):
        """Mostra progresso da quantidade de pacotes com captura de histórico realizada"""

        self.contagemProgresso += 1
        os.system('cls')
        barradeprogresso = '='*int(self.contagemProgresso*100/len(self.ids))
        print(f'{self.contagemProgresso} pacotes consultados de {len(self.ids)}\n{self.contagemProgresso/len(self.ids):.1%} |{barradeprogresso}|')

    def consolidar_historico_sem_usuario(self, driver, By, pd):
        """Consolida histórico de movimentações do pacote sem o usuário que realizou a movimentação"""

        self.ids = list(set(self.ids))

        for id in self.ids:
            if id in self.idsconsultados: continue
            driver.get(f'https://envios.mercadolivre.com.br/logistics/management-packages/package/{id}')
            while True:
                historico = driver.find_elements(By.CLASS_NAME, 'package-history-list')
                if len(historico) > 0 and 'hs' in historico[0].text and driver.current_url == f'https://envios.mercadolivre.com.br/logistics/management-packages/package/{id}': break
                elif len([i for i in driver.find_elements(By.TAG_NAME, 'p') if i.text == 'Erro ao buscar os dados']) > 0:
                    driver.refresh()
                    continue
                elif len([i for i in driver.find_elements(By.TAG_NAME, 'h4') if i.text == 'Ops! Ocorreu um erro']) > 0:
                    driver.refresh()
                    continue                
                else: 
                    time.sleep(1)
                    pass
            self.historicoSemUsuario += [[id,historico[0].text]]
            self.idsconsultados += [id]
            self.mostrar_progresso()
        
        self.tranformar_historico_em_tabela(pd)

    def exportar_para_excel(self) -> None:
        """Exporta histórico dos pacotes em questão para pasta 'Arquivo'"""

        self.historicoSemUsuario[['ID','Histórico','Data','Evento']].to_excel(f'Arquivo\Histórico de pacotes - {time_agora}.xlsx')

    def limpar_atributos(self) -> None:
        """Limpa atributos da classe"""
        
        self.ids: str = ''
        self.status: str = ''
        self.usuarioResponsavel: str = ''
        self.historicoSemUsuario: str = ''
        self.contagemProgresso: int = 0