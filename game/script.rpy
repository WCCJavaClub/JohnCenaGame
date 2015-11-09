
define e = Character('Eileen', color="#c8ffc8")

image john manly = "somethingElse.png"
define john = Character("John Cena", color="#fff000")
image bg coolName = "birthday.jpeg"

label start:
    
    scene birthday
    pause (3)
    show john manly
    play music "renameIt.mp3"
    john "its Johnnnn cenaaaaa"

    return
