from behave import given, then, when
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@given(u'que devo acessar o site')
def acessando (context):
    print("começando teste")
    driver.get("https://www.americanas.com.br") #entrando no site das americanas
    time.sleep(2)

@given(u'validar que estou no site')
def validando_site(context):
     assert "Americanas" in driver.title
     time.sleep(2)

@then(u'devo fazer a pesquisa')
def fazendo_pesquisa(context):
    driver.find_element('xpath', '//*[@id="rsyswpsdk"]/div/header/div[1]/div[1]/div/div[1]/form/input').send_keys("fone de ouvido") #escrevendo na barra de pesquisa
    time.sleep(2)

@when(u'eu fazer a pesquisa clico na lupa')
def step_impl(context):
    clic = driver.find_element('xpath', '//*[@id="rsyswpsdk"]/div/header/div[1]/div[1]/div/div[1]/form/button').click()
    #driver.execute_script("arguments[0].click();", clic)
    time.sleep(2)


@when(u'depois devo validar que a pesquisa foi feita')
def step_impl(context):
    assert "Fone" in driver.title
    time.sleep(2)

@when(u'for validado devo sair do site')
def saindo_do_site(context):
    driver.quit()
    print("terminando o teste")

