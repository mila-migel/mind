# Определяем переменную message и присваиваем ей значение "Hello, World!"
message = "Hello, World!"

# Выводим значение переменной message на экран
#Print this is:function
print(message)



import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

# Определяем размеры и отступы
box_width, box_height = 1, 0.6
decision_size = 1.2
arrowprops = dict(facecolor='black', edgecolor='black', arrowstyle='->')

# Функция для добавления прямоугольников
def add_box(text, xy):
    rect = patches.FancyBboxPatch(xy, box_width, box_height, boxstyle="round,pad=0.3", linewidth=2, edgecolor='black', facecolor='lightblue')
    ax.add_patch(rect)
    ax.text(xy[0] + box_width / 2, xy[1] + box_height / 2, text, horizontalalignment='center', verticalalignment='center', fontsize=10, weight='bold')

# Функция для добавления ромбов
def add_diamond(text, center):
    diamond = patches.RegularPolygon(center, numVertices=4, radius=decision_size/2, orientation=0, linewidth=2, edgecolor='black', facecolor='black')
    ax.add_patch(diamond)
    ax.text(center[0], center[1], text, horizontalalignment='center', verticalalignment='center', fontsize=10, weight='bold', color='white')

# Добавляем узлы
add_box("Hard", (0, 0))
add_box("Round", (2, 0))
add_diamond("Decision", (4, 0))
add_box("Result 1", (6, 1))
add_box("Result 2", (6, -1))

# Добавляем стрелки
ax.annotate("", xy=(2, 0.3), xytext=(1, 0.3), arrowprops=arrowprops)
ax.text(1.5, 0.4, "MyText", horizontalalignment='center', verticalalignment='center', fontsize=8, weight='bold')

ax.annotate("", xy=(4 - decision_size / 2, 0), xytext=(3, 0), arrowprops=arrowprops)

ax.annotate("", xy=(5, 0.6), xytext=(4 + decision_size / 2, 0), arrowprops=arrowprops)
ax.text(5, 0.7, "One", horizontalalignment='center', verticalalignment='center', fontsize=8, weight='bold')

ax.annotate("", xy=(5, -0.6), xytext=(4 + decision_size / 2, 0), arrowprops=arrowprops)
ax.text(5, -0.7, "Two", horizontalalignment='center', verticalalignment='center', fontsize=8, weight='bold')

# Настройка осей
ax.set_xlim(-1, 7)
ax.set_ylim(-2, 2)
ax.axis('off')

plt.savefig('/mnt/data/flowchart.png')
plt.show()
