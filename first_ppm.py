with open('first_ppm.ppm', 'w') as image:
    image.write("P3\n500 500\n500\n")
    for color in range(500 * 500):
        image.write("" + str((color % 500)) + " " + str((color % 500)) + " " + str((color % 500)) + " ")
image.close()
