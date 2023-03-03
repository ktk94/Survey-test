import pandas as pd
import graphviz
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 그래프
def get_graph(df):
    graph = graphviz.Graph()
    # node
    graph.node('PO/PM', shape='doubleoctagon', style='filled', color='black', fontcolor='white', width='5')

    graph.node('서비스 기획', shape='invhouse', style='filled', color='hotpink', fontcolor='white', width='2')
    graph.node('데이터 문해', shape='invhouse', style='filled', color='orange1', fontcolor='white', width='2')
    graph.node('리서치', shape='invhouse', style='filled', color='orangered1', fontcolor='white', width='2')
    graph.node('프로젝트 관리', shape='invhouse', style='filled', color='lightseagreen', fontcolor='white', width='2')
    graph.node('프로덕트 관리', shape='invhouse', style='filled', color='royalblue1', fontcolor='white', width='2')

    graph.node('앱 서비스 기획', shape='rect', 
            style='filled' if (df[df['경험']=='앱 서비스 기획']['응답']=='Y').bool() else 'none', 
            fontcolor='white' if (df[df['경험']=='앱 서비스 기획']['응답']=='Y').bool() else 'hotpink',
            color='hotpink', width='1.7')
    graph.node('웹 서비스 기획', shape='rect', 
            style='filled' if (df[df['경험']=='웹 서비스 기획']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='웹 서비스 기획']['응답']=='Y').bool() else 'hotpink',
            color='hotpink', width='1.7')
    graph.node('UX/UI 기획', shape='rect', 
            style='filled' if (df[df['경험']=='UX/UI 기획']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='UX/UI 기획']['응답']=='Y').bool() else 'hotpink',
            color='hotpink', width='1.7')
    graph.node('요구사항정의서 작성', shape='rect', 
            style='filled' if (df[df['경험']=='요구사항정의서 작성']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='요구사항정의서 작성']['응답']=='Y').bool() else 'hotpink',
            color='hotpink', width='1.7')
    graph.node('백오피스 기획', shape='rect', 
            style='filled' if (df[df['경험']=='백오피스 기획']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='백오피스 기획']['응답']=='Y').bool() else 'hotpink',
            color='hotpink', width='1.7')

    graph.node('데이터 분석', shape='rect', 
            style='filled' if (df[df['경험']=='데이터 분석']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='데이터 분석']['응답']=='Y').bool() else 'orange1',
            color='orange1', width='1.7')
    graph.node('데이터 기반 의사결정', shape='rect', 
            style='filled' if (df[df['경험']=='데이터 기반 의사결정']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='데이터 기반 의사결정']['응답']=='Y').bool() else 'orange1',
            color='orange1', width='1.7')
    graph.node('가설 검정', shape='rect', 
            style='filled' if (df[df['경험']=='가설 검정']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='가설 검정']['응답']=='Y').bool() else 'orange1',
            color='orange1', width='1.7')
    graph.node('데이터 시각화', shape='rect', 
            style='filled' if (df[df['경험']=='데이터 시각화']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='데이터 시각화']['응답']=='Y').bool() else 'orange1',
            color='orange1', width='1.7')
    graph.node('데이터 전처리', shape='rect', 
            style='filled' if (df[df['경험']=='데이터 전처리']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='데이터 전처리']['응답']=='Y').bool() else 'orange1',
            color='orange1', width='1.7')
    graph.node('통계학 이해', shape='rect', 
            style='filled' if (df[df['경험']=='통계학 이해']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='통계학 이해']['응답']=='Y').bool() else 'orange1',
            color='orange1', width='1.7')

    graph.node('정량/정성 분석', shape='rect', 
            style='filled' if (df[df['경험']=='정량/정성 분석']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='정량/정성 분석']['응답']=='Y').bool() else 'orangered1',
            color='orangered1', width='1.7')
    graph.node('시장 조사', shape='rect', 
            style='filled' if (df[df['경험']=='시장 조사']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='시장 조사']['응답']=='Y').bool() else 'orangered1',
            color='orangered1', width='1.7')
    graph.node('A/B 테스트', shape='rect', 
            style='filled' if (df[df['경험']=='A/B 테스트']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='A/B 테스트']['응답']=='Y').bool() else 'orangered1',
            color='orangered1', width='1.7')
    graph.node('사용자 조사', shape='rect', 
            style='filled' if (df[df['경험']=='사용자 조사']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='사용자 조사']['응답']=='Y').bool() else 'orangered1',
            color='orangered1', width='1.7')

    graph.node('애자일', shape='rect', 
            style='filled' if (df[df['경험']=='애자일']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='애자일']['응답']=='Y').bool() else 'lightseagreen',
            color='lightseagreen', width='1.7')
    graph.node('프로젝트 관리1', shape='rect', 
            style='filled' if (df[df['경험']=='프로젝트 관리']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='프로젝트 관리']['응답']=='Y').bool() else 'lightseagreen',
            color='lightseagreen', width='1.7')
    graph.node('유관부서와 협업', shape='rect', 
            style='filled' if (df[df['경험']=='유관부서와 협업']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='유관부서와 협업']['응답']=='Y').bool() else 'lightseagreen',
            color='lightseagreen', width='1.7')
    graph.node('프로젝트 리딩', shape='rect', 
            style='filled' if (df[df['경험']=='유관부서와 협업']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='유관부서와 협업']['응답']=='Y').bool() else 'lightseagreen',
            color='lightseagreen', width='1.7')

    graph.node('서비스 운영', shape='rect', 
            style='filled' if (df[df['경험']=='서비스 운영']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='서비스 운영']['응답']=='Y').bool() else 'royalblue1',
            color='royalblue1', width='1.7')
    graph.node('서비스 출시', shape='rect', 
            style='filled' if (df[df['경험']=='서비스 출시']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='서비스 출시']['응답']=='Y').bool() else 'royalblue1',
            color='royalblue1', width='1.7')
    graph.node('서비스 고도화', shape='rect', 
            style='filled' if (df[df['경험']=='서비스 고도화']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='서비스 고도화']['응답']=='Y').bool() else 'royalblue1',
            color='royalblue1', width='1.7')
    graph.node('사업 기획', shape='rect', 
            style='filled' if (df[df['경험']=='사업 기획']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='사업 기획']['응답']=='Y').bool() else 'royalblue1',
            color='royalblue1', width='1.7')
    graph.node('사업 개발', shape='rect', 
            style='filled' if (df[df['경험']=='사업 개발']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='사업 개발']['응답']=='Y').bool() else 'royalblue1',
            color='royalblue1', width='1.7')
    graph.node('서비스 전략 수립', shape='rect', 
            style='filled' if (df[df['경험']=='서비스 전략 수립']['응답']=='Y').bool() else 'none',
            fontcolor='white' if (df[df['경험']=='서비스 전략 수립']['응답']=='Y').bool() else 'royalblue1',
            color='royalblue1', width='1.7')

    # edge
    graph.edge('PO/PM', '서비스 기획', color='lightgrey')
    graph.edge('PO/PM', '데이터 문해', color='lightgrey')
    graph.edge('PO/PM', '리서치', color='lightgrey')
    graph.edge('PO/PM', '프로젝트 관리', color='lightgrey')
    graph.edge('PO/PM', '프로덕트 관리', color='lightgrey')

    graph.edge('서비스 기획', '앱 서비스 기획', color='lightgrey')
    graph.edge('앱 서비스 기획', '웹 서비스 기획', color='lightgrey')
    graph.edge('웹 서비스 기획', 'UX/UI 기획', color='lightgrey')
    graph.edge('UX/UI 기획', '요구사항정의서 작성', color='lightgrey')
    graph.edge('요구사항정의서 작성', '백오피스 기획', color='lightgrey')

    graph.edge('데이터 문해', '데이터 분석', color='lightgrey')
    graph.edge('데이터 분석', '데이터 기반 의사결정', color='lightgrey')
    graph.edge('데이터 기반 의사결정', '가설 검정', color='lightgrey')
    graph.edge('가설 검정', '데이터 시각화', color='lightgrey')
    graph.edge('데이터 시각화', '데이터 전처리', color='lightgrey')
    graph.edge('데이터 전처리', '통계학 이해', color='lightgrey')

    graph.edge('리서치', '정량/정성 분석', color='lightgrey')
    graph.edge('정량/정성 분석', '시장 조사', color='lightgrey')
    graph.edge('시장 조사', 'A/B 테스트', color='lightgrey')
    graph.edge('A/B 테스트', '사용자 조사', color='lightgrey')

    graph.edge('프로젝트 관리', '애자일', color='lightgrey')
    graph.edge('애자일', '프로젝트 관리1', color='lightgrey')
    graph.edge('프로젝트 관리1', '유관부서와 협업', color='lightgrey')
    graph.edge('유관부서와 협업', '프로젝트 리딩', color='lightgrey')

    graph.edge('프로덕트 관리', '서비스 운영', color='lightgrey')
    graph.edge('서비스 운영', '서비스 출시', color='lightgrey')
    graph.edge('서비스 출시', '서비스 고도화', color='lightgrey')
    graph.edge('서비스 고도화', '사업 기획', color='lightgrey')
    graph.edge('사업 기획', '사업 개발', color='lightgrey')
    graph.edge('사업 개발', '서비스 전략 수립', color='lightgrey')

    return graph

