import streamlit as st
import json

def create_theme_form():
    with st.form(key='theme_form'):
        theme = st.text_input("Theme")
        intents = st.multiselect("Intents", options=["Product Issue", "Positive Aspect"])
        subthemes = st.text_area("Subthemes", height=200)
        subthemes_list = [s.strip() for s in subthemes.split("\n") if s.strip()]
        submit = st.form_submit_button("Add Theme")

        if submit:
            return {
                "theme": theme,
                "intents": intents,
                "subthemes": subthemes_list
            }
    return None

def main():
    st.title("Theme and Subtheme Creator")
    st.write("Create and manage themes, intents, and subthemes for text review categorization.")

    themes_and_subthemes = []

    while True:
        new_theme = create_theme_form()
        if new_theme:
            themes_and_subthemes.append(new_theme)
        else:
            break

    if st.button("Download JSON"):
        json_data = json.dumps(themes_and_subthemes, indent=4)
        st.download_button(
            label="Download JSON",
            data=json_data,
            file_name="themes_and_subthemes.json",
            mime="application/json",
        )

if __name__ == "__main__":
    main()
