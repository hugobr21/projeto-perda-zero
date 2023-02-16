from minhas_funcoes.bases_de_dados import baseDeDadosGoogle
import xlwings as xw

instancia_teste = baseDeDadosGoogle(idBaseAssistente="1taUVEmnNEf8tCb2HNO9tWIunfYFD2k4DtBOUX3qeiyY")

app = xw.App(visible = False, add_book = False)

wb = xw.Book(r"Fechamento de Inventário diário.xlsm")
wb.activate()
ws = wb.sheets["Sheet1"]
app.screen_updating = False
instancia_teste.subir_base_assistente(ws[f"analise_historico_de_pacotes"].options(index=False).value)
app.screen_updating = True
app.quit()