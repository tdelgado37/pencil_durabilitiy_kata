

class Pencil:
    text_to_write = input("Please enter a string: ")

    def write_on_paper(self,paper):
        paper.text += self.text_to_write



class Paper:
    text = ''
