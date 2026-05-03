<h4 align="center"><code>tempz</code> folder </h4>

1. [What](#what)
2. [Rendering Template HTML](#rendering-template-html)
3. [Regarding templating](#regarding-templating)

# What

1. This folder has all the template html that is being rendered.

# Rendering Template HTML

1. in the file - [`../routes/main.py`](../routes/main.py) -

```py
# In the code below we define the html that beeds to be rendered
@main_bp.route('/')
def home():
    return render_template('index.html')
```

2. Note that in order for templates to be rendered you have to define the folder - [`../app.py`](../app.py)

```py
# If this is not defined FlaskServer will not know where to look for the html to be rendered
app = Flask(__name__, template_folder='tempz')
```

# Regarding templating

1. The actual template html is [`base.html`](./base.html) - This serves as the main template , so you dodnt hav to keep writing the same code over and over agin , especially the styling part
2. Then in subsequent HTML files you can first call the template , eg - [`f1.html`](./f1.html)
