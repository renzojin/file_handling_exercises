class NumberProcessor:
    """A class to process numbers from a file and separate even and odd numbers"""

    def __init__(self, input_filename, even_filename, odd_filename):
        """
        Initialize the NumberProcessor with file names

        Args:
            input_filename (str): Name if the input file containing numbers
            even_filename (str): Name if the input file containing even
            odd_filename (str): Name if the input file containing odd
        """
        self.input_filename = input_filename
        self.even_filename = even_filename
        self.odd_filename = odd_filename
        self.numbers = []

    def read_numbers(self):
        """
        Read integers from the input file

        Returns:
            bool: True if numbers were read, False otherwise
        """
        try:
            with open(self.input_filename, 'r') as file:
                for line in file:
                    # Split line by whitespace and convert to integers
                    numbers_in_line = line.strip().split()
                    for num_str in numbers_in_line:
                        try:
                            self.numbers.append(int(num_str))
                        except ValueError:
                            print(f"Warning: '{num_str}' is not a valid integer, skipping...")

            if len(self.numbers) != 20:
                print(f"Warning: Expected 20 numbers but found {len(self.numbers)}")

            return True

        except FileNotFoundError:
            print(f"Error: {self.input_filename} not found")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def separate_numbers(self):
        """
        Separate numbers into even and odd lists

        Returns:
            tuple: (even_numbers, odd_numbers)
        """
        even_numbers = [num for num in self.numbers if num % 2 == 0]
        odd_numbers = [num for num in self.numbers if num % 2 != 0]

        return even_numbers, odd_numbers

    def write_numbers_to_files(self, even_numbers, odd_numbers):
        """
        Write even and odd numbers to their respective files

        Args:
            even_numbers (list): List of even numbers
            odd_numbers (list): List of odd numbers
        """
        try:
            with open(self.even_filename, 'w') as even_file:
                for num in even_numbers:
                    even_file.write(f"{num}\n")

            with open(self.odd_filename, 'w') as odd_file:
                for num in odd_numbers:
                    odd_file.write(f"{num}\n")

            print(f"Successfully wrote {len(even_numbers)} even numbers to {self.even_filename}")
            print(f"Successfully wrote {len(odd_numbers)} odd numbers to {self.odd_filename}")

        except Exception as e:
            print(f"Error: {e}")

        def process(self):
            """
                    Main processing method that orchestrates the entire operation

                    Returns:
                        bool: True if successful, False otherwise
                    """
            if not self.read_numbers():
                return False

            even_numbers, odd_numbers = self.separate_numbers()
            self.write_numbers_to_files(even_numbers, odd_numbers)

            print(f"\nSummary:")
            print(f"Total numbers read: {len(self.numbers)}")
            print(f"Even numbers: {len(even_numbers)}")
            print(f"Odd numbers: {len(odd_numbers)}")

            return True

        if __name__ == "__main__":
            processor = NumberProcessor("numbers.txt", "even.txt", "odd.txt")

            processor.process()