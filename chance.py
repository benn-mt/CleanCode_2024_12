class Chance:
    def __init__(self, likelihood):
        self._likelihood = likelihood

    # override == operator
    def __eq__(self, other):
        return True
