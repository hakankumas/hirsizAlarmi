import RPi.GPIO as GPIO
import time
import smtplib
import datetime

def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return

counter = 1
while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.IN)
    m = "Musteri"

    if GPIO.input(16):
        print(counter, m)
        counter = counter + 1
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18, GPIO.OUT)
        for i in range(0, 1):
            blink(18)
        GPIO.cleanup()

    if (datetime.datetime.now().strftime("%H:%M:%S") == "18:33:18"):
        counter = counter - 1
        content = str(counter)
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("emailGiriniz","sifreGiriniz")
        mail.sendmail("emailGiriniz","emailGonderilecekHesabinAdi",content)
        print("Mail Gönderildi")
        break
        
    time.sleep(1)


