import os

class HelpFunctions:

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
        input("Press Enter to continue...")

    def text_helper(self, text):
        print(text)
        self.pause()
        self.clear_screen()

    def get_user_input(self, prompt, clear=False, input_type=None, valid_range=None):
        """
Gets user input and validates it based on the expected type, with optional range validation and type conversion.

Args:
    prompt (str): The message to display to the user.
    input_type (str): The expected type of input ('int', 'float', or None).
    valid_range (tuple, optional): A tuple (min, max) defining the valid input range.
    clear (bool, optional): Whether to clear the screen after input.
    convert_to_str (bool, optional): Whether to convert the input to a string before returning.

Returns:
    str: The validated user input as a string if convert_to_str is True.
    int/float: The validated input in its original type otherwise.
        """
        while True:
            user_input = input(prompt).strip()

            # Handle empty input
            if not user_input:
                if clear:
                    self.clear_screen()
                print("You did not enter anything. Please try again.")
                continue

            try:
                # Validate and convert input based on type
                if input_type in ['float', 'int']:
                    user_input = float(user_input) if input_type == 'float' else int(user_input)

                    # Validate range if provided
                    if valid_range:
                        min_val, max_val = valid_range
                        if not (min_val <= user_input <= max_val):
                            if clear:
                                self.clear_screen()
                            print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")
                            continue

                # Clear screen if specified
                if clear:
                    self.clear_screen()

                return user_input

            except ValueError:
                if clear:
                    self.clear_screen()
                input_type_desc = "an integer" if input_type == "int" else "a float" if input_type == "float" else "valid input"
                print(f"Invalid input. Please enter {input_type_desc}.")