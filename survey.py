import pandas as pd
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

import subfunction as sf


def page1():
    ##최초 부분
    st.header('비사이드 역량진단')
                    
    col1,col2=st.columns(2)
    with col1:
        user_name=st.text_input('이름을 입력하시고, Enter키를 눌러주세요.')
    with col2:
        position=st.radio('직무를 선택해주세요',('PO/PM','서비스 기획'),horizontal=False)
    if len(user_name)!=0:
        st.write(f'안녕하세요 {user_name}님! 비사이드 역량진단을 위해 아래 설문에 답해주세요!')
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
            st.markdown(f"<span style='font-size:24px;font-family:Arial'>제출해주셔서 감사합니다.</span>", unsafe_allow_html=True)
            ans_dict = {
                'user_name' : user_name,
                'position' : position,
                'ans_list' : ans_list
            }
            page2(ans_dict)

def page2(ans_dict):
    user_name = ans_dict['user_name']
    position = ans_dict['position']
    ans_list = ans_dict['ans_list']

    st.title('응답 내용')
    df=sf.get_df(ans_list)
    st.dataframe(df)

    st.title("결과")
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["요약", "서비스 기획", "데이터 문해", "리서치", "프로젝트 관리", "프로덕트 관리"])

    with tab1:
        summary_tab(df, user_name, position)
    
    with tab2:
        tab(df, '서비스 기획')

    with tab3:
        tab(df, '데이터 문해')
        
    with tab4:
        tab(df, '리서치')

    with tab5:
        tab(df, '프로젝트 관리')
    
    with tab6:
        tab(df, '프로덕트 관리')

def summary_tab(df, user_name, position):
    # 채용공고 수, 역량 개수, 유저 데이터 수, 유저 데이터 평균
    data={
        'PO/PM' : ['2,377', '25', '237', '7'],
        '서비스 기획자' : ['4,000', '30', '300', '10']
    }
    ability_cnt=len(df[df['응답']=='Y'])

    st.subheader("요약")
    st.write(f"""
        채용공고 `{data[position][0]}`개 분석 결과, `{position}`에게 필요한 주요 역량은 `{data[position][1]}`개 입니다.\n
        `{user_name}`님은 이중 `{ability_cnt}`개 역량을 가지고 있네요.\n
        동료 `{position}` `{data[position][2]}`명의 평균과 비교했을 때 `{abs(ability_cnt-int(data[position][3]))}`개 `{'많은' if ability_cnt-int(data[position][3])>0 else '적은'}` 수준이에요.
        """)

    st.subheader("내 강점과 약점은?")
    strength, weekness=sf.get_user_category(df)
    if len(strength)>1 & len(weekness)>1 :
        st.write(f"""
            채용공고와 동료의 역량 진단 결과를 종합적으로 분석했을 때\n
            {user_name} 님은 `{(', ').join(strength)}` 역량이 뛰어나네요!\n
            `{(', ').join(weekness)}` 역량을 키우면 더욱 경쟁력이 생길 거예요.
        """)

    elif len(strength)>1:
        st.write(f"""
            채용공고와 동료의 역량 진단 결과를 종합적으로 분석했을 때\n
            `{user_name}` 님은 `{(', ').join(strength)}` 역량이 뛰어나네요!
        """)
    elif len(weekness)>1:
        st.write(f"""
            채용공고와 동료의 역량 진단 결과를 종합적으로 분석했을 때\n
            `{(', ').join(weekness)}` 역량을 키우면 더욱 경쟁력이 생길 거예요.
        """)

    st.write('자세한 진단 결과는 다른 탭을 눌러 확인해보세요.')

    graph = sf.get_graph(df)
    st.graphviz_chart(graph)
    

def tab(df, category):
    disc={
        '서비스 기획' : '`서비스 기획` 역량은 서비스 구현에 필요한 기능, 정책, 화면 등을 상세히 설계할 수 있는 것을 뜻해요.',
        '데이터 문해' : '`데이터 문해` 역량은 어쩌구 저쩌구',
        '리서치' : '`리서치` 역량은 어쩌구 저쩌구',
        '프로젝트 관리' : '`프로젝트 관리` 역량은 어쩌구 저쩌구',
        '프로덕트 관리' : '`프로덕트 관리` 역량은 어쩌구 저쩌구',
    }
    ability={
        '서비스 기획' : ['웹 서비스 기획', 'UX/UI 기획'],
        '데이터 문해' : ['데이터 분석', '데이터 기반 의사결정'],
        '리서치' : ['A/B 테스트', '사용자 조사'],
        '프로젝트 관리' : ['유관부서와 협업', '프로젝트 리딩'], 
        '프로덕트 관리' : ['서비스 운영', '서비스 출시']
    }

    st.subheader(category)
    st.write(disc[category])
    barchart1=sf.get_barchart(df, category, '채용공고')
    st.pyplot(barchart1)

    st.subheader('다른 사람과 비교했을 때 나는?')
    st.write(f'역량 진단을 진행한 동료가 가지고 있는 상위 2개 역량은\n `{ability[category][0]}`, `{ability[category][1]}` 입니다.')
    barchart2=sf.get_barchart(df, category, '유저 데이터')
    st.pyplot(barchart2)


def main():
    page1()

if __name__ == "__main__":
    main()


