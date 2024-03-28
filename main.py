def on_button_pressed_b():
    robot.motor_run(0, 100)
    basic.pause(5000)
    robot.motor_stop()
input.on_button_pressed(Button.B, on_button_pressed_b)

robot.yahboom_tiny_bit.start()

def on_every_interval():
    robot.set_color(0xff0000)
    robot.play_tone(262, music.beat(BeatFraction.HALF))
    basic.pause(100)
    robot.play_tone(330, music.beat(BeatFraction.HALF))
    robot.set_color(0x0000ff)
    basic.pause(100)
loops.every_interval(500, on_every_interval)
