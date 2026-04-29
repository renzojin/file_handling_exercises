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

            