# 바 차트
def get_barchart(df, category, type):
#     plt.rcParams['font.family'] ='Malgun Gothic'
#     plt.rcParams['axes.unicode_minus'] =False    
    path='MALGUN.TTF'
    font=fm.FontProperties(fname=path).get_name()
    plt.rcParams['font.family'] = font
    plt.rcParams['axes.unicode_minus'] =False

    df_subset = df[df['카테고리']==category][['경험','채용공고 %', '유저 데이터 %', 'color']]

    fig, ax = plt.subplots(figsize=(4,4))

    if type=="채용공고":
        df_subset=df_subset.sort_values(by='채용공고 %', ascending=False)
        x_value=df_subset['경험'].tolist()
        y_value=df_subset['채용공고 %'].tolist()
        c_value=df_subset['color'].tolist()
    elif type=="유저 데이터":
        df_subset=df_subset.sort_values(by='유저 데이터 %', ascending=False)
        x_value=df_subset['경험'].tolist()
        y_value=df_subset['유저 데이터 %'].tolist()
        c_value=df_subset['color'].tolist()

    x_value.reverse()
    y_value.reverse()
    c_value.reverse()
    plt.barh(x_value, y_value, color=c_value)


    return fig

# 데이터 프레임 처리
def get_df(ans_list):
    df = pd.DataFrame(
        data=[
            ['서비스 기획', '앱 서비스 기획', 138, 61],
            ['서비스 기획', '웹 서비스 기획', 176, 86],
            ['서비스 기획', 'UX/UI 기획', 162, 49],
            ['서비스 기획', '요구사항정의서 작성', 36, 0],
            ['서비스 기획', '백오피스 기획', 29, 0],
            ['데이터 문해', '데이터 분석', 613, 80],
            ['데이터 문해', '데이터 기반 의사결정', 359, 78],
            ['데이터 문해', '가설 검정', 116, 57],
            ['데이터 문해', '데이터 시각화', 0, 0],
            ['데이터 문해', '데이터 전처리', 0, 0],
            ['데이터 문해', '통계학 이해', 39, 11],
            ['리서치', '정량/정성 분석', 64, 24],
            ['리서치', '시장 조사', 39, 8],
            ['리서치', 'A/B 테스트', 51, 35],
            ['리서치', '사용자 조사', 43, 32],
            ['프로젝트 관리', '애자일', 439, 69],
            ['프로젝트 관리', '프로젝트 관리', 350, 61],
            ['프로젝트 관리', '유관부서와 협업', 165, 99],
            ['프로젝트 관리', '프로젝트 리딩', 133, 80],
            ['프로덕트 관리', '서비스 운영', 482, 89],
            ['프로덕트 관리', '서비스 출시', 323, 71],
            ['프로덕트 관리', '서비스 고도화', 199, 69],
            ['프로덕트 관리', '사업 기획', 77, 43],
            ['프로덕트 관리', '사업 개발', 75, 15],
            ['프로덕트 관리', '서비스 전략 수립', 54, 63]
        ],
        columns=['카테고리','경험','채용공고 수','유저 데이터 수']
    )
    df['채용공고 %'] = round(df['채용공고 수']/2377*100, 2)
    df['유저 데이터 %'] = round(df['유저 데이터 수']/237*100, 2)
    df['응답'] = ans_list
    df['color'] = df['응답'].apply(lambda x: 'dodgerblue' if x=='Y' else 'gainsboro')

    return df

