#Defining characters

define ro = Character("Robotito")
define ci = Character("Científico")
define si = Character("Sistema")
define ni = Character("Niño")
define an = Character("Anciana")
define pe = Character("Transeúnte")

# The game starts here.

label start:
    jump scene1

    return

    ## Si quieres que el texto se detenga a la mitad y siga después del clic, usa las etiquetas de texto:
    ## {w}: pausa y espera un clic, luego continúa en la misma caja de texto.
    ## {p}: salta a un párrafo nuevo, esperando clic.
    ##{w=1.0}: pausa de 1 segundo y sigue solo, sin clic.
    ##{nw}: pasa a lo siguiente automáticamente, sin esperar clic.
    ## Para esperar un rato sin diálogo (por ejemplo, antes de mostrar una imagen), usa pause:
    ##     scene bg cuarto
    ## with dissolve
    ## pause 1.5
    ## a "Bienvenida."