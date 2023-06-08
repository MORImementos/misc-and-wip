import argparse

parser = argparse.ArgumentParser(description="DSRPG")
parser.add_argument("command", type=str, help="Enter a command")
args = parser.parse_args()
command = args.command.lower()

def analyze_command(command):
    if command == "dsrpg":
        print("Now using DSRPG tool.")

analyze_command(command)

while True:
    additional_command = input("Enter another prompt: ")
    analyze_command(additional_command)