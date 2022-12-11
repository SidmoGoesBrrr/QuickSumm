import streamlit as st
import summarize_text
import summarize_audio
st.header("Audio Visual Text Summariser")
st.subheader("This is a web app that summarises text and audio")
placeholder = st.empty()
placeholder.image("https://miro.medium.com/max/531/0*UhKdZfJHuXJDYMbh")
def text():
    import streamlit as st
    text = st.text_area("Enter text here", height=200)
    placeholder.empty()
    summary_length = st.slider( "Enter the percentage of text you want to summarise",1, 100, 40)
    summary_length= summary_length/100
    if st.button("Summarize"):
        if text == "":
            st.error("Please enter text to summarize")
        else:
            with st.spinner('Summarizing...'):
                text = summarize_text.summarize(text, summary_length)
                st.write("Summarized text:", font_size=20)
                st.write(text)



def audio():
    audio = st.file_uploader("Upload Audio", type=['wav', 'mp3'])
    type_of_summary = st.selectbox("What type of summary would you like?",("bullets","bullets_verbose","gist","paragraph"))
    placeholder.empty()

    if st.button("Summarize"):
        if audio is None:
            st.error("You have not uploaded an audio file")
        else:
            with st.spinner('Summarizing...'):
                url = summarize_audio.upload(audio)

                data, error = summarize_audio.get_transcription_result_url(url,type_of_summary)
                if error:
                    print(error)
                    st.error("Oops there as an error")
                else:
                    st.write("Summarized text")
                    print(data['text'])
                    st.write(data['summary'])

add_selectbox = st.sidebar.selectbox(
    'How would you like enter text?',
    ('', 'Text', 'Audio')
)

if add_selectbox == 'Text':
    text()

elif add_selectbox == 'Audio':
    audio()

