data_str = """
- Detected Emotion: 기쁨
- Movie 1: "라라랜드", [유쾌하고 음악적인 요소가 풍부하여 기분을 좋게 해주는 영화입니다. 주인공들이 꿈을 쫓는 과정에서 느끼는 즐거움이 당신의 기분과 잘 어울립니다.]
- Movie 2: "인생은 아름다워", [슬픔을 담고 있지만, 사랑과 가족의 힘을 느낄 수 있는 영화로, 긍정적인 메시지를 통해 마음을 따뜻하게 해줄 것입니다.]
- Diary Review: [오늘의 일기에서는 좋은 날씨 속에서 운동을 하며 맛있는 음식을 즐기는 기쁜 하루를 보냈다는 내용을 담고 있습니다. 전반적으로 긍정적인 감정이 드러나며, 행복한 순간을 소중히 여기는 것 같아요.]
"""

# 1. 데이터를 JSON이나 딕셔너리 형태로 가공하기
import re

parsed_data = {}

# 감정 추출
emotion_match = re.search(r"- Detected Emotion: (.+)", data_str)
if emotion_match:
    parsed_data['detected_emotion'] = emotion_match.group(1).strip()

# Movie 1과 Movie 2 정보 추출
movies = re.findall(r"- Movie \d+: \"(.+)\", \[(.+)\]", data_str)
parsed_data['movies'] = [{'title': movie[0], 'reason': movie[1]} for movie in movies]

# Diary Review 추출
review_match = re.search(r"- Diary Review: \[(.+)\]", data_str)
if review_match:
    parsed_data['diary_review'] = review_match.group(1).strip()

print(parsed_data)
