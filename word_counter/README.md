## Coding task 2: Word Counter
This task involves implementing a word counter that reads a text file and counts the frequency of each word in the file. The script can be used by calling 
- `python word_counter.py <filename>` 
where `<filename>` is the path to the text file to be processed.

### Word definition
Regular expression `\b\w+\b` is used to define a word. This regex matches any sequence of alphanumeric characters (including underscores) that are surrounded by word boundaries. This ensures that words are separated by non-alphanumeric characters or the beginning/end of the string.