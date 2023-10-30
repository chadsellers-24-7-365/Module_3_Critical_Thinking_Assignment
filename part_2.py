# START
#   DISPLAY "What is the current time (in hours, using a 24-hour clock)?"
#   INPUT current_time
#
#   WHILE current_time < 0 OR current_time > 23 DO
#     DISPLAY "Invalid input. Please enter a time between 0 and 23."
#     INPUT current_time
#   END WHILE
#
#   DISPLAY "How many hours do you want to wait for the alarm?"
#   INPUT hours_to_wait
#
#   SET alarm_time = (current_time + hours_to_wait) MOD 24
#
#   DISPLAY "The alarm will go off at " + alarm_time + " on a 24-hour clock."
# END
def main():
    # Get the current time from the user
    current_time = int(input("What is the current time (in hours, using a 24-hour clock)? "))

    # Validate the input for the current time
    while current_time < 0 or current_time > 23:
        print("Invalid input. Please enter a time between 0 and 23.")
        current_time = int(input("What is the current time (in hours, using a 24-hour clock)? "))

    # Get the number of hours to wait for the alarm
    hours_to_wait = int(input("How many hours do you want to wait for the alarm? "))

    # Calculate the alarm time
    alarm_time = (current_time + hours_to_wait) % 24

    # Output the result
    print(f"The alarm will go off at {alarm_time} on a 24-hour clock.")

if __name__ == "__main__":
    main()
                                                       