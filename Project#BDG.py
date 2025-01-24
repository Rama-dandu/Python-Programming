import threading
import random


def timer_action(duration):

    ## part 1
    # Randomly select a number from 0 to 9
    random_number = random.randint(0, 9)

    # Create a list of numbers from 0 to 9
    # numbers = list(range(10))

    # Shuffle the numbers randomly
    # random.shuffle(numbers)

    # Pick a random number from the shuffled list
    # random_number = numbers[0]  # Take the first number after shuffling

    # Determine the size ("small" or "big") based on the number
    if random_number in range(0, 5):  # Numbers from 0 to 4
        size = "small"
    else:  # Numbers from 5 to 9
        size = "big"

    # Determine the color based on the number
    if random_number == 0:
        # If the number is 0, pick both "red" and "violet"
        selected_colors = ["red", "violet"]
        print(
            f"Number: {random_number}, Big Small: {size}, Color: {', '.join(selected_colors)}")
    elif random_number in [2, 4, 6, 8]:
        # If the number is 2, 4, 6, or 8, pick "red"
        selected_color = "red"
        print(
            f"Number: {random_number}, Big Small: {size}, Color: {selected_color}")
    elif random_number in [1, 3, 7, 9]:
        # If the number is 1, 3, 7, or 9, pick "green"
        selected_color = "green"
        print(
            f"Number: {random_number}, Big Small: {size}, Color: {selected_color}")
    elif random_number == 5:
        # If the number is 5, pick both "green" and "violet"
        selected_colors = ["green", "violet"]
        print(
            f"Number: {random_number}, Big Small: {size}, Colors: {', '.join(selected_colors)}")


## main part of code
def run_continuous_timer(duration):
    print(f"Starting a timer that will always run for {duration} seconds...")

    while True:
        timer_event = threading.Event()

        def timer_action_with_event():
            timer_action(duration)
            timer_event.set()  # Signal that the timer is completed

        # Start the timer
        timer = threading.Timer(duration, timer_action_with_event)
        timer.start()

        # Wait for the timer to complete before starting again
        timer_event.wait()


# Main program
try:
    duration = int(input("Enter the duration in seconds (e.g., 30): "))
    if duration <= 0:
        print("Please enter a positive number.")
    else:
        run_continuous_timer(duration)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
