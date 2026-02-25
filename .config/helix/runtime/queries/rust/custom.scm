; -----
; custom highlights
; -----
(string_literal "\"" @string.delimiter)
(string_literal (string_content) @string)

(lifetime
  "'" @string.delimiter)

(lifetime
  (identifier) @type)

(self) @variable.builtin.self

[
  "::"
  "."
  ":"
] @punctuation.delimiter.rust
