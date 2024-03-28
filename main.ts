input.onButtonPressed(Button.B, function on_button_pressed_b() {
    robot.motorRun(0, 100)
    basic.pause(5000)
    robot.motorStop()
})
robot.yahboomTinyBit.start()
loops.everyInterval(500, function on_every_interval() {
    robot.setColor(0xff0000)
    robot.playTone(262, music.beat(BeatFraction.Half))
    basic.pause(100)
    robot.playTone(330, music.beat(BeatFraction.Half))
    robot.setColor(0x0000ff)
    basic.pause(100)
})
