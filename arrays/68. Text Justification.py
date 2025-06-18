from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        words_in_line = []        # Stores words that go in the current line
        wordLenNoSpace = 0        # Total length of characters in words_in_line (no spaces)

        for word in words:
            # Check if adding this word + minimum spaces would exceed the line
            if wordLenNoSpace + len(words_in_line) + len(word) > maxWidth:
                total_spaces = maxWidth - wordLenNoSpace
                number_of_gaps = len(words_in_line) - 1

                if number_of_gaps == 0:
                    # Only one word in the line → left-align with padding at the end
                    justified_line = words_in_line[0] + ' ' * total_spaces
                else:
                    # Evenly distribute spaces between words
                    space_per_gap, extra_spaces = divmod(total_spaces, number_of_gaps)
                    justified_line = ""

                    for i in range(number_of_gaps):
                        justified_line += words_in_line[i]
                        # Add extra space to the leftmost gaps first
                        spaces_to_add = space_per_gap + (1 if i < extra_spaces else 0)
                        justified_line += ' ' * spaces_to_add
                    justified_line += words_in_line[-1]  # Add the last word without extra space

                result.append(justified_line)

                # Start a new line with the current word
                words_in_line = [word]
                wordLenNoSpace = len(word)
            else:
                # Word fits → add it to the current line
                words_in_line.append(word)
                wordLenNoSpace += len(word)

        # Handle the last line (left-aligned)
        last_line = ' '.join(words_in_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result