import pandas as pd
import streamlit as st
import numpy as np
data=pd.read_csv('참가신청 정보.csv')
data.dropna(subset=['참가 직군'],inplace=True)
data2=data[['유저아이디','커리어카드 URL','참가 직군','기획_참가 분야','디자인_참가 분야','개발_참가 분야','연차','총 투입 가능 시간']]
data2['총 투입 가능 시간']=data2['총 투입 가능 시간'].replace('60시간 이상',60)
data2['총 투입 가능 시간']=data2['총 투입 가능 시간'].astype(int)
year_experience_mapping = {
    '학생 및 취준': 0,
    '만 6개월 미만': 1,
    '만 6개월 이상 1년 미만': 2,
    '만 1년 이상 2년 미만': 3,
    '만 2년 이상 3년 미만': 4,
    '만 3년 이상 4년 미만': 5,
    '만 4년 이상 5년 미만': 6,
    '만 5년 이상 10년 미만': 7
}
data2['연차_순서'] = data2['연차'].map(year_experience_mapping)
개발자 = data2[data2['참가 직군'] == '개발']
개발자 = 개발자[개발자['개발_참가 분야'].isin(['백엔드', '프론트엔드 (Web)', '프론트엔드 (App)'])]
개발자['개발_참가 분야'] = 개발자['개발_참가 분야'].replace({'프론트엔드 (Web)': '프론트엔드', '프론트엔드 (App)': '프론트엔드'})
data2=pd.concat([data2[data2['참가 직군']!='개발'],개발자])
st.title('추천 멤버 제안 3가지 방안')
target_user_id=st.text_input('추천 받고자 하는 유저 ID')
n_recommendation=st.number_input('받고 싶은 추천 멤버 수(1~10)',min_value=1,max_value=10,step=1)
st.markdown("""
    <style>
    .css-18e3th9 {
        padding: 1rem 1rem;  # 사이드바의 내부 여백 조정
    }
    </style>
    """, unsafe_allow_html=True)
st.sidebar.subheader("유저 리스트")
st.sidebar.dataframe(data2[['유저아이디','참가 직군','연차']])
if target_user_id:
    if target_user_id in data2['유저아이디'].values:
        참가직군 = data2[data2['유저아이디'] == target_user_id]['참가 직군'].values[0]
        연차 = data2[data2['유저아이디'] == target_user_id]['연차'].values[0]
        st.markdown(f'##### **유저의 참가 직군**: <span style="color: blue">**{참가직군}** </span>', unsafe_allow_html=True)
        st.markdown(f'##### **유저의 연차** :<span style="color: blue">**{연차}**</span>', unsafe_allow_html=True)
##연차만 이용한 추천
def career_month_recommend(target_id, n_recommendations=2):
    # 대상 사용자 정보 확인
    target_user_info = data2.loc[data2['유저아이디'] == target_id, ['참가 직군', '개발_참가 분야', '연차_순서']].iloc[0]
    target_user_job = target_user_info['참가 직군']
    target_user_dev_field = target_user_info['개발_참가 분야']
    target_user_experience_order = target_user_info['연차_순서']

    # 필요한 직군 및 개발 분야 정의
    required_fields = []
    if target_user_job == '기획':
        required_fields = [('디자인', None), ('개발', '프론트엔드'), ('개발', '백엔드')]
    elif target_user_job == '디자인':
        required_fields = [('기획', None), ('개발', '프론트엔드'), ('개발', '백엔드')]
    elif target_user_job == '개발':
        if target_user_dev_field == '백엔드':
            required_fields = [('기획', None), ('디자인', None), ('개발', '프론트엔드')]
        elif target_user_dev_field == '프론트엔드':
            required_fields = [('기획', None), ('디자인', None), ('개발', '백엔드')]

    recommended_users = []
    for job, dev_field in required_fields:
        # 조건에 맞는 사용자 필터링
        if dev_field:
            filtered_users = data2[(data2['참가 직군'] == job) & (data2['개발_참가 분야'] == dev_field)]
        else:
            filtered_users = data2[data2['참가 직군'] == job]

        # 연차 차이 계산 및 가장 비슷한 사용자 추천
        experience_diff = abs(filtered_users['연차_순서'] - target_user_experience_order)
        recommended_indices = experience_diff.nsmallest(n_recommendations).index
        recommended_users.extend(filtered_users.loc[recommended_indices].to_dict('records'))

    # 추천된 사용자들을 데이터 프레임으로 변환
    recommended_df = pd.DataFrame(recommended_users)
    return recommended_df

