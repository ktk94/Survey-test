import streamlit as st
import subfunction as sf

def page2(user_name, position, ans_list):

    st.title('응답 내용')
    df=sf.get_df(ans_list)
    st.dataframe(df)

    st.title("결과")
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["요약", "서비스 기획", "데이터 문해", "리서치", "프로젝트 관리", "프로덕트 관리"])

    with tab1:
        sf.summary_tab(df, user_name, position)
    
    with tab2:
        sf.tab(df, '서비스 기획')

    with tab3:
        sf.tab(df, '데이터 문해')
        
    with tab4:
        sf.tab(df, '리서치')

    with tab5:
        sf.tab(df, '프로젝트 관리')
    
    with tab6:
        sf.tab(df, '프로덕트 관리')

def main():
    try:
        page2(user_name=st.session_state.user_name,
            position=st.session_state.position,
            ans_list=st.session_state.ans_list
            )
    except:
        st.warning('설문에 응답한 뒤 결과를 확인해주세요.')

if __name__ == "__main__":
    main()

