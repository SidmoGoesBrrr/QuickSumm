import streamlit as st
import summarize_text
import summarize_audio
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
    summary_length = st.slider('What is the length of the summary', 0, 1, 0.4)

    if st.button("Summarise"):
        if text == "":
            st.error("Please enter text")
        else:
            with st.spinner('Wait for it...'):
                st.write("Summarised text:", font_size=20)
                text = summarize_text.summarize(text, summary_length)
                st.write(text)



def audio():
    audio = st.file_uploader("Upload Audio", type=['wav', 'mp3'])
    type_of_summary = st.selectbox("What type of summary would you like?",("bullets","bullets_verbose","gist","paragraph"))
    if st.button("Summarise"):
        if audio is None:
            st.error("You have not uploaded an audio file")
        else:
            url = summarize_audio.upload(audio)

            data, error = summarize_audio.get_transcription_result_url(url,type_of_summary)
            if error:
                print(error)
            st.write("Summarised text:", font_size=20)
            print(data['text'])
            st.write(data['summary'])
