# SeleniumComPy
Aprendendo

-- Tudo que foi usado --

- python 3.11.1 (ultima versao)
- selenium 
- behave
- cucumber

- IDE Que eu usei -
  Pycharm
  
 -- Baixando o ambiente --
 
 -Primeiro: tem que ter o python instalado na maquina
 
 possivel fazer o dowload nesse link: https://www.python.org/downloads/
 
 -Segundo: tem que instalar o selenium
 
 isso é feito pela cmd digitando: pip install selenium
 
 -Terceiro: instalar o behave
 
 mesma coisa do selenium só que digitando: behave no lugar de selenium
 
-- Pycharm -- 

tem que baixar o plugin do gherkin 

na barra superior clica em File/ settings ou (Ctrl+Alt+s)

depois plugins, marketplace e pesquise por Gherkin 

- feito isso tem que configurar os packs do pycharm 
 
 em settings procure por Project
 
 dentro disso clica em python interpreter
 
 e vai no botao com simbolo de (+)
 
pesquisa selenium instala e depois behave instala tambem 

com isso ja da pra usar 

-- EXECUÇÃO --

pra executar o cenario criado na pasta feature 
tem que ir no terminal e digitar: behave .\features\(nome da sua feature).feature
assim o behave vai executar a sua feature 

-- Organizando as pastas --

feature/steps 

criei essas pastas 

o arquivo (.feature fica dentro da pasta features)

e os arquivos (.py fica dentro de steps)

-- Minha feature --

cenario simples so para ver como funciona testes com python 



    #language: pt
   
    Funcionalidade: cucumber com python só para aprender
 
        como um usuario
        quero acessar lojas americanas
        e fazer uma pesquisa de um produto

    Cenario: iniciando a pesquisa
         Dado que devo acessar o site
         E validar que estou no site
         Entao devo fazer a pesquisa
         Quando eu fazer a pesquisa clico na lupa
         E depois devo validar que a pesquisa foi feita
         Quando for validado devo sair do site 
