def read_filter():
    with open("filter.txt", 'r') as f:
        arquivo = f.readlines()

    arquivo_split = []
    aux = [float(x) for x in arquivo[0].split()]
    arquivo_split.append(aux)
    arquivo_split.append([])

    if arquivo[1] == "box":
        size = int(arquivo_split[0][0] * arquivo_split[0][1])
        for i in range(size):
            arquivo_split[1].append(1/size)

    if arquivo[1] == "sobel":
        arquivo_split.append([])
        arquivo_split[1] = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
        arquivo_split[2] = [-1, 0, 1, -2, 0, 2, -1, 0, 1]

    return arquivo_split


def my_filter(img):
    with open("filter.txt") as f:
        tipo = f.readlines()[1]

    pixel_map = img.load()
    copy_map = img.copy().load()

    width = img.width
    height = img.height

    filtro = read_filter()

    m = int(filtro[0][0])
    n = int(filtro[0][1])

    if m % 2 == 0:
        m += 1
    if n % 2 == 0:
        n += 1

    half_m = m//2
    half_n = n//2

    mini, maxi = get_min_max(img)

    for w in range(width):
        for h in range(height):
            r_total, g_total, b_total = [0, 0, 0]
            f_index = 0

            for filtro_x in range(max(0, w-half_m), min(width-1, w+half_m) + 1):
                for filtro_y in range(max(0, h-half_n), min(height-1, h+half_n) + 1):
                    r, g, b = copy_map[filtro_x, filtro_y]

                    r_total += r * filtro[1][f_index]
                    g_total += g * filtro[1][f_index]
                    b_total += b * filtro[1][f_index]

                    f_index += 1

            if tipo == "sobel":
                r_sobel, g_sobel, b_sobel = [0, 0, 0]
                f_index = 0

                for filtro_x in range(max(0, w-half_m), min(width-1, w+half_m) + 1):
                    for filtro_y in range(max(0, h-half_n), min(height-1, h+half_n) + 1):
                        r, g, b = copy_map[filtro_x, filtro_y]

                        r_sobel += r * filtro[2][f_index]
                        g_sobel += g * filtro[2][f_index]
                        b_sobel += b * filtro[2][f_index]

                        f_index += 1

                r_total = abs(r_total) + abs(r_sobel)
                g_total = abs(g_total) + abs(g_sobel)
                b_total = abs(b_total) + abs(b_sobel)

                r_total = ((r_total - mini[0]) / (maxi[0] - mini[0])) * 255
                g_total = ((g_total - mini[1]) / (maxi[1] - mini[1])) * 255
                b_total = ((b_total - mini[2]) / (maxi[2] - mini[2])) * 255

            pixel_map[w, h] = (int(r_total), int(g_total), int(b_total))


def get_min_max(img):
    pixel_map = img.load()

    width = img.width
    height = img.height

    mini = [255, 255, 255]
    maxi = [0, 0, 0]

    for w in range(width):
        for h in range(height):
            r, g, b = pixel_map[w, h]

            if r > maxi[0]:
                maxi[0] = r
            if r < mini[0]:
                mini[0] = r

            if g > maxi[1]:
                maxi[1] = g
            if g < mini[1]:
                mini[1] = g

            if b > maxi[2]:
                maxi[2] = b
            if b < mini[2]:
                mini[2] = b

    return [mini, maxi]
