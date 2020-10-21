```
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
```

1. Match phone number: 
   + \d\d\d.\d\d\d.\d\d\d\d
2. Chracter Set: 
   + \d\d\d[.-]\d\d\d[.-]\d\d\d\d
   + [98]00[.-]\d\d\d[.-]\d\d\d\d
3. Match single char in range: 
   + [a-z1-7]
4. Match char not in the set: 
   + [^a-z]
5. Quantifiers:   
   + \d{3}.\d{3}.\d{4}   
   + Mr\.?\s[A-Z]\w*
6. Group:
   + M(r|s|rs)\.?\s[A-Z]\w*
7. More example-urls: 
   + https?://(www\.)?(\w+)(\.\w+)
   + Get domain name: 
    ```nhom2 : $2``` ($0 is the whole url)
