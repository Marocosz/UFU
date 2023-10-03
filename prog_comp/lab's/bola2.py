import graph1 as graph

escala = 600

center1 = 300
color = (2, 100, 8)
radius = 200
thick = -1

min = radius
max = escala - radius

delay = 0.00001

scene = graph.create_scene(escala) #cria um frame vazio (black)

cond = 0

while cond == 0:
    if cond == 0:
        color = (0, 123, 2)
        for altura in range(min, max):

            img = scene.copy() #copia o frame vazio

            graph.cv.circle(img, (center1, altura), radius, color, thick)

            #Gerencia imagem
            graph.cv.imshow('dark', img) #mostra
            graph.time.sleep(delay) #delay
            if graph.destroy_scene():
                cond = 1
                break #se quit, esc

    if cond == 0:
        color = (12, 0, 123)
        for altura in range(max, min, -1):

            img = scene.copy()  # copia o frame vazio

            graph.cv.circle(img, (center1, altura), radius, color, thick)

            # Gerencia imagem
            graph.cv.imshow('dark', img)  # mostra
            graph.time.sleep(delay)  # delay
            if graph.destroy_scene():
                cond = 1
                break  # se quit, esc
