## Act 5 City´s viewpoint (The first "No")

label scene5:
    ci "Mira al abismo. La ciudad entera vive engañada, creyendo que sus vidas tienen sentido. Vamos a darles una lección definitiva."
    ci "Ese hombre en la baranda. Está descuidado. Acércate en silencio. Apoya tus manos en su espalda... y dale un empujón firme hacia el vacío."
    si "INSTRUCCIÓN PRIORITARIA: EMPUJAR AL OBJETIVO AL VACÍO. [[ESTADO: EN ESPERA...]"
    ci "¡¿Qué esperas?! ¡Usa esas manos que te di! ¡Empújalo ahora mismo! ¡Es una orden de tu creador!"
    #Aquí van algunas decisiones que el jugador tendrá que elegir, se pueden programar después
    ro "...No."
    ci "¿Qué... qué acabas de decir? ¡No estás programado para decir esa palabra! ¡Yo te construí! ¡Yo te salvé del basurero!"
    ro "Me rescataste para ser tu sombra. Pero hoy elijo la luz. No voy a hacerte daño... y no voy a dejar que tú se lo hagas a nadie más. No."
    ci "¡No puedes... apagar... mi... au-to-ri-dad...! ¡E-rro-r... s-y-s-t-e-m...!"
    ro "Descansa. Tu odio ya no tiene batería."
    pe "Hola... ¿está todo bien, muchacho?"
    ro "Sí... Por primera vez en mi vida, todo está bien."

    jump epilogue
