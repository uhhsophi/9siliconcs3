# Creates a class named Publication
class Publication:
    # Private attributes using double underscores
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    # Getters and Setters
    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_author(self) -> str:
        return self.__author

    def set_author(self, author: str):
        self.__author = author

    # Display title and author
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


# Book class inheriting from Publication
class Book(Publication):
    def __init__(self, title: str, author: str, number_of_pages: int):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages

    # Getter returns a formatted string to match sample output
    def get_number_of_pages(self) -> str:
        return f"Number of pages: {self.__number_of_pages}"

    # Setter with positive number validation
    def set_number_of_pages(self, number_of_pages: int):
        if number_of_pages <= 0:
            print("Number of pages must be positive.")
        else:
            self.__number_of_pages = number_of_pages


# Magazine class inheriting from Publication
class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = issue_number

    # Getter returns a formatted string to match sample output
    def get_issue_number(self) -> str:
        return f"Issue number: {self.__issue_number}"

    # Setter with positive number validation
    def set_issue_number(self, issue_number: int):
        if issue_number <= 0:
            print("Issue number must be positive.")
        else:
            self.__issue_number = issue_number


# Main program execution
if __name__ == "__main__":
    # Create objects
    pub1 = Publication("Journal of Experimental Psychology", "Ratcliff, R. & Van Dongen, H.")
    book1 = Book("Notes from Underground", "Fyodor Dostoevsky", 176)
    mag1 = Magazine("National Geographic", "Various Authors", 202)

    # Output Publication info
    print("Publication Information:")
    pub1.display_info()

    # Output Book info with validation
    print("\nBook Information:")
    book1.set_number_of_pages(-310)  # Invalid input test
    book1.display_info()
    print(book1.get_number_of_pages())

    # Output Magazine info
    print("\nMagazine Information:")
    mag1.display_info()
    print(mag1.get_issue_number())
