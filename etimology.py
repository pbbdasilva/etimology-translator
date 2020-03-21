from bs4 import BeautifulSoup
import requests
from googletrans import Translator


def etimology(word):
    splitted_word = word.split()
    print(splitted_word)
    url = 'https://www.etymonline.com/search?q='
    for i in range(0, len(splitted_word)):
        url = url + splitted_word[i]
        if i == len(splitted_word)-1:
            pass
        else:
            url = url + '+'
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    source_of_knowledge = soup.find('section', class_='word__defination--2q7ZH undefined')
    return source_of_knowledge.text



def main():
    word = input('Digite uma palavra: ')
    translator = Translator()
    translated = translator.translate(text=word, src='pt', dest='en')
    traduzido = etimology(translated.text)
    retranslated = translator.translate(text=traduzido, src='en', dest='pt')
    print(retranslated.text)


if __name__ == '__main__':
    main()

