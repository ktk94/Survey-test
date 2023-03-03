import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title='기획자 역량 진단', initial_sidebar_state="collapsed")

import time

def page1():

    if ('user_name' in st.session_state) & ('position' in st.session_state) & ('ans_list' in st.session_state):
        st.subheader("다시 진단하시겠어요?")
        if st.button("다시 진단하기"):
            del st.session_state['user_name']
            del st.session_state['position']
            del st.session_state['ans_list']
            page1()

    else: 
        st.header('비사이드 역량진단')
                    
        col1,col2=st.columns(2)
        with col1:
            user_name=st.text_input('이름을 입력하시고, Enter키를 눌러주세요.')
        with col2:
            position=st.radio('직무를 선택해주세요',('PO/PM','서비스 기획'),horizontal=False)
        if len(user_name)!=0:
            st.write(f"""안녕하세요 {user_name}님!
            \n비사이드 역량진단을 위해 아래 설문에 답해주세요!""")
        else:
            st.warning('이름을 입력하고 직무를 선택해주세요!')
            st.stop()
        
        with st.form("설문"):
            choice=('응답선택','Y','N')
            col3,col4=st.columns(2)
            with col3:
                # st.subheader("서비스 기획")
                ans1=st.selectbox(' 앱 서비스 기획',choice)
                ans2=st.selectbox(' 웹 서비스 기획',choice)
                ans3=st.selectbox(' UX/UI 기획',choice)
                ans4=st.selectbox(' 요구사항 정의서 작성',choice)
                ans5=st.selectbox(' 백오피스 기획',choice)

                # st.subheader("데이터 문해")
                ans6=st.selectbox(' 데이터 분석',choice)
                ans7=st.selectbox(' 데이터 기반 의사결정',choice)
                ans8=st.selectbox(' 가설 검증',choice)
                ans9=st.selectbox(' 데이터 시각화',choice)
                ans10=st.selectbox(' 데이터 전처리',choice)
                ans11=st.selectbox(' 통계학 이해',choice)

                # st.subheader("리서치")
                ans12=st.selectbox(' 정량/정성 분석',choice)
                ans13=st.selectbox(' 시장 조사',choice)  
                
                
            with col4:
                ans14=st.selectbox(' A/B 테스트',choice)
                ans15=st.selectbox(' 사용자 조사',choice) 
                
                # st.subheader("프로젝트 관리")
                ans16=st.selectbox(' 애자일',choice)
                ans17=st.selectbox(' 프로젝트 관리',choice)
                ans18=st.selectbox(' 유관 부서와 협업',choice)
                ans19=st.selectbox(' 프로젝트 리딩',choice)

                # st.subheader("프로덕트 관리")
                ans20=st.selectbox(' 서비스 운영',choice)
                ans21=st.selectbox(' 서비츠 출시',choice)
                ans22=st.selectbox(' 서비스 고도화',choice)
                ans23=st.selectbox(' 사업 기획',choice)
                ans24=st.selectbox(' 사업 개발',choice)
                ans25=st.selectbox(' 서비스 전략 수립',choice)
                
            submit_button=st.form_submit_button('제출')

        if submit_button:
            ans_list=[ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10,
                    ans11,ans12,ans13,ans14,ans15,ans16,ans17,ans18,ans19,ans20,
                    ans21,ans22,ans23,ans24,ans25]
            if '응답선택' in ans_list:
                st.warning('응답하시지 않은 질문이 있습니다')
            else:
                # Initialization
                if 'user_name' not in st.session_state:
                    st.session_state['user_name'] = user_name
                if 'position' not in st.session_state:
                    st.session_state['position'] = position
                if 'ans_list' not in st.session_state:
                    st.session_state['ans_list'] = ans_list

                # Retry
                if 'user_name' in st.session_state:
                    del st.session_state['user_name']
                    st.session_state['user_name'] = user_name
                if 'position' in st.session_state:
                    del st.session_state['position']
                    st.session_state['position'] = position
                if 'ans_list' in st.session_state:
                    del st.session_state['ans_list']
                    st.session_state['ans_list'] = ans_list

                with st.balloons():
                    time.sleep(3)

                switch_page("result")


def main():
    page1()

if __name__ == "__main__":
    main()


