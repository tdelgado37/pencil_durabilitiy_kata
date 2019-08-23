import constants

class Pencil:
    def __init__(self):
        self.letters_until_dull = constants.INITIAL_SHARPEN_VALUE
        self.eraser_status = constants.INITIAL_ERASER_VALUE
        self.erased_position = 0

    def write_on_paper(self,paper, text_to_write):
        str_to_write_on_paper = ''

        for character in text_to_write:
            not_dull_pencil = self.letters_until_dull > 0
            if not_dull_pencil:
                self._pencil_point_degradation_logic(character)
            else:
                character = ' '

            str_to_write_on_paper += character

        paper.text = str_to_write_on_paper


    def _pencil_point_degradation_logic(self, character):
        if not self._is_white_space(character):
            if character.isupper():
                self.letters_until_dull -=2
            else:
                self.letters_until_dull -=1

    def _is_white_space(self, character):
        return character in constants.WHITE_SPACE_LIST

    def sharpen(self):
        self.letters_until_dull = constants.INITIAL_SHARPEN_VALUE

    def erase(self, paper, erase_str):
        self.erased_position = 0

        new_text_on_paper = self._new_text_on_paper_erase_logic(paper.text.split(),erase_str)
        paper.text = new_text_on_paper


    def _new_text_on_paper_erase_logic(self, paper_text_list, erase_str):
        replacement_string = self._create_replacement_string(erase_str)
        str_has_been_erased = False
        new_text_on_paper = ''

        for word_on_paper in reversed(paper_text_list):

            new_text_on_paper_has_words = len(new_text_on_paper) > 0
            if new_text_on_paper_has_words:
                new_text_on_paper = ' ' + new_text_on_paper
                if not str_has_been_erased:
                    space_padding = -1
                    self._adjust_erased_position(space_padding)

            if not str_has_been_erased:
                word_on_paper_matches_erase_str = word_on_paper == erase_str
                if word_on_paper_matches_erase_str:
                    word_on_paper = replacement_string
                    str_has_been_erased = True
                else:
                    partially_erased_word = word_on_paper.replace(erase_str, replacement_string)
                    part_of_word_has_been_erased = partially_erased_word != word_on_paper

                    if part_of_word_has_been_erased:
                        word_on_paper = partially_erased_word
                        str_has_been_erased = True

            new_text_on_paper = word_on_paper + new_text_on_paper

            added_to_new_text_and_str_still_not_erased = not str_has_been_erased
            if added_to_new_text_and_str_still_not_erased:
                self._adjust_erased_position(-len(new_text_on_paper))

        self._adjust_erased_position(len(new_text_on_paper))
        return new_text_on_paper

    def _create_replacement_string(self, erase_str):
        replacement_string = ''
        for character in reversed(erase_str):
            eraser_still_works = self.eraser_status > 0
            if eraser_still_works:
                replacement_string = ' ' + replacement_string
                self.eraser_status -= 1
                self.erased_position -= 1
            else:
                replacement_string = character + replacement_string
        return replacement_string

    def _adjust_erased_position(self, integer):
        self.erased_position += integer

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
            white_space = self._is_white_space(editable_char)

            if white_space:
                editable_char = character
            else:
                editable_char = '@'
            new_text_on_paper += editable_char
        return new_text_on_paper


class Paper:
    text = ''
