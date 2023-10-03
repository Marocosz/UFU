import graph

escala = 300

min = 20
max = 280

center1 = 150

color = (152, 90, 8)

delay = 0.001

radius = 20

thick = -1

scene = graph.create_scene(escala) #cria um frame vazio (black)

for altura in range(min, max):

    img = scene.copy() #copia o frame vazio

    graph.cv.circle(img, (center1, altura), radius, color, thick)

    #Gerencia imagem
    graph.cv.imshow('dark', img) #mostra
    graph.time.sleep(delay) #delay

    if graph.destroy_scene():
        break #se quit, esc


