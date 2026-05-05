<h4 align="center">p4 - Flask with Forms, POST</h4>

1. [What](#what)
2. [Dirz](#dirz)
3. [Deployed](#deployed)

# What

1. This proejct is for testing forms
2. The project is structured for isolating `routes` using `blueprint` a feature of flask
3. Strucuture is little complicated

# Dirz

|                     Dir                     |                 What                  |
| :-----------------------------------------: | :-----------------------------------: |
|                [`sc`](./sc/)                |           Execution Scripts           |
|                [`do`](./do/)                |               HTML Docs               |
|             [`tempz`](./tempz/)             |         HTML Template Folder          |
|            [`routes`](./routes/)            | Folder where routes are being defined |
|            [`app.py`](./app.py/)            |        Application entry point        |
| [`limiter_config.py`](./limiter_config.py/) |         Flask Limiter Global          |

# Deployed

|                                     What                                     |    Explain     |
| :--------------------------------------------------------------------------: | :------------: |
|  [`https://mx-pfla-p4-api.vercel.app/`](https://mx-pfla-p4-api.vercel.app/)  | Flask Endpoint |
| [`https://mx-pfla-p4-docz.vercel.app/`](https://mx-pfla-p4-docz.vercel.app/) |      Docs      |

- Notice the naming convention
- `https://mx-pfla-p4-XXX.vercel.app` - `XXX` defines whether it is app or docs
