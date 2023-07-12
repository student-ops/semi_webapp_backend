## curl

```

curl --no-buffer -X POST -H "Content-Type: application/json" -d '{
  "bot_name": "faculty",
  "question": "どのような人材を目指していますか"
}' http://localhost:4000/llama_chat


// ソースノード
curl -X POST -H "Content-Type: application/json" -d '{
  "question_id": "61c12def-eed6-4afd-8ae5-5919810e7601",
}' http://localhost:4000/verify_source_node


// 検証結果
curl -X POST -H "Content-Type: application/json" -d '{
  "question_id": "61c12def-eed6-4afd-8ae5-5919810e7601",
}' http://localhost:4000/verify
```

```
docker run -d -p 6379:6379 redis
```

redis memory check

```
cedis-cli: not found
```


