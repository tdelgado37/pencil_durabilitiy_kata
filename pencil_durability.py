

class Pencil:
    text_to_write = ''

    def write_on_paper(self,paper):
        paper.text += self.text_to_write

    def set_text_to_write(self, str):
        self.text_to_write = str


class Paper:
    text = ''
