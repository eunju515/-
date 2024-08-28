import streamlit as st

# Set the title of the web app
st.title('나의 첫 웹 서비스 만들기!!')

# Text input for user's name
name = st.text_input('이름을 입력해주세요 : ')

# Dropdown menu for selecting MBTI type
mbti = st.selectbox(
    'MBTI를 선택해주세요:', 
    ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 
     'ISTP', 'ISFP', 'INFP', 'INTP', 
     'ESTP', 'ESFP', 'ENFP', 'ENTP', 
     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
)

# Dictionary to store detailed MBTI descriptions
mbti_descriptions = {
    'ISTJ': 'ISTJ는 성실하고 현실적인 성격을 가지며, 체계적이고 책임감이 강합니다.',
    'ISFJ': 'ISFJ는 친절하고 책임감이 강하며, 타인의 감정을 잘 이해하는 성격입니다.',
    'INFJ': 'INFJ는 이상적이고 통찰력이 뛰어나며, 다른 사람을 돕는 것을 즐깁니다.',
    'INTJ': 'INTJ는 독립적이고 분석적이며, 논리적인 계획을 세우는 것을 좋아합니다.',
    'ISTP': 'ISTP는 실용적이고 문제 해결 능력이 뛰어나며, 새로운 경험을 즐깁니다.',
    'ISFP': 'ISFP는 온화하고 유연하며, 창의적이고 예술적인 활동을 좋아합니다.',
    'INFP': 'INFP는 이상적이고 공감 능력이 뛰어나며, 깊이 있는 생각을 즐깁니다.',
    'INTP': 'INTP는 논리적이고 호기심이 많으며, 복잡한 문제를 해결하는 것을 좋아합니다.',
    'ESTP': 'ESTP는 활동적이고 현실적이며, 문제를 해결하는 데 능숙합니다.',
    'ESFP': 'ESFP는 사교적이고 열정적이며, 현재의 순간을 즐깁니다.',
    'ENFP': 'ENFP는 창의적이고 열정적이며, 사람들과의 교류를 즐깁니다.',
    'ENTP': 'ENTP는 논쟁을 좋아하고 혁신적인 아이디어를 찾는 것을 즐깁니다.',
    'ESTJ': 'ESTJ는 조직적이고 실용적이며, 리더십을 발휘하는 것을 좋아합니다.',
    'ESFJ': 'ESFJ는 타인을 돕고 배려하며, 사회적 관계를 중요하게 생각합니다.',
    'ENFJ': 'ENFJ는 타인의 성장을 돕고 영감을 주는 것을 좋아합니다.',
    'ENTJ': 'ENTJ는 결단력 있고 목표 지향적이며, 리더십을 발휘하는 것을 즐깁니다.'
}

# Button to generate the greeting
if st.button('인사말 생성'):
    # Display a personalized greeting along with MBTI description
    st.write(f"{name}님! 당신의 MBTI 유형은 {mbti}이군요?!")
    st.write(f"{mbti_descriptions[mbti]}")

  
