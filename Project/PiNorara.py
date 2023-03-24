from flask import Flask
from flask import render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
# GPIO에 대한 설정
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12,GPIO.OUT)

pwm=GPIO.PWM(12,1.0)
scale = [523, 391, 329, 415, 440, 415, 391, 415, 391, 369, 369]
snake_scale = [659, 523]

# 이하 app.route는 각 페이지나 GPIO 및 센서를 flask에서 제어한 함수들
@app.route("/")
def mainpage():
    return render_template("MainPage.html")


@app.route("/SelectPage")
def selectpage():
    return render_template("SelectPage.html")


@app.route("/Dodge")
def dodge():
    return render_template("Dodge.html")

@app.route("/LED/ON")
def led_on():
    try:
        GPIO.output(8, GPIO.HIGH)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/Snake")
def snake():
    return render_template("Snake.html")
    
        
@app.route("/LED/OFF")
def led_off():
    try:
        GPIO.output(8, GPIO.LOW)
        return "ok"
    except expression as identifier:
        return "fail"
        
@app.route("/PWM/DODGE")
def pwm_dodge():
    try:
        pwm.start(50.0)
        for i in range(0,11):
            pwm.ChangeFrequency(scale[i])
            time.sleep(0.5)
        pwm.stop()
        return "ok"
    except expression as identifier:
        return "fail"
        
@app.route("/PWM/SNAKE")
def pwm_snake():
    try:
        pwm.start(50.0)
        for i in range(0,2):
            pwm.ChangeFrequency(snake_scale[i])
            time.sleep(0.3)
        pwm.stop()
        return "ok"
    except expression as identifier:
        return "fail"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
