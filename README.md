## Australian Patent Search

---

### Web Scraping through API Call

#### How to run ?

1. Create python environment and activate

```py
    python -m venv .venv
    source .venv/bin/activate
```

2. Install dependencies

```py
    pip install -r requirements.txt
```

3. Update `QUERY` in `app.py` file. Default is `QUERY = "Robotic Surgery"`.

4. Run the program

```py
    python app.py
```

---

> **_NOTE:_** The result is an array of json objects, saved in a file named `results_{QUERY}.json` .
