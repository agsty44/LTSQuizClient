radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 3) {
        buzzed = 0
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.A, function () {
    if (buzzed == 0 && setup == 0) {
        radio.sendNumber(teamNumber)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        buzzed = 1
    }
})
let buzzed = 0
let setup = 0
let teamNumber = 0
radio.setGroup(1)
teamNumber = 0
setup = 1
while (true) {
    if (teamNumber == 0) {
        basic.showString("J")
    } else if (teamNumber == 1) {
        basic.showString("H")
    } else if (teamNumber == 2) {
        basic.showString("S")
    }
    if (input.buttonIsPressed(Button.A) && teamNumber < 2) {
        teamNumber += 1
        basic.clearScreen()
    } else if (input.buttonIsPressed(Button.A) && teamNumber == 2) {
        teamNumber = 0
        basic.clearScreen()
    } else if (input.buttonIsPressed(Button.B)) {
        basic.clearScreen()
        setup = 0
        break;
    }
}
basic.forever(function () {
	
})