## 참가시간만 이용한 추천
def participation_time_recommend(target_id, n_recommendations=2):
    # 대상 사용자 정보 확인
    target_user_info = data2.loc[data2['유저아이디'] == target_id, ['참가 직군', '개발_참가 분야', '총 투입 가능 시간']].iloc[0]
    target_user_job = target_user_info['참가 직군']
    target_user_dev_field = target_user_info['개발_참가 분야']
    target_user_available_time = target_user_info['총 투입 가능 시간']

    # 필요한 직군 및 개발 분야 정의
    required_fields = []
    if target_user_job == '기획':
        required_fields = [('디자인', None), ('개발', '프론트엔드'), ('개발', '백엔드')]
    elif target_user_job == '디자인':
        required_fields = [('기획', None), ('개발', '프론트엔드'), ('개발', '백엔드')]
    elif target_user_job == '개발':
        if target_user_dev_field == '백엔드':
            required_fields = [('기획', None), ('디자인', None), ('개발', '프론트엔드')]
        elif target_user_dev_field == '프론트엔드':
            required_fields = [('기획', None), ('디자인', None), ('개발', '백엔드')]

    recommended_users = []
    for job, dev_field in required_fields:
        # 조건에 맞는 사용자 필터링
        if dev_field:
            filtered_users = data2[(data2['참가 직군'] == job) & (data2['개발_참가 분야'] == dev_field)]
        else:
            filtered_users = data2[data2['참가 직군'] == job]

        # 시간 차이 계산 및 가장 가까운 사용자 추천
        time_diff = abs(filtered_users['총 투입 가능 시간'].astype(int) - int(target_user_available_time))
        recommended_indices = time_diff.nsmallest(n_recommendations).index
        recommended_users.extend(filtered_users.loc[recommended_indices].to_dict('records'))

    # 추천된 사용자들을 데이터 프레임으로 변환
    recommended_df = pd.DataFrame(recommended_users)
    return recommended_df
## 연차+참가시간을 고려한 추천
def comprehensive_recommend(target_id, n_recommendations=2):
    # 대상 사용자 정보 확인
    target_user_info = data2.loc[data2['유저아이디'] == target_id, ['참가 직군', '개발_참가 분야', '연차_순서', '총 투입 가능 시간']].iloc[0]
    target_user_job = target_user_info['참가 직군']
    target_user_dev_field = target_user_info['개발_참가 분야']
    target_user_vector = np.array([target_user_info['연차_순서'], target_user_info['총 투입 가능 시간']])

    # 필요한 직군 및 개발 분야 정의 (대상 사용자의 직군은 제외)
    required_fields = []
    if target_user_job == '기획':
        required_fields.extend([('디자인', None), ('개발', '프론트엔드'), ('개발', '백엔드')])
    elif target_user_job == '디자인':
        required_fields.extend([('기획', None), ('개발', '프론트엔드'), ('개발', '백엔드')])
    elif target_user_job == '개발':
        if target_user_dev_field == '백엔드':
            required_fields.extend([('기획', None), ('디자인', None), ('개발', '프론트엔드')])
        elif target_user_dev_field == '프론트엔드':
            required_fields.extend([('기획', None), ('디자인', None), ('개발', '백엔드')])

    recommended_users = []
    for job, dev_field in required_fields:
        # 조건에 맞는 사용자 필터링 (대상 사용자의 직군 제외)
        if dev_field:
            filtered_users = data2[(data2['참가 직군'] == job) & (data2['개발_참가 분야'] == dev_field) & (data2['유저아이디'] != target_id)]
        else:
            filtered_users = data2[(data2['참가 직군'] == job) & (data2['유저아이디'] != target_id)]

        # 사용자 벡터 생성 및 대상 사용자와의 거리 계산
        user_vectors = filtered_users[['연차_순서', '총 투입 가능 시간']].to_numpy()
        distances = np.linalg.norm(user_vectors - target_user_vector, axis=1)

        # 가장 가까운 사용자 추천
        recommended_indices = np.argsort(distances)[:n_recommendations]
        recommended_users.extend(filtered_users.iloc[recommended_indices].to_dict('records'))

    # 추천된 사용자들을 데이터 프레임으로 변환 및 중복 제거
    recommended_df = pd.DataFrame(recommended_users).drop_duplicates().head(n_recommendations * len(required_fields))
    return recommended_df




