import PyPDF2  # Ігноруємо потенційні попередження про типи від PyPDF2
import pyttsx3 # Ігноруємо потенційні попередження про типи від pyttsx3


with open(r'C:\Users\SERGIYYY\Desktop\Pdf_to_Audio\Ukraine.pdf', 'rb') as pdf_file: # Відкриваємо PDF-файл у двійковому режимі для читання
    reader = PyPDF2.PdfReader(pdf_file) # Створюємо об'єкт PdfReader для читання файлу
    speaker = pyttsx3.init() # Ініціалізуємо об'єкт для перетворення тексту в мовлення

    rate = speaker.getProperty('rate') # Отримуємо поточну швидкість мовлення
    speaker.setProperty('rate', 150) # Встановлюємо нову швидкість мовлення (150 слів за хвилину)

    for pagenumber in range(len(reader.pages)): # Цикл по всіх сторінках PDF-файлу
        page = reader.pages[pagenumber] # Отримуємо поточну сторінку
        text = page.extract_text() # Витягуємо текст зі сторінки
        speaker.say(text) # Перетворюємо текст у мовлення і відтворюємо його
        speaker.runAndWait() # Перетворюємо текст у мовлення і відтворюємо його

    speaker.save_to_file(text, r'C:\Users\SERGIYYY\Desktop\Pdf_to_Audio\result.mp3') # Зберігаємо озвучений текст у MP3-файл. # УВАГА: цей рядок зберігає лише текст останньої сторінки!
    speaker.runAndWait() # Чекаємо завершення запису у файл