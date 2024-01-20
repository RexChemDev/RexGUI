import PySimpleGUI as sg
from os.path import getsize, splitext
from sheet_importer import pullexcel
from network import ot_send
import traceback

sg.theme("dark grey 8")

valid_ext = [".xls", ".xlsx"]

layout = [
    [sg.Text("Choose a protocol."), sg.Combo(["Dilution"], key="protocol_input"), sg.Input("Select a spreadsheet.", key="filename", enable_events=True), sg.FileBrowse(target="filename")],
    [sg.Text("Command Preview")],
    [sg.Output(size=(100, 5), key="sheet_output")],
    [sg.Text("Robot address:"), sg.Input("0.0.0.0", key="ip_input")],
    [sg.Button("Send commands to robot", key="net_send", disabled=True)],
    [sg.Text("", key="retcode")]
]

window = sg.Window("RexChem Protocol Sender", layout, size=(800, 500))

while True:
    try:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Close":
            break
        if event == "filename":
            filename = values["filename"]
            _, ext = splitext(filename)
            if not ext in valid_ext:
                window["sheet_output"].update(f"Files of type '{ext}' are not supported.\nPlease enter a spreadsheet file.")
                window["net_send"].update(disabled=True)
                continue

            commands = pullexcel(filename)
            commands.append("STOP")
            window["sheet_output"].update(commands)
            window["net_send"].update(disabled=False)
        if event == "net_send":
            retcode = ot_send(commands, values["ip_input"], 65432)
            window["retcode"].update(str(retcode))
    except OSError:
        window["retcode"].update(f"Could not reach {values["ip_input"]}.\nMachine may not be listening or address is invalid.")
    except ConnectionRefusedError:
        window["retcode"].update(f"Target machine {values["ip_input"]} refused connection.")
    except Exception as e:
        tb = traceback.format_exc()
        sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)

window.close()
