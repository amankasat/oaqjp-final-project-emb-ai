import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_joy_detection(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger_detection(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust_detection(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness_detection(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear_detection(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()