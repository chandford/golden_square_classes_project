class GrammarStats:
    def __init__(self):
        self.pass_count = 0
        self.fail_count = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise

        ending_punctuation = ".?!"
        if text[0].isupper() and text[-1] in ending_punctuation:
            self.pass_count += 1
            return True
        
        else:
            self.fail_count += 1
            return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        total_count = self.pass_count+self.fail_count
        if total_count == 0:
            return 0
        else:
            pass_percentage = int((self.pass_count / total_count) * 100)
        return pass_percentage

