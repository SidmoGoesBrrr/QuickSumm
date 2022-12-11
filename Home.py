import streamlit as st
import summarize_text

st.header("Audio Visual Text Summariser")
st.subheader("This is a web app that summarises text and audio")

add_selectbox = st.sidebar.selectbox(
    'How would you like enter text?',
    ('', 'Text', 'Audio')
)

if add_selectbox == 'Text':
    text()

elif add_selectbox == 'Audio':
    audio()


def text():
    import streamlit as st
    text = st.text_area("Enter text here", height=200)
    summary_length = st.slider('How old are you?', 0, 1, 0.4)

    if st.button("Summarise"):
        if text == "":
            st.error("Please enter text")
        else:
            text = summarize_text.summarize(text, summary_length)
            st.write("Summarised text:", font_size=20)
            st.write(text)


def audio():
    audio = st.file_uploader("Upload Audio", type=['wav', 'mp3'])
    if st.button("Summarise"):
        if audio is None:
            st.error("You have not uploaded an audio file")
        else:
            #summarize audio here
            st.write("Summarised text:", font_size=20)
