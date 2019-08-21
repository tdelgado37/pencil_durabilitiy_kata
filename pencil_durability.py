

class Pencil:
    text_to_write = ''

    #I picked 10 as an arbitrary number
    letters_until_dull = 10

    eraser_status = 10

    _inital_sharpen_value = 10

    erased_position = 0

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
        self.erased_position = 0
        replacement_string = ''
        str_has_been_erased = False
        new_text_on_paper = ''
        eraser_position_padding =0
        #run a check to see how long the erase_str is
        #if >1 then normal,
        #elif eraser_status > 1 , set e pos =0 and make sure replacement_string
        #   is just a space
        #have to consider how to manager replacement_string
        #this sets index inside of word
        #change to replacement_string creation method

        if(len(erase_str)> 1):
            for character in reversed(erase_str):
                if self.eraser_status > 0:
                    replacement_string = ' ' + replacement_string
                    self.eraser_status -= 1
                    self.erased_position -= 1
                else:
                    replacement_string = character + replacement_string
            for word_on_paper in reversed(paper.text.split()):
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
        else:
            for word_on_paper in reversed(paper.text.split()):
                new_text_on_paper = self._single_character_erase_logic(word_on_paper, erase_str) + new_text_on_paper


        paper.text = new_text_on_paper

    def _single_character_erase_logic(self, word, e_str):
        replace_string = ''
        for index, character in enumerate(reversed(word), start = 1):
            if character == e_str:
                self.erased_position = len(word) - index
                character = ' '
            replace_string = character + replace_string
        return replace_string

    def edit_text(self, paper, editing_text):
        str_before_edited_text = paper.text[0:self.erased_position]
        str_after_edited_text = paper.text[self.erased_position + len(editing_text):]
        paper.text = str_before_edited_text + editing_text + str_after_edited_text





class Paper:
    text = ''
