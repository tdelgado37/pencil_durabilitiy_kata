

class Pencil:
    text_to_write = ''

    #I picked 10 as an arbitrary number
    letters_until_dull = 10

    eraser_status = 10

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

    def erase(self, paper, erase_str):
        empty_string = ''
        str_has_been_erased = False
        new_text_on_paper = ''
        for character in reversed(erase_str):
            if self.eraser_status > 0:
                empty_string = ' ' + empty_string
                self.eraser_status -= 1
            else:
                empty_string = character + empty_string
        for word_on_paper in reversed(paper.text.split()):
            #adding a space before each word is added to new word
            #because we are going in reverse order
            if len(new_text_on_paper) > 0:
                new_text_on_paper = ' ' + new_text_on_paper
            if word_on_paper == erase_str and not str_has_been_erased:
                word_on_paper = empty_string
                str_has_been_erased = True
            elif not str_has_been_erased:
                partially_erased_word = word_on_paper.replace(erase_str, empty_string)
                if(partially_erased_word != word_on_paper):
                    word_on_paper = partially_erased_word
                    str_has_been_erased = True
            new_text_on_paper = word_on_paper + new_text_on_paper

        paper.text = new_text_on_paper



class Paper:
    text = ''
