import graph1
import math

# Tarefa 1: Crie o planetas1.py parametrizando os dados abaixo.
# Parametrize: raio do sol, posição do sol, distância da Terra do sol, incremento em radianos

# Tarefa2: acrescente Marte e Vênus

# Tarefa3: Acrescente a lua da Terra

dimensao = 500

pos1_sol = int(dimensao/2)
pos_sol = (int(dimensao/2), int(dimensao/2))
tam_sol = int(dimensao/10)
cor_sol = (74, 246, 249)
thick = -1

cor_venus = (0, 45, 120)
tam_venus = int(tam_sol/4.8)

cor_terra = (152, 90, 8)
tam_terra = int(tam_sol/5)

cor_marte = (39, 40, 127)
tam_marte = int(tam_sol/4)

cor_lua = (255, 255, 255)
tam_lua = int(tam_terra/3)

scene = graph1.create_scene(dimensao)

radv = 0
radt = 0
radm = 0
radl = 0

while True:
    img = scene.copy()

    # Sol
    graph1.cv.circle(img, pos_sol, tam_sol, cor_sol, thick)

    # Venus
    t = int(pos1_sol + (pos1_sol - pos1_sol * 0.6) * math.cos(radv))
    r = int(pos1_sol + (pos1_sol - pos1_sol * 0.6) * math.sin(radv))

    # Terra
    x = int(pos1_sol + (pos1_sol - pos1_sol * 0.4) * math.cos(radt))
    y = int(pos1_sol + (pos1_sol - pos1_sol * 0.4) * math.sin(radt))

    # Marte
    u = int(pos1_sol + (pos1_sol - pos1_sol * 0.2) * math.cos(radm))
    v = int(pos1_sol + (pos1_sol - pos1_sol * 0.2) * math.sin(radm))

    # lua
    p = int(x + 30 * math.cos(radl))
    m = int(y + 30 * math.sin(radl))

    # Venus
    graph1.cv.circle(img, (x, y), tam_terra, cor_terra, thick)

    # Terra
    graph1.cv.circle(img, (u, v), tam_marte, cor_marte, thick)

    # Marte
    graph1.cv.circle(img, (t, r), tam_venus, cor_venus, thick)

    # Lua
    graph1.cv.circle(img, (p, m), tam_lua, cor_lua, thick)

    # Mostra imagem
    graph1.cv.imshow('dark', img)
    graph1.time.sleep(0.01)

    radv = radv + (0.8 * math.pi) / 200
    radt = radt + (0.5 * math.pi) / 200
    radm = radm + (0.3 * math.pi) / 200
    radl = radl + (0.8 * math.pi) / 200

    if graph1.destroy_scene():
        break
