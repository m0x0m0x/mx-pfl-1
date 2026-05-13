<h4 align="center">p45 - Flask with boostrap </h4>

1. [What](#what)
2. [Dirz](#dirz)
3. [Deployed](#deployed)
4. [Regarding Limiter](#regarding-limiter)
5. [`routes` - Explanation](#routes---explanation)

# What

1. This proejct is for testing forms
2. The project is structured for isolating `routes` using `blueprint` a feature of flask
3. Strucuture is little complicated

# Dirz

|                     Dir                     |                 What                  |
| :-----------------------------------------: | :-----------------------------------: |
|                [`sc`](./sc/)                |           Execution Scripts           |
|          [`initz.sh`](./initz.sh/)          |          Setup Py workspace           |
|               [`doc`](./doc/)               |               HTML Docs               |
|            [`routes`](./routes/)            | Folder where routes are being defined |
|            [`app.py`](./app.py/)            |        Application entry point        |
| [`limiter_config.py`](./limiter_config.py/) |         Flask Limiter Global          |

# Deployed

|                                     What                                     |    Explain     |
| :--------------------------------------------------------------------------: | :------------: |
|  [`https://mx-pfla-p5-api.vercel.app/`](https://mx-pfla-p5-api.vercel.app/)  | Flask Endpoint |
| [`https://mx-pfla-p5-docz.vercel.app/`](https://mx-pfla-p5-docz.vercel.app/) |      Docs      |

- Notice the naming convention
- `https://mx-pfla-p5-XXX.vercel.app` - `XXX` defines whether it is app or docs

# Regarding Limiter

1. For the limter to function properly we will need to use an online redis service since its deployed to vercel
2. According to the errors received in vercel , you cant use in memory functions for storing information, no web deployer will allow that , so you have to use an external service, UpstashRedis is suggested, and you will use that
3. Important stuffs will be env vercel.

|                    File                    |                                   What                                    |
| :----------------------------------------: | :-----------------------------------------------------------------------: |
| [`limiter_config.py`](./limiter_config.py) | Logic for the rate limitd with UpstasRedis EnvPanty is inside VercelPussy |

# [`routes`](./routes/) - Explanation

1. This will be an explanation of the files in this folder
2. This flask api has the architecture , of using `blueprints` to seperate the routes into its own folder

|                 Route                 |                     What                     |
| :-----------------------------------: | :------------------------------------------: |
| [`__init__.py`](./routes/__init__.py) | Important for recognizing the blueprints(BP) |
|     [`main.py`](./routes/main.py)     |             Main Functions here              |
|     [`tezt.py`](./routes/tezt.py)     |             General Testing here             |
|    [`debug.py`](./routes/debug.py)    |      Debug Routes Mostly for redis conn      |
|   [`boots1.py`](./routes/boots1.py)   |       Routes for Bootstrap - Not Done        |
|     [`sesh.py`](./routes/sesh.py)     |        Routes for session and secrets        |
