import serial
import sys
import optparse

p = optparse.OptionParser()
p.add_option('-p', '--port', metavar="PORT", help="Port for serial communications (/dev/ttyUSB0)", default="/dev/ttyUSB0")
p.add_option('-b', '--baudrate', metavar="BAUDRATE", help="Device baudrate (115200)", default=115200, type=int)
p.add_option('-t', '--timeout', metavar="TIMEOUT", help="Timeout (1)", default=1, type=int)
options, arguments = p.parse_args()

ser = serial.Serial(
    port=options.port,
    baudrate=options.baudrate,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=options.timeout
)

# Reference link for commands: https://www.rotel.com/sites/default/files/product/rs232/RA1592%20Protocol.pdf
rotel_commands = {
    # POWER & VOLUME COMMANDS
    "PowerOn": "power_on!",
    "PowerOff": "power_off!",
    "PowerToggle": "power_toggle!",
    "VolumeUp": "vol_up!",
    "VolumeDown": "vol_dwn!",
    "VolumeMin": "vol_min!",
    "MuteToggle": "mute!",
    "MuteOn": "mute_on!",
    "MuteOff": "mute_off!",

    # SOURCE SELECTION COMMANDS
    "SourceCD": "cd!",
    "SourceCoax1": "coax1!",
    "SourceCoax2": "coax2!",
    "SourceCoax3": "coax3!",
    "SourceOpt1": "opt1!",
    "SourceOpt2": "opt2!",
    "SourceOpt3": "opt3!",
    "SourceAux": "aux!",
    "SourceTuner": "tuner!",
    "SourcePhono": "phono!",
    "SourceUSB": "usb!",
    "SourceBT": "bluetooth!",
    "SourceXlr": "bal_xlr!",
    "SourcePcUsb": "pcusb!",

    # SOURCE CONTROL COMMANDS
    "Play": "play!",
    "Stop": "stop!",
    "Pause": "pause!",
    "TrackForward": "trkf!",
    "TrackBackward": "trkb!",

    # TONE CONTROL COMMANDS
    "ToneBypassOn": "bypass_on!",
    "ToneBypassOff": "bypass_off!",
    "BassUp": "bass_up!",
    "BassDown": "bass_down!",
    "BassDown10": "bass_-10!",
    "BassUp10": "bass_+10!",
    "Bass0": "bass_000!",
    "TrebleUp": "treble_up!",
    "TrebleDown": "treble_down!",
    "TrebleDown10": "treble_-10!",
    "TrebleUp10": "treble_+10!",
    "Treble0": "treble_000!",

    # BALANCE CONTROL COMMANDS
    "BalanceRight": "balance_r!",
    "BalanceLeft": "balance_l!",
    "BalanceMaxLeft": "balance_l15!",
    "Balance0": "balance_000!",
    "BalanceMaxRight": "balance_r15!",

    # SPEAKER OUTPUT COMMANDS
    "SpeakerAToggle": "speaker_a!",
    "SpeakerBToggle": "speaker_b!",
    "SpeakerAOn": "speaker_a_on!",
    "SpeakerAOff": "speaker_a_off!",
    "SpeakerBOn": "speaker_b_on!",
    "SpeakerBOff": "speaker_b_off!",

    # OTHER COMMANDS
    "Dimmer": "dimmer!",
    "Dimmer0": "dimmer_0!",
    "Dimmer1": "dimmer_1!",
    "Dimmer2": "dimmer_2!",
    "Dimmer3": "dimmer_3!",
    "Dimmer4": "dimmer_4!",
    "Dimmer5": "dimmer_5!",
    "Dimmer6": "dimmer_6!",
    "PcUsb1": "pcusb_class_1!",
    "PcUsb2": "pcusb_class_2!",

    # RS232 FEEDBACK COMMANDS
    "Rs232UpdateOn": "rs232_update_on!",
    "Rs232UpdateOff": "rs232_update_off!",
}


def send_cmd(cmd):
    global rotel_commands
    if cmd in rotel_commands:
        print("sending " + cmd)
        ser.write(rotel_commands[cmd].encode())
        return cmd
    else:
        return "Command not found."


send_cmd(sys.argv[1])

response = ser.readline()
print(response)
ser.close()
