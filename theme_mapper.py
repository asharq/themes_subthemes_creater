import streamlit as st
import json
import logging

logging.basicConfig(level=logging.INFO)

def create_theme_form(index):
    with st.form(key=f'theme_form_{index}'):
        theme = st.text_input(f"Theme {index+1}")
        intents = st.multiselect(f"Intents {index+1}", options=["Product Issue", "Positive Aspect"])
        subthemes = st.text_area(f"Subthemes {index+1}", height=200)
        subthemes_list = [s.strip() for s in subthemes.split("\n") if s.strip()]
        # No "Save Changes" button here

    return {
        "theme": theme,
        "intents": intents,
        "subthemes": subthemes_list
    }

def main():
    st.title("Theme and Subtheme Creator")
    st.write("Create and manage themes, intents, and subthemes for text review categorization.")

    themes_and_subthemes = []

    num_themes = st.number_input("Number of Themes", min_value=1, max_value=40, value=5, step=1)

    for i in range(int(num_themes)):
        new_theme = create_theme_form(i)
        if new_theme["theme"].strip():
            themes_and_subthemes.append(new_theme)
        else:
            st.error(f"Please enter a theme for Theme {i+1}.")

    if themes_and_subthemes:
        st.subheader("JSON Preview")
        json_data = json.dumps(themes_and_subthemes, indent=4)
        st.code(json_data)

        if st.download_button(
            label="Download JSON",
            data=json_data,
            file_name="themes_and_subthemes.json",
            mime="application/json",
        ):
            st.success("JSON file downloaded successfully!")
    else:
        st.warning("Please add at least one theme before downloading the JSON file.")

if __name__ == "__main__":
    main()
