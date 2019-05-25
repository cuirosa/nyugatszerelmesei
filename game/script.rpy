define s = Character('Hola', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")
label start:
    $v = 42
    scene bg meadow
    with fade

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    "hey [v]"

    m "Hey... Umm..."

    show sylvie green smile
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    menu:

        "DRINK":
            $ renpy.notify('Cheat mode enabled')
            "I drank."

        "EAT":
            
            "I ate."

    jump check

    label .check:

        m "MWHAHAHA"
