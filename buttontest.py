import RPi.GPIO as GPIO
import time
import signal
import sys

# Ctrl+CによってSIGINTシグナルが送信された時のハンドラ。終了前にGPIO.cleanupを呼び出す
def handler(signum, frame):
  print ('Signal handler called with signal', signum)
  GPIO.cleanup()
  sys.exit(0)

# ハンドラの登録
signal.signal(signal.SIGINT, handler)

# GPIO9を入力として利用
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
before = 0
count = 0

# 無限ループ
while True:
  # 押された場合には1、押されていない場合0を返す
  now = GPIO.input(18)
  if before == 0 and now == 1:
    print("Push!!!")
    count += 1
    if count%2 == 0:
        GPIO.output(17, 1)
    else:
        GPIO.output(17, 0)
  time.sleep(0.1)
  before = now
