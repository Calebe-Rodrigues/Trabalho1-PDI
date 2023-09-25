def RGBtoHSB(red, green, blue):
    # normalize red, green and blue values
    r = (float(red) / 255.0)
    g = (float(green) / 255.0)
    b = (float(blue) / 255.0)

    # conversion start
    maxi = max(r, g, b)
    mini = min(r, g, b)

    h = 0.0
    if maxi == r and g >= b and maxi - mini != 0:
        h = 60 * (g - b) / (maxi - mini)
    elif maxi == r and g < b and maxi - mini != 0:
        h = 60 * (g - b) / (maxi - mini) + 360
    elif maxi == g and maxi - mini != 0:
        h = 60 * (b - r) / (maxi - mini) + 120
    elif maxi == b and maxi - mini != 0:
        h = 60 * (r - g) / (maxi - mini) + 240

    s = 0.0 if (maxi == 0) else (1.0 - (mini / maxi))

    return [h, s, float(maxi)]


def HSBtoRGB(h, s, v):
    r = 0.0
    g = 0.0
    b = 0.0

    if not (s > 0):
        r = v
        g = v
        b = v
    else:
        # the color wheel consists of 6 sectors. Figure out which sector
        # you're in.
        sector_pos = h / 60.0
        sector_number = h // 60
        # get the fractional part of the sector
        fractional_sector = sector_pos - sector_number

        # calculate values for the three axes of the color.
        p = v * (1.0 - s)
        q = v * (1.0 - (s * fractional_sector))
        t = v * (1.0 - (s * (1 - fractional_sector)))

        # assign the fractional colors to r, g, and b based on the sector
        # the angle is in.
        if sector_number == 0:
            r = v
            g = t
            b = p
        elif sector_number == 1:
            r = q
            g = v
            b = p
        elif sector_number == 2:
            r = p
            g = v
            b = t
        elif sector_number == 3:
            r = p
            g = q
            b = v
        elif sector_number == 4:
            r = t
            g = p
            b = v
        elif sector_number == 5:
            r = v
            g = p
            b = q

    return [int(r * 255), int(g * 255), int(b * 255)]
