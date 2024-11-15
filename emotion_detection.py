import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        response_dict = response.json()
        emotions = response_dict.get("emotion", {})
        scores = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
        }
        
        # Find the dominant emotion
        dominant_emotion = max(scores, key=scores.get)
        scores['dominant_emotion'] = dominant_emotion
        
        return scores
    else:
        response.raise_for_status()
