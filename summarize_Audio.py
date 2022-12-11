import requests
import time

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers_auth_only = {'authorization': '60deafcf49f0493ba71be566aa3a0734'}
headers = {
    "authorization": '60deafcf49f0493ba71be566aa3a0734',
    "content-type": "application/json"
}


def upload(file):
    response = requests.post(upload_endpoint,
                             headers=headers_auth_only,
                             data=file)
    return response.json()['upload_url']


def transcribe(upload_url, type_of_summary):
    json = {
        "audio_url": upload_url,
        "summarization": True,
        "summary_model": "informative",
        "summary_type": type_of_summary,
    }

    transcript_response = requests.post(transcript_endpoint, json=json, headers=headers_auth_only)
    return transcript_response.json()['id']


def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(url, type_of_summary):
    transcribe_id = transcribe(url, type_of_summary)
    while True:
        data = poll(transcribe_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        # this time is needed to transcribe the audio
        time.sleep(30)