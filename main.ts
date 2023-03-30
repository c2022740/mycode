input.onSound(DetectedSound.Loud, function () {
    item += 1
    basic.showNumber(item)
})
let Duty = 0
let item = 0
item = 0
basic.forever(function () {
    if (item >= 10) {
        while (Duty < 1023) {
            pins.digitalWritePin(DigitalPin.P0, Duty)
            Duty = Duty + 1
            basic.pause(10)
        }
    }
})
