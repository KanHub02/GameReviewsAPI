favorite_genre = (
    ("Sandbox", "Sandbox"),
    ("RTS", "RTS)"),
    ("FPS", "FPS"),
    ("MOBA", "MOBA"),
    ("RPG", "RPG"),
    ("MMORPG", "MMORPG"),
    ("MMOFPS", "MMOFPS"),
    ("Simulator", "Simulator"),
    ("Battle_royale", "Battle_royale"),
    ("Survival", "Survival"),
    ("Horror", "Horror"),
    ("Puzzles", "Puzzles"),
    ("Platformer", "Platformer"),
    ("Adventure", "Adventure"),
    ("Sport", "Sport"),
)

from django.core.validators import RegexValidator

telegram_validator = RegexValidator(
    regex=r"^@[a-zA-Z0-9]+$", message="The telegram username was '@XXXXXXXX'"
)


status_choices = (
    ("Sleeping", "Sleeping"),
    ("Playing", "Playing"),
    ("Working", "Working"),
    ("Studing", "Studing"),
    ("Bored", "Bored"),
)
