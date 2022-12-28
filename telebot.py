import telebot
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys


executable_path = 'C:/chromedriver.exe'
service = ChromeService(executable_path=executable_path)
driver = webdriver.Chrome(service=service)





logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = ''

bot = telebot.TeleBot(TOKEN)


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            logging.info(f'{m.chat.first_name}: {m.text}')


bot.set_update_listener(listener)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!Начнем?Скажи свой Знак зодиака(например Лев) и я скажу что тебя сегодня ждет!')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    print('Получено сообщение:', message.text)
    logger.info('Received message from %s: %s', message.chat.id, message.text)
    word = message.text
    driver.get('https://vk.com/kokoskop')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if len(word) < 3:
        bot.send_message(message.chat.id, 'Прогнозы со знаком зодиака "{}" не найдены.Может вы допустили ошибку?Попробуйте еще раз.'.format(word))
    else:
        if word == 'рыба' or word == 'Рыба' or word == 'рыбы' or word == 'Рыбы':
            word = 'РЫБЫ'
        if word == 'лев' or word == 'Лев':
            word = 'ЛЬВЫ'
        if word == 'козерог' or word == 'Козерог':
            word = 'КОЗЕРОГИ'
        if word == 'телец' or word == 'Телец':
            word = 'ТЕЛЬЦЫ'
        if word == 'водолей' or word == 'Водолей':
            word = 'ВОДОЛЕИ'
        if word == 'скорпион' or word == 'Скорпион':
            word = 'СКОРПИОНЫ'
        if word == 'рак' or word == 'Рак':
            word = 'РАКИ'
        if word == 'близнецы' or word == 'Близнецы':
            word = 'БЛИЗНЕЦЫ'
        if word == 'стрелец' or word == 'Стрелец':
            word = 'СТРЕЛЬЦЫ'
        if word == 'весы' or word == 'Весы':
            word = 'ВЕСЫ'
        if word == 'дева' or word == 'Дева':
            word = 'ДЕВЫ'
        if word == 'овен' or word == 'Овен':
            word = 'ОВНЫ'
        posts = driver.find_elements(By.CLASS_NAME, 'wall_text')
        for post in posts:
            sms = post.find_element(By.CLASS_NAME, 'wall_post_text')
            title = sms.text
            print (title)
            if word in title:
                img_element = post.find_element(By.CSS_SELECTOR, 'img')
                img_url = img_element.get_attribute('src')
                bot.send_photo(message.chat.id, img_url, caption=title)
                break
        else:
            bot.send_message(message.chat.id, 'Прогнозы со знаком зодиака "{}" не найдены.Может вы допустили ошибку?Попробуйте еще раз.'.format(word))


bot.infinity_polling()