import re
import os
import openai
import streamlit as st

api_key = os.environ.get('API_KEY')
openai.api_key = api_key

def calculate_similarity_using_gpt(string1, string2):

    # text = f"""Your task is to answer in a consistent style. Compare the two strings given based on their meanings. 
    #         String 1 = {string1}, String 2 = {string2}. 
    #         Find the semantic similarity between the two strings. Comment whether they are similar or not in terms of their meaning.
    #         Display a value between 0 and 1 to show how much they are related to each other in format 'Similarity score: obtained value'
    #         """


    text = """Your task is to respond in a consistent manner. 
    Analyze the two provided strings and evaluate their semantic similarity. Here are the strings to be compared:
    String 1: {string1}
    String 2: {string2}
    Find the semantic similarity between the two strings. Comment whether they are similar or not in terms of their meaning.
    Display a value between 0 and 1 to show how much they are related to each other in format 'Similarity score: obtained value'
    """
    result = openai.Completion.create(
    model='text-davinci-003',
    prompt=text,
    max_tokens=500,
    temperature=0)

    return result.choices[0].text
def transform_string(string):
    # Insert space before first capital letter after first character
    string = re.sub(r'(?<=\w)([A-Z])', r' \1', string, count=1)

    string = string.lower()
    # Replace underscores with spaces
    string = string.replace('_', ' ')

    return string
def main():
    st.title("📝String Similarity Calculator")
    string1 = st.text_input("Enter the first string:")
    string2 = st.text_input("Enter the second string:")
    
    if st.button("Calculate Similarity"):

        string1 = transform_string(string1)
        string2 = transform_string(string2)

        similarity_response = calculate_similarity_using_gpt(string1, string2)
        st.write(f"String 1: {string1}")
        st.write(f"String 2: {string2}")
        st.write(f"{similarity_response}")

if __name__ == "__main__":
    main()