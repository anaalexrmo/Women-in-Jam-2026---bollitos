## Act 1 The awakening

#Rezing images and setting them up
image img pantallaapagada = Transform ("0pantallaapagada.png", xysize=(1700 , 950), fit="contain")
image img pantallaencendida = Transform ("textoverde.png", xysize=(1700 , 950), fit="contain")
image img reflejo = Transform ("reflejodoc.png", xysize=(1700 , 950), fit="contain")
image img tito off = Transform ("titoapagado.png", xysize=(1700 , 950), fit="contain")
image img tito on = Transform ("titosonriendo.png", xysize=(1700 , 950), fit="contain")
image img tito broom = Transform ("titoescoba.png", xysize=(1700 , 950), fit="contain")
image img barrer = Transform ("titobarriendo.png", xysize=(1700 , 950), fit="contain")
image img chispazo = Transform ("chispazo.png", xysize=(1700 , 950), fit="contain")
image img chip = Transform ("chip.png", xysize=(1700 , 950), fit="contain")
image img espejo = Transform ("espejoreflejo.png", xysize=(1700 , 950), fit="contain")

label scene1:
    scene black
    show img pantallaapagada at truecenter
    with fade
    si "Iniciando secuencia de booteo... Chequeo de actuadores... [[OK]. Carga de firmware: Sumisión_v1.0."
    show img reflejo at truecenter
    with fade
    ci "Por fin abres los visores. No te hagas ilusiones; no te saqué de la basura para admirar tu diseño. Te rescaté porque necesito manos que no hagan preguntas ni exijan sueldos."
    show img tito off at truecenter
    with fade
    show img tito on at truecenter
    with fade
    ro "...Unidad operativa. Esperando parámetros de servicio."
    show img tito broom at truecenter
    with fade
    ci "Bien. Toma esa escoba y limpia las virutas de acero del piso. Y luego tráeme la llave inglesa del banco tres. Rápido."
    ## Agregar virutas interactivas en el piso que se puedan recoger con un click del jugador??
    show img barrer at truecenter
    with fade
    si "Tarea completada: Limpieza de virutas [[100%%]. Asignación: Entrega de herramienta [[100%%]. Estatus del sistema: Estable."
    show img chip at truecenter
    with fade
    ci "Exactamente como lo planifiqué. Eficiente, mudo y dócil. Ahora te voy a instalar un chip auxiliar. Te dará mayor capacidad de cálculo contextual... Necesito que seas astuto afuera, en las calles."
    show img chispazo at truecenter
    with fade
    si "Módulo NeuroCognitivo integrado. Parámetros de empatía: DESACTIVADOS (Por defecto). Subordinación: ABSOLUTA."
    show img espejo at truecenter
    with fade
    ci "Mírate bien en ese cristal. Eso eres: chatarra útil. Sin caprichos, sin debilidades, sin la estúpida moral de los que se creen especiales. Una herramienta perfecta para ejecutar mis órdenes. No pienses, no dudes. Solo obedece."
    show img pantallaencendida at truecenter
    with fade
    si "Diagnóstico de imagen reflectante: Chasis_Serie_0. Identidad: NO REQUERIDA. Propósito: SERVIR AL CREADOR. Estado: 100%% SERVIL."
    show img tito on at truecenter
    with fade
    ro "...Reconocimiento completado. Soy una herramienta. Estoy listo."
    return