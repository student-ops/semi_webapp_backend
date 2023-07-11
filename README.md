## curl

```

curl --no-buffer -X POST -H "Content-Type: application/json" -d '{
  "bot_name": "faculty",
  "question": "どのような人材を目指していますか"
}' http://localhost:4000/llama_chat

```

## 再起動時
```
source myvenv/bin/activate
pip install -r requirements.txt
python src/scraping/main.py
```


```

python3 -m venv myvenv
source myvenv/bin/activate
pip install  -r requirements.txt

```

```
 pip freeze > requirements.txt
```