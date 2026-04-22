<h3 align="center"> <i> p1 - 1st version of python flask </i> </h3>

1. [What](#what)
2. [Dirz](#dirz)
3. [App Summary](#app-summary)
4. [Regarding params](#regarding-params)
5. [Active Deployment](#active-deployment)
   1. [Current Endpoint](#current-endpoint)

# What

1. First version of python flasks study

# Dirz

|           Dir           |       What        |
| :---------------------: | :---------------: |
| [`runs.sh`](./runs.sh/) | Logs from runz.sh |
|    [`logz`](./logz/)    |  Logs from ru.sh  |

# App Summary

1. Testing more endpoints to resemble a webapp

# Regarding params

```python
@app.route('/handle_url_params')
def handle_params():
    return str(request.args)
```

- When you go to this route it will show an empty dictionary
- Then you can add elements to this dictionary with the url below

```sh
https://fluffy-telegram-97679qp95pvf4xg-5000.app.github.dev/handle_url_params?=Nike&booty=Smell&Bonda=Lunda

# Output
ImmutableMultiDict([('', 'Nike'), ('booty', 'Smell'), ('Bonda', 'Lunda')])

# Another variation
https://fluffy-telegram-97679qp95pvf4xg-5000.app.github.dev/handle_url_params2?name=Mike&greeting=Fuck
# Result
Fuck, Mike!
```

- The `params` in the url are actualy adding to the python dictionary

# Active Deployment

1. This was deployed to VerPANTYcel , since it allows simple python flaskapps
2. Easy deploy with `vc --prod`

## Current Endpoint

```sh
https://ftut1.vercel.app/
```

- Note just a direct UL
