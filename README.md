# paste
This works like the paste function in bash.

The specifics of the function are that they take in rawtext written in the format 'text text text\nthis is a new line'. There are various options available that the user can control, such as being able to change the width of the margin and whether or not to include a header separator (and in regards to the header, there is an included header constructor). The function returns the processed text in raw string which can be then plugged into a print function, or just saved from there. The lightweight version just omits every non-vital function, and restricts the margin to 1 space.
