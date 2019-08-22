

class Pencil:
    text_to_write = ''

    #I picked 10 as an arbitrary number
    letters_until_dull = 10

    eraser_status = 10

    _inital_sharpen_value = 10

    erased_position = 0

    def set_text_to_write(self, str):
        self.text_to_write = str

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



    def sharpen(self):
        self.letters_until_dull = self._inital_sharpen_value

    def erase(self, paper, erase_str):
        self.erased_position = 0

        new_text_on_paper = self._new_text_on_paper_erase_logic(paper.text.split(),erase_str)
        paper.text = new_text_on_paper

    def _create_replacement_string(self, erase_str):
        replacement_string = ''
        for character in reversed(erase_str):
            if self.eraser_status > 0:
                replacement_string = ' ' + replacement_string
                self.eraser_status -= 1
                self.erased_position -= 1
            else:
                replacement_string = character + replacement_string
        return replacement_string

    def _new_text_on_paper_erase_logic(self, paper_text_array, erase_str):
        replacement_string = self._create_replacement_string(erase_str)
        str_has_been_erased = False
        new_text_on_paper = ''

        for word_on_paper in reversed(paper_text_array):
            #adding a space before each word is added to new word
            #because we are going in reverse order
            if len(new_text_on_paper) > 0:
                new_text_on_paper = ' ' + new_text_on_paper
                if not str_has_been_erased:
                    self.erased_position -= 1
            if word_on_paper == erase_str and not str_has_been_erased:
                word_on_paper = replacement_string
                str_has_been_erased = True
            elif not str_has_been_erased:
                partially_erased_word = word_on_paper.replace(erase_str, replacement_string)
                if(partially_erased_word != word_on_paper):
                    word_on_paper = partially_erased_word
                    str_has_been_erased = True
            new_text_on_paper = word_on_paper + new_text_on_paper
            if not str_has_been_erased:
                self.erased_position -= len(new_text_on_paper)
        self.erased_position += len(new_text_on_paper)
        return new_text_on_paper

    def edit_text(self, paper, editing_text):

        str_before_edited_text = paper.text[0:self.erased_position]
        str_to_be_edited = paper.text[self.erased_position:]
        str_after_edited_text = paper.text[self.erased_position + len(editing_text):]

        new_text_on_paper = self._text_editing_override_logic(str_to_be_edited, editing_text)
        paper.text = str_before_edited_text + new_text_on_paper + str_after_edited_text


    def _text_editing_override_logic(self,str_to_be_edited, editing_text):
        new_text_on_paper = ''
        for index, character in enumerate(editing_text):
            editable_char  = str_to_be_edited[index]
            if editable_char.isspace():
                editable_char = character
            else:
                editable_char = '@'
            new_text_on_paper += editable_char
        return new_text_on_paper


class Paper:
    text = ''
