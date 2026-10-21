# Klasyfikator zgłoszeń

Skrzynka helpdesku. Zgłoszenie ma temat, treść i datę. Kategorię dopisuje model (Ollama, domyślnie `qwen3:8b`). Jak żadna kolejka nie pasuje, zostaje brak dopasowania.

## Uruchomienie

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m app
```

Panel: http://127.0.0.1:8000

Ollama musi działać na http://127.0.0.1:11434. Na GTX 1070 przy sterowniku starszym niż 570 CUDA w tej Ollamie się wywala, wtedy:

```powershell
$env:OLLAMA_LLM_LIBRARY = "vulkan"
ollama serve
```

Pusta baza przy pierwszym starcie dostaje 100 przykładowych zgłoszeń. `python -m app.seed --force` kasuje zgłoszenia i wgrywa je od nowa.

API: http://127.0.0.1:8000/api/zgloszenia
