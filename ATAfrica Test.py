import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = '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'

def clean_text(text):
    # Placeholder function for text preprocessing
    return text

def format_code(code):
    # Placeholder function for code formatting
    return code

def create_prompt(user_description):
    # Preprocess and format user description
    processed_text = clean_text(user_description)
    # Craft prompt with instructions and user input
    prompt = f"Generate Python code to {processed_text}. I am targeting users with Python knowledge and want the code to be readable and efficient."
    return prompt

def generate_code(prompt):
    # Use OpenAI API to send prompt and retrieve response
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    generated_code = response.choices[0].text.strip()
    return generated_code

def explain_code(code):
    # Preprocess and format code for explanation model
    processed_code = format_code(code)
    # Craft prompt to request explanation for 5-year-old
    prompt = f"Explain this Python code in simple terms that a 5-year-old could understand: {processed_code}"
    # Utilize another OpenAI model for explanation
    explanation_response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    explanation = explanation_response.choices[0].text.strip()
    return explanation

def main():
    st.title("Python Code Generator and Explainer")

    user_description = st.text_input("Enter a description of what you want the code to do:")
    
    if st.button("Generate Code"):
        prompt = create_prompt(user_description)
        generated_code = generate_code(prompt)
        st.code(generated_code, language='python')

    if st.button("Explain Code"):
        user_code = st.text_area("Enter Python code:")
        explanation = explain_code(user_code)
        st.write("Explanation:")
        st.write(explanation)

if __name__ == "__main__":
    main()
