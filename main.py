def on_sound_loud():
    global item
    item += 1
    basic.show_number(item)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

Duty = 0
item = 0
item = 0

def on_forever():
    global Duty
    if item >= 10:
        while Duty < 1023:
            pins.digital_write_pin(DigitalPin.P0, Duty)
            Duty = Duty + 1
            basic.pause(10)
basic.forever(on_forever)
