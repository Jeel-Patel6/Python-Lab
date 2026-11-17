import json

def display():
    try:
        with open("logs.json", "r") as file:
            data = json.load(file)

            print("\n--- All Log Records ---")

            for log in data:
                print("Timestamp:", log["Timestamp"])
                print("Log Level:", log["Log Level"])
                print("Message:", log["Message"])
                print("----------------------")

            analyze(data)

    except FileNotFoundError:
        print("Error: logs.json file not found.")

    except json.JSONDecodeError:
        print("Error: Invalid JSON data.")


def analyze(data):
    info = 0
    warning = 0
    error = 0

    for log in data:
        if log["Log Level"] == "INFO":
            info += 1

        elif log["Log Level"] == "WARNING":
            warning += 1

        elif log["Log Level"] == "ERROR":
            error += 1

    print("\n--- Log Summary ---")
    print("Total INFO messages:", info)
    print("Total WARNING messages:", warning)
    print("Total ERROR messages:", error)


# Main Program
display()