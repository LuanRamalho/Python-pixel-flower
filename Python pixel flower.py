from PIL import Image
import math

width, height = 31, 31
# Cria uma imagem RGB com fundo preto
image = Image.new("RGB", (width, height), (0, 0, 0))
pixels = image.load()

for y in range(height):
    for x in range(width):
        dx, dy = x - 15, y - 15
        r = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)
        
        petal = abs(math.sin(5 * angle))
        if r < 10 + 5 * petal:
            pixels[x, y] = (255, int(80 + 150 * petal), 220)
        elif r < 3:
            pixels[x, y] = (255, 220, 40)

# Redimensiona a imagem para ficar maior e mais visível na tela
image_ampliada = image.resize((465, 465), Image.NEAREST)
image_ampliada.show()