def get_user_category(df):
    ability={
        '서비스 기획' : ['웹 서비스 기획', 'UX/UI 기획'],
        '데이터 문해' : ['데이터 분석', '데이터 기반 의사결정'],
        '리서치' : ['A/B 테스트', '사용자 조사'],
        '프로젝트 관리' : ['유관부서와 협업', '프로젝트 리딩'], 
        '프로덕트 관리' : ['서비스 운영', '서비스 출시']
    }

    strength=[]
    if (df[df['경험']==ability['서비스 기획'][0]]['응답']=='Y').bool() & (df[df['경험']==ability['서비스 기획'][1]]['응답']=='Y').bool():
        strength.append('서비스 기획')
    if (df[df['경험']==ability['데이터 문해'][0]]['응답']=='Y').bool() & (df[df['경험']==ability['데이터 문해'][1]]['응답']=='Y').bool():
        strength.append('데이터 문해')
    if (df[df['경험']==ability['리서치'][0]]['응답']=='Y').bool() & (df[df['경험']==ability['리서치'][1]]['응답']=='Y').bool():
        strength.append('리서치')
    if (df[df['경험']==ability['프로젝트 관리'][0]]['응답']=='Y').bool() & (df[df['경험']==ability['프로젝트 관리'][1]]['응답']=='Y').bool():
        strength.append('프로젝트 관리')
    if (df[df['경험']==ability['프로덕트 관리'][0]]['응답']=='Y').bool() & (df[df['경험']==ability['프로덕트 관리'][1]]['응답']=='Y').bool():
        strength.append('프로덕트 관리')

    weekness=[]
    if (df[df['경험']==ability['서비스 기획'][0]]['응답']=='N').bool() & (df[df['경험']==ability['서비스 기획'][1]]['응답']=='N').bool():
        weekness.append('서비스 기획')
    if (df[df['경험']==ability['데이터 문해'][0]]['응답']=='N').bool() & (df[df['경험']==ability['데이터 문해'][1]]['응답']=='N').bool():
        weekness.append('데이터 문해')
    if (df[df['경험']==ability['리서치'][0]]['응답']=='N').bool() & (df[df['경험']==ability['리서치'][1]]['응답']=='N').bool():
        weekness.append('리서치')
    if (df[df['경험']==ability['프로젝트 관리'][0]]['응답']=='N').bool() & (df[df['경험']==ability['프로젝트 관리'][1]]['응답']=='N').bool():
        weekness.append('프로젝트 관리')
    if (df[df['경험']==ability['프로덕트 관리'][0]]['응답']=='N').bool() & (df[df['경험']==ability['프로덕트 관리'][1]]['응답']=='N').bool():
        weekness.append('프로덕트 관리')
    
    return strength, weekness
    