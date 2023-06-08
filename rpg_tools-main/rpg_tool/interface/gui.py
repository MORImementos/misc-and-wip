import PySimpleGUI as sg

# sg.Window(title="DSRPG", layout=[[]], margins=(200,100)).read()

layout = [[sg.Text("Dimension Splash RPG")], [sg.Button("End")]]

# make window
window = sg.Window("Test", layout)

# event loop
while True:
    event, values = window.read()
    # end program if presses end button or closes window
    if event == "End" or event == sg.WIN_CLOSED:
        break

window.close()