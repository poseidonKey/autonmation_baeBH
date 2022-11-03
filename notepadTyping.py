import pywinmacro as pw
from datetime import datetime
import time

pw.key_on("window")
pw.key_press_once('r')
# pw.key_on("r")
# pw.key_off("r")
pw.key_off("window")
time.sleep(.5)
pw.typing('notepad')
pw.key_press_once("enter")
time.sleep(2)
pw.typing('hello!!')
time.sleep(1)
pw.key_on("control")
pw.key_press_once('s')
pw.key_off("control")
time.sleep(2)
pw.typing("aaa"+str(datetime.today())[-4:])
time.sleep(1)
pw.key_press_once('enter')
time.sleep(1)
pw.key_on("alt")
pw.key_press_once('f4')
pw.key_off("alt")

# loc = (3434, 175)
# print(loc)
# pw.click(loc)

# pw.typing('123451234512345123451234512345')
# time.sleep(1)
# for i in range(5):
#   pw.click(loc)  # .key_press_once('window')
#   time.sleep(2)
