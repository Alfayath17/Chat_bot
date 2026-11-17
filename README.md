# Python Course

Notebooks and small apps from a Python course. The course goes from Python basics to building apps on Google Gemini with Streamlit and FastAPI.

## Contents

### Python basics (Jupyter notebooks)

| Notebook | Topic |
|---|---|
| `datatype-and_for_loop.ipynb` | Data types, variables and `for` loops |
| `functions.ipynb` | Writing functions and returning multiple values |
| `classes.ipynb` | Classes, methods and Pydantic models |
| `practice.ipynb` | Practice: classes, lists and dictionaries |
| `file_handling.ipynb` | Reading and writing text files (writes `joke.text`) |
| `api_call.ipynb` | Calling a web API with `requests` (USD to INR exchange rate) |
| `db_int.ipynb` | Working with a SQLite database (creates `shop.db`) |

### Working with Gemini (Jupyter notebooks)

| Notebook | Topic |
|---|---|
| `call_llm.ipynb` | First Gemini call and a `generate_recipe()` function |
| `structure_output.ipynb` | Getting JSON back from the model, with Pydantic schemas |
| `chatbot-memory.ipynb` | Giving a chatbot memory by sending the full conversation history |

### Apps

| File | What it does |
|---|---|
| `recipe_app.py` | Streamlit app that writes a recipe from your ingredients, cuisine and diet |
| `chatbot_app.py` | Streamlit chatbot that remembers the conversation |
| `fast_api/main.py` | FastAPI server with a profit-margin endpoint and a review sentiment endpoint |

## Setup

1. Install Python 3.12 or later.
2. Install the packages:

   ```bash
   pip install google-genai python-dotenv streamlit fastapi uvicorn requests pydantic jupyter
   ```

3. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).
4. Create a file named `.env` in the project folder with this line:

   ```
   GEMINI_API_KEY=your-api-key-here
   ```

   `.env` is listed in `.gitignore`, so your key is not committed to git.

## Running the apps

**Recipe generator**

```bash
python -m streamlit run recipe_app.py
```

**Chatbot with memory**

```bash
python -m streamlit run chatbot_app.py
```

Both open in your browser at http://localhost:8501.

**FastAPI server**

```bash
cd fast_api
python -m uvicorn main:app --reload
```

Then open http://localhost:8000/docs to try the endpoints:

- `GET /` returns a welcome message.
- `GET /margin?revenue=100&expenses=40` returns the profit and the margin percentage.
- `POST /sentiment` with `{"text": "The biryani was amazing!"}` returns a sentiment label and a score from 1 to 5.

## Running the notebooks

Open a notebook in VS Code or run `jupyter notebook`, then run the cells from top to bottom. The Gemini notebooks need the `.env` file from the setup steps.
