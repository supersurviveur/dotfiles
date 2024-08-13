[
  "@at-root"
  "@debug"
  "@error"
  "@extend"
  "@forward"
  "@mixin"
  "@use"
  "@warn"
  "@media"
  "="
] @keyword

"@function" @keyword.function

"@return" @keyword.return

"@include" @keyword.import

[
  "@while"
  "@each"
  "@for"
  "from"
  "through"
  "in"
] @keyword.repeat

(js_comment) @comment @spell
(comment) @comment

(function_name) @function

[
  ">="
  "<="
] @operator

(mixin_statement
  name: (identifier) @function)

(mixin_statement
  (parameters
    (parameter) @variable.parameter))

(function_statement
  name: (identifier) @function)

(function_statement
  (parameters
    (parameter) @variable.parameter))

((plain_value) @variable.scss
   (#match? @variable.scss "^--.+"))

((property_name) @variable.scss
   (#match? @variable.scss "^--.+"))

((property_name) @variable.scss
   (#match? @variable.scss "^$.+"))

(plain_value) @type

(string_value) @string

(selectors
  (pseudo_element_selector
    (tag_name) @attribute.jsx))

(selectors
  (pseudo_class_selector
    (class_name) @attribute.jsx))


(nesting_selector) @keyword

(tag_name) @tag

(keyword_query) @function

(identifier) @variable.scss.ident

(variable) @variable.scss

(argument) @variable.parameter

(arguments
  (variable) @variable.parameter)

(integer_value) @constant.numeric.integer

(integer_value
  (unit) @keyword)

(class_name) @classname
(id_name) @idname

(attribute_name) @attribute.jsx

(class_selector
  "." @punctuation.italic)
(id_selector
  "#" @punctuation.italic)

(pseudo_class_selector
  ":" @punctuation.italic)
"::" @punctuation.italic

[
  "["
  "]"
] @punctuation.bracket

[
  "{"
  "}"
  ":"
  ";"
  "#{"
  ","
  "("
  ")"
] @punctuation


(include_statement
  (identifier) @function)
