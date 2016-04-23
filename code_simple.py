from ipywidgets import IntSlider, Text, VBox
from IPython.display import display

s = IntSlider(max=200, value=100)
t = Text()

def update_text(change):
    t.value = str(s.value ** 2)

s.observe(update_text, names='value')
display(VBox([s, t]))