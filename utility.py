class check:
    @staticmethod
    def check_card(n, min, max):

        if n.isdigit():
            n = int(n)
            if n >= min and n <= max:
                return True
            else:
                return False

        else:
            print("Enter number only!")
            return False




