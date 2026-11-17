try:
    
    file = open("log.txt", "r")

    error_count = 0

    print("Contents of the Log File:\n")

    for line in file:
        print(line.strip())

        if "ERROR" in line:
            error_count += 1

    print("\nTotal number of ERROR messages:", error_count)

    file.close()

except FileNotFoundError:
    print("Error: The file log.txt does not exist.")