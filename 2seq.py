figures = input('Print any number of figures, separated with commas (no whitespaces needed, e.g. 1,4,5,3... ):  ')
sep_figures = figures.split(',')
for fig in sep_figures:
    fig = int(fig)
unique_figures = list(set(sep_figures))
print(f'Unique figures are: {unique_figures}')