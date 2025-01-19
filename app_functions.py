from periodic_table_base import periodic_table_base as pta
from help_functions import HelpFunctions
import json
import os

class AppFunctions:
    
    def __init__(self):
        self.recent_searches = {}
        self.help_functions = HelpFunctions()
        self.load_from_json()
    
        
    def get_element_info(self, user_input, method):
        search_keys = {1: 'name', 2: 'symbol', 3: 'atomicNumber'}
        search_key = search_keys.get(method)

        # Check if already cached
        if (user_input, search_key) in self.recent_searches:
            return self.recent_searches[(user_input, search_key)]

        for element in pta:
            if str(element[search_key]).lower() == str(user_input).lower():
                # Cache the result
                self.recent_searches[(user_input, search_key)] = element
                self.save_json_file() 
                return element
        return None

    def get_element(self):
        text = """
How do you want to search for the element?
    1. Name    
    2. Symbol   
    3. Atomic number
Enter your choice (1-3): """
        while True:
            search_method = self.help_functions.get_user_input(text, True, 'int', (1, 3))
            search_prompts = {
                1: "Enter the name of an element: ",
                2: "Enter the symbol of an element: ",
                3: "Enter the atomic number of an element: "
            }

            while True:
                user_input = input(search_prompts[search_method]).strip()

                # Get element info
                element_data = self.get_element_info(user_input, search_method)

                if element_data:
                    self.help_functions.clear_screen()
                    self.print_element_info(element_data)
                    return
                else:
                    self.help_functions.clear_screen()
                    print("Element not found. Please try again.")

    def print_element_info(self, element_data):
        print(f"\n{'-'*40}")
        
        # Print each key-value pair in the element_data dictionary
        max_key_length = max(len(k) for k in element_data.keys())
        for key, value in element_data.items():
            if isinstance(value, dict):
                print(f"{key.capitalize():<{max_key_length}}:")
                for sub_key, sub_value in value.items():
                    print(f"  {sub_key.capitalize():<{max_key_length}}: {sub_value or 'N/A'}")
            else:
                print(f"{key.capitalize():<{max_key_length}}: {value or 'N/A'}")
        
        print(f"{'-'*40}")
        input("Press anything to continue...")
        self.help_functions.clear_screen()

    def show_recent_searches(self):
        if not self.recent_searches:
            print("No recent searches found.")
            return

        print("\nRecent Searches:")
        print(f"{'-'*40}")
        search_list = list(self.recent_searches.items())  # Convert to a list for indexing
        for idx, ((user_input, search_key), element) in enumerate(search_list, start=1):
            print(f"{idx}| Search: {user_input} ({search_key}) -> Element: {element['name']}")
        print(f"{'-'*40}")
        
        # Get the user's choice
        user_input = self.help_functions.get_user_input("Which element do you want to check (enter number): ", True, "int", (1, len(search_list)))
        selected_element = search_list[user_input - 1][1]  # Get the element data
        self.print_element_info(selected_element)

    def clear_recent_searches(self):
        if not self.recent_searches:
            print("There is nothing to clear.")
            return
        self.recent_searches = {}
        print("Cleared search history successfully")
        self.save_json_file()



    def save_json_file(self, filename="data.json"):
        try:
            json_compatible_data = {
                f"{key[0]}|{key[1]}": value
                for key, value in self.recent_searches.items()
            }
            with open(filename, "w") as file:
                json.dump(json_compatible_data, file, indent=2)
        except Exception as e:
            print(f"An error occurred while saving: {e}")

    def load_from_json(self, filename="data.json"):
        try:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    data = json.load(file)
                    # Convert string keys back to tuples
                    self.recent_searches = {
                        tuple(key.split("|")): value
                        for key, value in data.items()
                    }
            else:
                self.recent_searches = {}
        except (json.JSONDecodeError, OSError) as e:
            print(f"An error occurred while loading: {e}")
            self.recent_searches = {}