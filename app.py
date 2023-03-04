{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0b33e20f-feca-4a04-99e4-b796995ccbbb",
   "metadata": {},
   "source": [
    "Preencher Formulário"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f6c155bd",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "\n",
    "servico = Service(ChromeDriverManager().install())\n",
    "\n",
    "navegador = webdriver.Chrome(service=servico)\n",
    "\n",
    "navegador.get(\"https://ola.oleconsignado.com.br\")\n",
    "\n",
    "navegador.find_element('xpath', '//*[@id=\"Senha\"]').send_keys(\"Corban2023*\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