if target_user_id:
    try:
        st.subheader('연차만 고려한 추천')
        career_month=career_month_df=career_month_recommend(target_user_id,n_recommendation)
        if 참가직군=='기획':
            st.dataframe(career_month[['유저아이디','참가 직군','연차','총 투입 가능 시간','디자인_참가 분야','개발_참가 분야','커리어카드 URL']], width=1500,hide_index =True,use_container_width=True)
        elif 참가직군=='디자인':
            st.dataframe(career_month[['유저아이디','참가 직군','연차','총 투입 가능 시간','기획_참가 분야','개발_참가 분야','커리어카드 URL']], width=1500,hide_index =True,use_container_width=True)
        else:
            st.dataframe(career_month[['유저아이디','참가 직군','연차','총 투입 가능 시간','기획_참가 분야','디자인_참가 분야','개발_참가 분야','커리어카드 URL']], width=1500,hide_index =True,use_container_width=True)
        st.subheader('참가시간만 고려한 추천')
        participation=participation_time_recommend(target_user_id,n_recommendation)
        if 참가직군=='기획':
            st.dataframe(participation[['유저아이디','참가 직군','연차','총 투입 가능 시간','디자인_참가 분야','개발_참가 분야','커리어카드 URL']], width=1500,hide_index =True,use_container_width=True)
        elif 참가직군=='디자인':
            st.dataframe(participation[['유저아이디','참가 직군','연차','총 투입 가능 시간','기획_참가 분야','개발_참가 분야','커리어카드 URL']], width=1500,hide_index =True,use_container_width=True)
        else:
            st.dataframe(participation[['유저아이디','참가 직군','연차','총 투입 가능 시간','기획_참가 분야','디자인_참가 분야','개발_참가 분야','커리어카드 URL']], width=1500,hide_index =True,use_container_width=True)
        st.subheader('연차+참가시간을 고려한 추천')
        comprehensive=comprehensive_recommend(target_user_id,n_recommendation)
        if 참가직군=='기획':
            st.dataframe(comprehensive[['유저아이디','참가 직군','연차','총 투입 가능 시간','디자인_참가 분야','개발_참가 분야','커리어카드 URL']], width=1500,hide_index =True,use_container_width=True)
        elif 참가직군=='디자인':
            st.dataframe(comprehensive[['유저아이디','참가 직군','연차','총 투입 가능 시간','기획_참가 분야','개발_참가 분야','커리어카드 URL']], width=1500,hide_index =True,use_container_width=True)
        else:
            st.dataframe(comprehensive[['유저아이디','참가 직군','연차','총 투입 가능 시간','기획_참가 분야','디자인_참가 분야','개발_참가 분야','커리어카드 URL']], width=1500,hide_index =True,use_container_width=True)
    except:
        st.error('해당하는 ID가 없습니다.')
else:
    st.write('왼쪽 유저 리스트를 보시고 유저 ID를 입력해주세요')
