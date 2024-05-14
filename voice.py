import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time


# speech to text
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understant")

# text to speech
def speechtx(x):
    engine = pyttsx3.init()
    voices =engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()

if __name__ =='__main__':

    if "hey buddy" in  sptext().lower():
        while True: 
            data1 = sptext().lower()

            if "your name" in data1:
                name = "I am Voice Assistant"
                speechtx(name)

            elif "old are you" in data1:
                age ="I am build in April-2024"
                speechtx(age)

            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif 'linkedin' in data1:
                webbrowser.open("https://www.linkedin.com/in/gaurika-sehgal-b0abba201/")

            
            elif 'picture' in data1:
                    from PIL import Image, ImageDraw, ImageFont
                    def create_image_with_text(text, filename):
                            # Create a blank image with white background
                            img = Image.new('RGB', (200, 100), color = (255, 255, 255))
                            d = ImageDraw.Draw(img)
                            # Using a basic font
                            font = ImageFont.load_default()
                            d.text((10,10), text, font=font, fill=(0,0,0))
                            # Save the image
                            img.save(filename)

                    # Input text
                    text = "hi how are you"

                    # Output file
                    filename = 'test_image.png'

                    # Create the image
                    create_image_with_text(text, filename)
                    
            
            elif 'exit' in data1:
                speechtx("Thanks")
                break

            time.sleep(10)


    else:
        print("thanks")
