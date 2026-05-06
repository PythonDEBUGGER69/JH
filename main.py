def on_gesture_shake():
    bitbot.go(BBDirection.FORWARD, 100)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    bitbot.led_brightness(255)
    bitbot.led_rainbow(True, BBArms.BOTH)
    bitbot.goms(BBDirection.FORWARD, 60, 1800)
    basic.pause(100)
    bitbot.rotatems(BBRobotDirection.RIGHT, 60, 20000)
input.on_button_pressed(Button.B, on_button_pressed_b)
