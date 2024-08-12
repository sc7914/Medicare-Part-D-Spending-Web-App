# README

## Setup

Create virtual environment:

```sh
conda create -n ump-env python=3.11
```

Activate the environment:

```sh
conda activate ump-env
```

Install packages:

```sh
#pip install requests
#pip install plotly
#pip install python-dotenv

# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
```

## Usage

Medicare Part D spending:

```sh
python -m app.medicare
```

Pull revenue:

```sh
python -m app.revenue
```
Pull calculate exposure:

```sh
python -m app.exposure
```


Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

export FLASK_APP=web_app
flask run

##Testing