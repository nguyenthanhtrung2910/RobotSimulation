class GetCommand:
    def __init__(self, file) -> None:
        self.file = file

    def set_сommands(self):
        with open(self.file, 'r') as f:
            text = f.read().split('\n')
        return text