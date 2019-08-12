

class Pencil:
    text_to_write = ''

    #I picked 10 as an arbitrary number
    letters_until_dull = 10

    _inital_sharpen_value = 10

    def write_on_paper(self,paper):
        str_to_write_on_paper = ''
        for character in self.text_to_write:
            if self.letters_until_dull > 0 and character != ' ' and character != '\n':
                if character.isupper():
                    self.letters_until_dull -=2
                else:
                    self.letters_until_dull -=1
            elif self.letters_until_dull <= 0 and character != ' ' and character != '\n':
                character = ' '

            str_to_write_on_paper += character

        paper.text = str_to_write_on_paper


    def set_text_to_write(self, str):
        self.text_to_write = str

    def sharpen(self):
        self.letters_until_dull = self._inital_sharpen_value


class Paper:
    text = ''
