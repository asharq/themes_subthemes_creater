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
        submit = st.form_submit_button("Save Changes")

        if submit:
            if theme.strip():
                logging.info(f"Added theme: {theme}")
                return {
                    "theme": theme,
                    "intents": intents,
                    "subthemes": subthemes_list
                }
            else:
                st.error(f"Please enter a theme for Theme {index+1}.")
    return None

def main():
    st.title("Theme and Subtheme Creator")
    st.write("Create and manage themes, intents, and subthemes for text review categorization.")

    themes_and_subthemes = []

    num_themes = st.number_input("Number of Themes", min_value=1, max_value=40, value=5, step=1)

    for i in range(int(num_themes)):
        new_theme = create_theme_form(i)
        if new_theme:
            themes_and_subthemes.append(new_theme)

    if st.button("Save Changes"):
        if themes_and_subthemes:
            json_data = json.dumps(themes_and_subthemes, indent=4)
            if st.download_button(
                label="Download JSON",
                data=json_data,
                file_name="themes_and_subthemes.json",
                mime="application/json",
            ):
                st.success("JSON file downloaded successfully!")
        else:
            st.warning("Please add at least one theme before downloading the JSON file.")

    if themes_and_subthemes:
        st.subheader("JSON Preview")
        st.code(json.dumps(themes_and_subthemes, indent=4))

if __name__ == "__main__":
    main()
