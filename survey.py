import pandas as pd
import streamlit as st
import numpy as np
##최초 부분
st.header('비사이드 역량진단')
def main():
    if 'name1' not in st.session_state:
        st.title('첫 번째 페이지')
        col1,col2=st.columns(2)
        with col1:
            name1=st.text_input('이름을 입력하시고, Enter키를 눌러주세요.')
        with col2:
            position=st.radio('직무를 선택해주세요',('PO/PM','서비스 기획'),horizontal=False)
        if len(name1)!=0:
            st.write(f'안녕하세요 {name1}님! 비사이드 역량진단을 위해 아래 설문에 답해주세요!')
            if st.button('다음 페이지'):
                st.session_state['name1'] = name1
                st.session_state['position'] = position   
                 
col1,col2=st.columns(2)
with col1:
    name1=st.text_input('이름을 입력하시고, Enter키를 눌러주세요.')
with col2:
    position=st.radio('직무를 선택해주세요',('PO/PM','서비스 기획'),horizontal=False)
if len(name1)!=0:
    st.write(f'안녕하세요 {name1}님! 비사이드 역량진단을 위해 아래 설문에 답해주세요!')
else:
    st.warning('이름을 입력하고 직무를 선택해주세요!')
    st.stop()
choice=('응답선택','Y','N')
with st.form("설문"):
    coll1,coll2=st.columns(2)
    with coll1:
        radio1=st.selectbox(' 웹 서비스 기획',choice)
        radio2=st.selectbox(' UX/UI 기획',choice)
        radio3=st.selectbox(' 앱 서비스 기획',choice)
        radio4=st.selectbox(' 요구사항 정의서 작성',choice)
        radio5=st.selectbox(' 백오피스 기획',choice)
        radio6=st.selectbox(' 데이터 분석',choice)
        radio7=st.selectbox(' 데이터 기반 의사결정',choice)
        radio8=st.selectbox(' 가설 검증',choice)
        radio9=st.selectbox(' 지표 관리',choice)
        radio10=st.selectbox(' 통계학 이해',choice)
        radio11=st.selectbox(' 데이터 전처리',choice)
        radio12=st.selectbox(' 정량/정성 분석',choice)
        radio13=st.selectbox(' A/B 테스트',choice)           
    with coll2:
        radio14=st.selectbox(' 사용자 조사',choice)
        radio15=st.selectbox(' 시장 조사',choice)
        radio16=st.selectbox(' 애자일',choice)
        radio17=st.selectbox(' 프로젝트 관리',choice)
        radio18=st.selectbox(' 유관 부서와 협업',choice)
        radio19=st.selectbox(' 프로젝트 리딩',choice)
        radio20=st.selectbox(' 서비스 운영',choice)
        radio21=st.selectbox(' 서비츠 출시',choice)
        radio22=st.selectbox(' 서비스 고도화',choice)
        radio23=st.selectbox(' 사업 기획',choice)
        radio24=st.selectbox(' 사업 개발',choice)
        radio25=st.selectbox(' 서비스 전략 수립',choice)
    button1=st.form_submit_button('Submit')


if button1:
    user_list=[radio1,radio2,radio3,radio4,radio5,radio6,radio7,radio8,radio9,radio10,radio11,radio12,radio13,radio14,radio15,radio16,radio17,radio18,radio19,radio20,radio21,radio22,radio23,radio24,radio25]
    if '응답선택' in user_list:
        st.warning('응답하시지 않은 질문이 있습니다')
    else:
        st.markdown(f"<span style='font-size:24px;font-family:Arial'>제출해주셔서 감사합니다.</span>", unsafe_allow_html=True)
