import PyPDF2 # type: ignore
import pyttsx3 # type: ignore

with open(r'C:\Users\SERGIYYY\Desktop\pd.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    speaker = pyttsx3.init()

    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', 100)

    for pagenumber in range(len(reader.pages)):
        page = reader.pages[pagenumber]
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

    speaker.save_to_file(text, r'C:\Users\SERGIYYY\Desktop\audio.mp3')
    speaker.runAndWait()