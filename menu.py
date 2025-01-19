from help_functions import HelpFunctions
from app_functions import AppFunctions

class Menu:
    def __init__(self):
        self.help_functions = HelpFunctions()
        self.app_functions = AppFunctions()

    def start_menu(self):
        """Displays the main menu and handles user choice."""
        menu_text = """
Welcome to the periodic table!
1. Start
2. Recent search
3. Help
4. Quit
Enter your choice (1-4): """
        choice = self.help_functions.get_user_input(menu_text, True, 'int', (1, 4))
        
        if choice == 1:
            self.app_functions.get_element()
            self.end_menu()
        elif choice == 2:
            self.recent_search_menu()
        elif choice == 3:
            self.show_help()
        elif choice == 4:
            self.quit_app()

    def recent_search_menu(self):
        """Handles the recent search submenu."""
        while True:
            recent_search_text = """
    Recent Searches:
    1. View recent searches
    2. Clear recent searches
    3. Back to main menu
    Enter your choice (1-3): """
            choice = self.help_functions.get_user_input(recent_search_text, True, 'int', (1, 3))
            
            if choice == 1:
                self.app_functions.show_recent_searches()
            elif choice == 2:
                self.app_functions.clear_recent_searches()
            elif choice == 3:
                self.start_menu()

    def show_help(self):
        """Displays the help information."""
        help_text = """
Help Section:
- Search for elements by name or symbol.
- View properties like atomic number, mass, and category.
Examples:
  - Name search: 'Oxygen'
  - Symbol search: 'O'
Returning to the main menu...
"""
        self.help_functions.text_helper(help_text)

    def end_menu(self):
        """Displays options after an element search."""
        end_text = """
Would you like to:
1. Search for another element
2. Quit
Enter your choice (1 or 2): """
        choice = self.help_functions.get_user_input(end_text, True, 'int', (1, 2))
        
        if choice == 1:
            self.start_menu()
        elif choice == 2:
            self.quit_app()

    def quit_app(self):
        """Exits the application."""
        self.help_functions.clear_screen()
        print("Thank you for using the periodic table app. Goodbye!")
        quit()