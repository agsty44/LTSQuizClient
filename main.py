def on_received_number(receivedNumber):
    global buzzed
    if receivedNumber == 3:
        buzzed = 0
        basic.clear_screen()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global buzzed
    if buzzed == 0 and setup == 0:
        radio.send_number(teamNumber)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        buzzed = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

buzzed = 0
setup = 0
teamNumber = 0
radio.set_group(1)
teamNumber = 0
setup = 1
while True:
    if teamNumber == 0:
        basic.show_string("J")
    elif teamNumber == 1:
        basic.show_string("H")
    elif teamNumber == 2:
        basic.show_string("S")
    if input.button_is_pressed(Button.A) and teamNumber < 2:
        teamNumber += 1
        basic.clear_screen()
    elif input.button_is_pressed(Button.A) and teamNumber == 2:
        teamNumber = 0
        basic.clear_screen()
    elif input.button_is_pressed(Button.B):
        basic.clear_screen()
        setup = 0
        break

def on_forever():
    pass
basic.forever(on_forever)
