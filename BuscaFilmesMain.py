import sys, requests, json
from designBuscaFilmes import *
from functools import partial
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets

#APIKEY = d3078a74
paginaAtual = 1
fimResultados = False

class MainWindow(QMainWindow, Ui_MainWindow):

 
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        #Nome que aparece no topo da janela
        self.setWindowTitle("Buscador de Filmes e Séries") 
        
        #O usuário deverá clicar em 'Pesquisar! ou pressionar Enter para dar início à busca'
        self.ButtonPesquisar.clicked.connect(self.eventoBusca, True)
        self.lineEditTitulo.returnPressed.connect(partial(self.eventoBusca, True))
        
        #As informações sobre o filme/serie são mostradas quando o respectivo itens no tableWidget for clicado
        self.tbWidgetResult.clicked.connect(self.detalhes)
        
        #O usuário pode avançar e voltar páginas atráves desses botões
        self.ButtonProxima.clicked.connect(partial(self.eventoControlePaginas, 'proxima'))
        self.ButtonAnterior.clicked.connect(partial(self.eventoControlePaginas, 'anterior'))
        
    
    ##################################################################
    #Função que faz pesquisa (search: ?s) com base no título digitado 
    #e escolha dos filtros Ano e Tipo 
    ##################################################################
    def eventoBusca(self, novaPesquisa):       
        print(f'Título: {self.lineEditTitulo.text()}  Ano: {self.comboBoxAno.currentText()}  Tipo: {self.comboBoxTipo.currentText()}')
        
        #Tratamento do Título
        TituloBusca = self.lineEditTitulo.text()
        TituloBusca = TituloBusca.strip()      
        TituloBusca = TituloBusca.replace(' ', '+')
        
        #Tratamento dos Filtros Ano e Tipo
        if(self.comboBoxAno.currentText() == '------'): #Ano não especificado
            AnoBusca = ''
        else:
            AnoBusca = '&y='+self.comboBoxAno.currentText()
            
        if(self.comboBoxTipo.currentText() == '------'): #Tipo não especificado
            TipoBusca = '' 
        else:
            TipoBusca = '&type='+self.comboBoxTipo.currentText()            
        
        global paginaAtual
        global fimResultados
        
        #Verifica se é o começo de uma pesquisa (novo nome buscado ou nova escolha nos filtros)
        if(novaPesquisa == True):
            paginaAtual = 1
        
        #URL composta
        url = 'http://www.omdbapi.com/?s='+TituloBusca+AnoBusca+TipoBusca+'&page='+str(paginaAtual)+'&apikey=d3078a74'
        print(f'Busca na api: {url}')
        
        try:
            #Acessa a url e cria o dicionário
            req = requests.get(url)
            dicionario = json.loads(req.text)
            
            #Chama a função que exibe os resultados no tableWidget
            self.exibeBusca(dicionario['Search'])
            
            #Aplica a quantidade de resultados encotrados em um label
            self.labelNumResult.setText(str(dicionario['totalResults'])+' resultados')
           
            #Calcula o número de páginas com base na quantidade de resultados
            if (int(dicionario['totalResults']) % 10 != 0):
                NumPagTotal = (int(dicionario['totalResults']) // 10) + 1
            else:
                NumPagTotal = int(dicionario['totalResults']) // 10
            
            fimResultados = False
            self.labelNumPag.setText(f'{paginaAtual}/{NumPagTotal}')
            self.labelNumPag.adjustSize()
        
        except Exception as erro:
            print(f'Não foi possível fazer a pesquisa ou a página não foi encontrada. Erro: {erro}')
            fimResultados = True

    ############################
    #Função para obter o poster
    ############################
    def eventoGetPoster(self, url):
        with open('Poster.jpg', 'wb') as handle:
            response = requests.get(url, stream = True)
            if not response.ok:
                print(response)
            
            else:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
    
    ###############################################################
    #Função para exibição dos resultados encotrados no tableWidget
    ###############################################################
    def exibeBusca(self, dic):
        self.tbWidgetResult.setRowCount(1)
        
        i = 0       
        for filme in dic:
            i += 1
            self.tbWidgetResult.insertRow(i)
            self.tbWidgetResult.setItem(i-1, 0, QtWidgets.QTableWidgetItem(str(filme['Title'])))
            self.tbWidgetResult.setItem(i-1, 1, QtWidgets.QTableWidgetItem(str(filme['Year'])))           
            self.tbWidgetResult.setItem(i-1, 2, QtWidgets.QTableWidgetItem(str(filme['Type'])))           
            self.tbWidgetResult.setItem(i-1, 3, QtWidgets.QTableWidgetItem(str(filme['imdbID'])))
        
        if(i > 0):
            self.tbWidgetResult.removeRow(i)
        
        header = self.tbWidgetResult.horizontalHeader() 
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    
    ###############################################
    #Função para acessar as páginas dos resultados
    ###############################################
    def eventoControlePaginas(self, opcao):
        global paginaAtual
        global fimResultados
        
        if(opcao == 'proxima' and fimResultados == False):
            paginaAtual += 1
        
        if(opcao == 'anterior' and fimResultados == False and paginaAtual > 1):
            paginaAtual -= 1
        
        elif(opcao == 'anterior' and fimResultados == True and paginaAtual > 1):
            paginaAtual -= 2
        
        return self.eventoBusca(False)        
    
    ############################################
    #Função responsavel por mostrar os detalhes 
    #do item escolhido no tableWidget
    ############################################
    def detalhes(self):
        linha = self.tbWidgetResult.currentRow()
        item = self.tbWidgetResult.selectedItems()
        imdbID = self.tbWidgetResult.item(linha, 3).text()
        
        #Pesquisa pelo imdbID
        url = 'http://www.omdbapi.com/?i='+imdbID+'&plot=full&apikey=d3078a74'
        print(f'Busca pelo imdbID: {url}')
        
        try:
            #acessa a url e cria o dicionário
            req = requests.get(url)
            dicionario = json.loads(req.text)            
            
            #Aplica as informações nas labels
            self.labelDiretorExibe.setText(dicionario["Director"])

            self.labelTituloExibe.setText(dicionario["Title"])
          
            self.labelAnoExibe.setText(dicionario["Year"])
           
            self.labelGeneroExibe.setText(dicionario["Genre"])
 
            self.labelIMDBExibe.setText(dicionario["imdbRating"])
            
            self.plainTESinopse.setPlainText(dicionario['Plot'])
            self.plainTESinopse.setReadOnly(True)
            
            self.labelAnoExibe.adjustSize()
        
        except Exception as erro:
            print(f'Erro na busca pelas informações. Erro {erro}')
            
        try:
            self.eventoGetPoster(dicionario["Poster"])
            pixmap = QPixmap('Poster.jpg').scaled(201,266)
            self.labelPoster.setPixmap(pixmap)           
        
        except Exception as erro:
            self.labelPoster.setText("Sem Poster") 

if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MainWindow()
        window.setWindowIcon(QIcon('icon.jpg'));
        window.show()
        app.exec_()