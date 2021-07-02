import png

height = 32
width = 32
img = []

for y in range(height):
    row = ()
    for x in range(width):
        if (x + y) % 2 == 0:
            row = row + tuple("1")
        else:
            row = row + tuple("0")
    img.append(row)

new_list = []
for words in img:
    new_list.append(''.join(words))
# print(new_list)
img = [[int(c) for c in row] for row in new_list]

palette = [(0, 0, 0), (255, 255, 255)]
w = png.Writer(width, height, palette=palette, bitdepth=1)
f = open('png.png', 'wb')
w.write(f, img)
f.close()
