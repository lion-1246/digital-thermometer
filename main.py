def on_forever():
    if input.temperature() > 37.5:
        music.play_tone(880, music.beat(BeatFraction.DOUBLE))
basic.forever(on_forever)

def on_forever2():
    led.plot_bar_graph(input.temperature(), 50)
    basic.pause(100)
basic.forever(on_forever2)
