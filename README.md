# pytextgenscript
Pytextgenscript - small interpreter for TextGen Script language.

Made by Ekaterina Ambartsumova and Vladislav Janvarev.

Require sexpdata library
```pip install sexpdata```

# Example usage
```
import pytextgenscript as ptgs
result = ptgs.run_s('("a" (#r "b" "c") "d")')
```

# Rules for TextGen Script

Elements are
* Text elements - renders "as is"
* Control atom - renders, and render subelements
* List - render and adds subelements

Examples:
* ("a" "b" "c") will be rendered to "abc"
* ("a" (("b") "c")) will be rendered to "abc", too

Control elements:
* #r - render random element of list. Example: ("a" (#r "b" "c")) will be rendered to "ab" or "ac" (randomly)
* #varSet - set var. Example: (#varSet "hero" "elf"). Or: (#varSet "hero" (#r "elf" "dwarf"))
* @\<var\> - render var. Example: ("The greatest hero, the " @hero " will come!")
* #ifVarEq - check var for equality. Example: (#ifVarEq "hero" "elf" ("Elf from forest moves silently..") ("Somebody UNKNOWN comes..."))

Live example (JS) here: http://d.janvarev.ru/sexp/textgenscript-html/

Russian version with a LOT of generators: http://janvarev.ru/TGen

TypeScript/JavaScript version: https://github.com/janvarev/sexp-textgenscript-tsjs