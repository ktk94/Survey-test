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
    target_user_job = data2.loc[data['유저아이디'] == target_id, '참가 직군'].values[0]
    target_user_experience_order = data2.loc[data['유저아이디'] == target_id, '연차_순서'].values[0]
    
    if target_user_job == '기획':
        required_jobs = ['디자인', '개발']
    elif target_user_job == '디자인':
        required_jobs = ['기획', '개발']
    else:  # 개발자인 경우
        required_jobs = ['기획', '디자인', '개발']  # 개발자도 포함해야 하는 경우를 고려
        
    filtered_users_by_job = data2[data2['참가 직군'].isin(required_jobs)]
    
    recommended_users_by_job_and_experience = {}
    for job in required_jobs:
        job_specific_users = data2[(data2['참가 직군'] == job) & (data2['유저아이디'] != target_id)]
        job_specific_distances = abs(job_specific_users['연차_순서'] - target_user_experience_order)
        recommended_indices = job_specific_distances.nsmallest(n_recommendations).index
        recommended_users = job_specific_users.loc[recommended_indices]
        recommended_users_by_job_and_experience[job] = recommended_users

    # 각 직군별 추천된 사용자들을 데이터 프레임으로 변환
    recommended_df = pd.concat(recommended_users_by_job_and_experience.values(), ignore_index=True)
    return recommended_df
## 참가시간만 이용한 추천
def participation_time_recommend(target_id, n_recommendations=2):
    # 대상 사용자의 직군과 총 투입 가능 시간 확인
    target_user_job = data2.loc[data2['유저아이디'] == target_id, '참가 직군'].values[0]
    target_user_available_time = data2.loc[data2['유저아이디'] == target_id, '총 투입 가능 시간'].values[0]

    # 필요한 직군 정의
    if target_user_job == '기획':
        required_jobs = ['디자인', '개발']
    elif target_user_job == '디자인':
        required_jobs = ['기획', '개발']
    else:  # 개발자인 경우
        required_jobs = ['기획', '디자인', '개발']

    recommended_users_by_job_and_time = {}
    for job in required_jobs:
        job_specific_users = data2[(data2['참가 직군'] == job) & (data2['유저아이디'] != target_id)]
        job_specific_time_diff = abs(job_specific_users['총 투입 가능 시간'].astype(int) - int(target_user_available_time))
        recommended_indices = job_specific_time_diff.nsmallest(n_recommendations).index
        recommended_users = job_specific_users.loc[recommended_indices,]
        recommended_users_by_job_and_time[job] = recommended_users

    # 각 직군별 추천된 사용자들을 데이터 프레임으로 변환
    recommended_df = pd.concat(recommended_users_by_job_and_time.values(), ignore_index=True)
    return recommended_df
## 연차+참가시간을 고려한 추천
def comprehensive_recommend(target_id, n_recommendations=2):
    # 대상 사용자의 직군, 연차 순서, 총 투입 가능 시간 확인
    target_user_job = data2.loc[data2['유저아이디'] == target_id, '참가 직군'].values[0]
    target_user_experience_order = data2.loc[data2['유저아이디'] == target_id, '연차_순서'].values[0]
    target_user_available_time = data2.loc[data2['유저아이디'] == target_id, '총 투입 가능 시간'].values[0]

    # 대상 사용자의 벡터 생성
    target_user_vector = np.array([target_user_experience_order, target_user_available_time])

    # 필요한 직군 정의
    if target_user_job == '기획':
        required_jobs = ['디자인', '개발']
    elif target_user_job == '디자인':
        required_jobs = ['기획', '개발']
    else:  # 개발자인 경우
        required_jobs = ['기획', '디자인', '개발']

    recommended_users_by_job_and_comprehensive = {}
    for job in required_jobs:
        job_specific_users = data2[(data2['참가 직군'] == job) & (data2['유저아이디'] != target_id)]
        job_specific_vectors = job_specific_users[['연차_순서', '총 투입 가능 시간']].to_numpy()
        distances = np.linalg.norm(job_specific_vectors - target_user_vector, axis=1)
        recommended_indices = np.argsort(distances)[:n_recommendations]
        recommended_users = job_specific_users.iloc[recommended_indices, :]
        recommended_users_by_job_and_comprehensive[job] = recommended_users

    # 각 직군별 추천된 사용자들을 데이터 프레임으로 변환
    recommended_df = pd.concat(recommended_users_by_job_and_comprehensive.values(), ignore_index=True)
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
