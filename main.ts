basic.forever(function () {
    if (input.temperature() > 37.5) {
        music.playTone(880, music.beat(BeatFraction.Double))
    }
})
basic.forever(function () {
    led.plotBarGraph(
    input.temperature(),
    50
    )
    basic.pause(100)
})
