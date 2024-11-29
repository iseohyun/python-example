### 특별한 문자 '/'와 '*' ###
"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      --┬--------    -┬--------     -----┬----
        |             |                  |
        |        Positional or keyword   |
        |                                └- Keyword only
        └-- Positional only
"""


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg("STD_ARG")

pos_only_arg("POS_ONLY_ARG")

kwd_only_arg(arg="KW_ONLY_ARG")

combined_example("POS_ONLY_ARG", standard="STD_ARG", kwd_only="KW_ONLY_ARG")
combined_example("POS_ONLY_ARG", "STD_ARG", kwd_only="KW_ONLY_ARG")
