figures_1 = input('List_1. Print any number of figures, separated with commas (no whitespaces needed, e.g. 1,4,5,3... ):  ')
figures_2 = input('List_2. Again print any number of figures, separated with commas (no whitespaces needed, e.g. 1,4,5,3... ):  ')
sep_figures_1 = figures_1.split(',')
sep_figures_2 = figures_2.split(',')

for i in range(len(sep_figures_2)):
    f = sep_figures_2.pop(0)
    if f in sep_figures_1:
        sep_figures_1.remove(f)

print(sep_figures_1)