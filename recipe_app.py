import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-3.5-flash"


@st.cache_resource
def get_client():
    return genai.Client()


def generate_recipe(ingredients, cuisine, diet, max_words):
    """Generate a recipe using the ingredients provided."""
    prompt = f"""
    Generate a recipe using the following ingredients:
    {', '.join(ingredients)}

    Recipe should not be more than {max_words} words.
    Cuisine: {cuisine}
    Diet: {diet}
    """
    response = get_client().models.generate_content(model=MODEL, contents=prompt)
    return response.text


st.set_page_config(page_title="Recipe Generator", page_icon="🍳")
st.title("🍳 AI Recipe Generator")
st.caption(f"Powered by Google Gemini ({MODEL})")

with st.form("recipe_form"):
    ingredients_text = st.text_area(
        "Ingredients (comma-separated)",
        placeholder="Tomato, Onion, Rice, Potato",
    )
    col1, col2 = st.columns(2)
    with col1:
        cuisine = st.selectbox(
            "Cuisine",
            ["Any", "Indian", "Italian", "Mexican", "Chinese", "Thai", "Mediterranean"],
        )
    with col2:
        diet = st.selectbox(
            "Diet",
            ["Any", "Vegetarian", "Vegan", "Jain", "Eggetarian", "Keto", "Gluten-free"],
        )
    max_words = st.slider("Max recipe length (words)", 50, 400, 100, step=50)
    submitted = st.form_submit_button("Generate Recipe")

if submitted:
    ingredients = [i.strip() for i in ingredients_text.split(",") if i.strip()]
    if not ingredients:
        st.warning("Please enter at least one ingredient.")
    else:
        with st.spinner("Cooking up your recipe..."):
            try:
                recipe = generate_recipe(ingredients, cuisine, diet, max_words)
                st.markdown(recipe)
                st.download_button(
                    "Download recipe",
                    recipe,
                    file_name="recipe.md",
                    mime="text/markdown",
                )
            except Exception as e:
                st.error(f"Failed to generate recipe: {e}")
