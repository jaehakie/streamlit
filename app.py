import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import datetime
plt.rcParams['font.family'] = 'Malgun Gothic'

# 첫 번째 서비스 구현
def service_1():
    in_person_in_buy = pd.read_csv("C:/Users/SEC/Desktop/충청남도 데이터포털 올담 데이터 활용 시각화 경진대회/충남 고객기준 충남 소비 현황.csv", encoding='cp949')
    ch_list = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시',
           '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군']
    menu_1 = st.sidebar.selectbox("시군구명 1", ch_list)
    menu_2 = st.sidebar.selectbox("시군구명 2", ch_list)
    selected_year = st.sidebar.selectbox("년도", ['2019', '2020', '2021', '2022'])

    st.title('충청남도 거주자의 충청남도 소비 현황 분석')
    st.text('마지막 새로고침 시간 : ' + str(datetime.datetime.now()))

    in_person_in_buy['기준연월'] = in_person_in_buy['기준연월'].astype(str).apply(lambda x: f'{x[:4]}년 {x[4:]}월')
    in_person_in_buy['평균이용금액'] = (in_person_in_buy['전체이용금액'] / in_person_in_buy['전체이용건수']).apply(lambda x: round(x))
    in_person_in_buy = in_person_in_buy.groupby(['기준연월', '시군구명']).mean().reset_index()
    in_person_in_buy_pivot = in_person_in_buy.pivot(index='기준연월', columns='시군구명', values='평균이용금액')
    
    if st.button('전체 데이터 보기'):
        st.write(in_person_in_buy_pivot)
    else:
        st.write("")

    fig, ax = plt.subplots(figsize=(15, 9))
    start_index = (int(selected_year) - 2019) * 12
    end_index = start_index + 12
    for i, item in enumerate(ch_list):
        if menu_1 == item or menu_2 == item:
            ax.plot(in_person_in_buy_pivot.index[start_index:end_index], in_person_in_buy_pivot[start_index:end_index][item], label=item, alpha=1)
            if st.checkbox(item):
                st.write(in_person_in_buy[in_person_in_buy['시군구명'] == item].set_index(['기준연월'])[start_index:end_index])
        else:
            ax.plot(in_person_in_buy_pivot.index[start_index:end_index], in_person_in_buy_pivot[start_index:end_index][item], label=item, alpha=0.1)

    ax.set_xlabel('기준 연월')
    ax.set_ylabel('평균 소비 금액')
    ax.set_title('월별 평균소비금액 변화 추이 지역별 비교')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    st.pyplot(fig)

# 두 번째 서비스 구현
def service_2():
    in_person_out_buy = pd.read_csv("C:/Users/SEC/Desktop/충청남도 데이터포털 올담 데이터 활용 시각화 경진대회/충남 고객기준 충남외 소비 현황.csv", encoding='cp949')
    ch_list = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시',
           '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군']
    menu_1 = st.sidebar.selectbox("시군구명 1", ch_list)
    menu_2 = st.sidebar.selectbox("시군구명 2", ch_list)
    selected_year = st.sidebar.selectbox("년도", ['2019', '2020', '2021', '2022'])

    st.title('충청남도 거주자의 충청남도외 소비 현황 분석')
    st.text('마지막 새로고침 시간 : ' + str(datetime.datetime.now()))

    in_person_out_buy['기준연월'] = in_person_out_buy['기준연월'].astype(str).apply(lambda x: f'{x[:4]}년 {x[4:]}월')
    in_person_out_buy['평균이용금액'] = (in_person_out_buy['전체이용금액'] / in_person_out_buy['전체이용건수']).apply(lambda x: round(x))
    in_person_out_buy = pd.DataFrame(in_person_out_buy.groupby(['기준연월', '시군구명'])['평균이용금액'].mean().apply(lambda x: round(x))).reset_index(['기준연월']).reset_index(['시군구명'])
    in_person_out_buy_pivot = in_person_out_buy.reset_index().pivot(index='기준연월', columns='시군구명', values='평균이용금액')

    if st.button('전체 데이터 보기'):
        st.write(in_person_out_buy_pivot)
    else:
        st.write("")
    
    fig, ax = plt.subplots(figsize=(15, 9))
    start_index = (int(selected_year) - 2019) * 12
    end_index = start_index + 12
    for i, item in enumerate(ch_list):
        if menu_1 == item or menu_2 == item:
            ax.plot(in_person_out_buy_pivot.index[start_index:end_index], in_person_out_buy_pivot[start_index:end_index][item], label=item, alpha=1)
            if st.checkbox(item):
                st.write(in_person_out_buy[in_person_out_buy['시군구명'] == item].set_index(['기준연월'])[start_index:end_index])
        else:
            ax.plot(in_person_out_buy_pivot.index[start_index:end_index], in_person_out_buy_pivot[start_index:end_index][item], label=item, alpha=0.1)

    ax.set_xlabel('기준 연월')
    ax.set_ylabel('평균 소비 금액')
    ax.set_title('월별 평균소비금액 변화 추이 지역별 비교')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    st.pyplot(fig)
    
# 세 번째 서비스 구현
def service_3():
    out_person_in_buy = pd.read_csv("C:/Users/SEC/Desktop/충청남도 데이터포털 올담 데이터 활용 시각화 경진대회/충남외 고객기준 충남 소비 현황.csv", encoding='cp949')
    ko_list = ['강원도','경기도','경상남도','경상북도','광주광역시','대구광역시','대전광역시','부산광역시','서울특별시','세종특별자치시',
           '울산광역시','인천광역시','전라남도','전라북도','제주특별자치도','충청북도']
    menu_1 = st.sidebar.selectbox("고객의 광역시군구명 1", ko_list)
    menu_2 = st.sidebar.selectbox("고객의 광역시군구명 2", ko_list)
    selected_year = st.sidebar.selectbox("년도", ['2019', '2020', '2021', '2022'])

    st.title('충청남도외 거주자의 충청남도 소비 현황 분석')
    st.text('마지막 새로고침 시간 : ' + str(datetime.datetime.now()))

    out_person_in_buy['기준연월'] = out_person_in_buy['기준연월'].astype(str).apply(lambda x: f'{x[:4]}년 {x[4:]}월')
    out_person_in_buy['평균이용금액'] = (out_person_in_buy['전체이용금액'] / out_person_in_buy['전체이용건수']).apply(lambda x: round(x))
    out_person_in_buy = out_person_in_buy.groupby(['기준연월', '고객광역시군구명']).mean().reset_index()
    out_person_in_buy_pivot = out_person_in_buy.pivot(index='기준연월', columns='고객광역시군구명', values='평균이용금액')

    if st.button('전체 데이터 보기'):
        st.write(out_person_in_buy_pivot)
    else:
        st.write("")
    
    fig, ax = plt.subplots(figsize=(15, 9))
    start_index = (int(selected_year) - 2019) * 12
    end_index = start_index + 12
    for i, item in enumerate(ko_list):
        if menu_1 == item or menu_2 == item:
            ax.plot(out_person_in_buy_pivot.index[start_index:end_index], out_person_in_buy_pivot[start_index:end_index][item], label=item, alpha=1)
            if st.checkbox(item):
                st.write(out_person_in_buy[out_person_in_buy['고객광역시군구명'] == item].set_index(['기준연월'])[start_index:end_index])
        else:
            ax.plot(out_person_in_buy_pivot.index[start_index:end_index], out_person_in_buy_pivot[start_index:end_index][item], label=item, alpha=0.1)

    ax.set_xlabel('기준 연월')
    ax.set_ylabel('평균 소비 금액')
    ax.set_title('월별 평균소비금액 변화 추이 지역별 비교')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    st.pyplot(fig)
    
#네 번째 서비스 구현
def service_4():
    month_per_card = pd.read_csv("C:/Users/SEC/Desktop/충청남도 데이터포털 올담 데이터 활용 시각화 경진대회/충남 월별 카드 소비 현황.csv", encoding='cp949')
    ch_list = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시',
           '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군']
    menu_1 = st.sidebar.selectbox("시군구명 1", ch_list)
    menu_2 = st.sidebar.selectbox("시군구명 2", ch_list)
    selected_year = st.sidebar.selectbox("년도", ['2019', '2020', '2021', '2022'])

    st.title('충청남도 월별 카드 소비 현황 분석')
    st.text('마지막 새로고침 시간 : ' + str(datetime.datetime.now()))

    month_per_card['기준연월'] = month_per_card['기준연월'].astype(str).apply(lambda x: f'{x[:4]}년 {x[4:]}월')
    month_per_card['평균이용금액'] = (month_per_card['이용금액'] / month_per_card['이용건수']).apply(lambda x: round(x))
    month_per_card = month_per_card.groupby(['기준연월', '시군구명']).mean().reset_index()
    month_per_card_pivot = month_per_card.pivot(index='기준연월', columns='시군구명', values='평균이용금액')

    if st.button('전체 데이터 보기'):
        st.write(month_per_card_pivot)
    else:
        st.write("")
    
    fig, ax = plt.subplots(figsize=(15, 9))
    start_index = (int(selected_year) - 2019) * 12
    end_index = start_index + 12
    for i, item in enumerate(ch_list):
        if menu_1 == item or menu_2 == item:
            ax.plot(month_per_card_pivot.index[start_index:end_index], month_per_card_pivot[start_index:end_index][item], label=item, alpha=1)
            if st.checkbox(item):
                st.write(month_per_card[month_per_card['시군구명'] == item].set_index(['기준연월'])[start_index:end_index])
        else:
            ax.plot(month_per_card_pivot.index[start_index:end_index], month_per_card_pivot[start_index:end_index][item], label=item, alpha=0.1)

    ax.set_xlabel('기준 연월')
    ax.set_ylabel('평균 소비 금액')
    ax.set_title('월별 카드소비현황 지역별 비교')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    st.pyplot(fig)
    
#다섯 번째 서비스 구현
def service_5():
    month_per_store = pd.read_csv("C:/Users/SEC/Desktop/충청남도 데이터포털 올담 데이터 활용 시각화 경진대회/충남 월별 휴폐업가맹점수 현황.csv", encoding='cp949')
    ch_list = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시',
           '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군']
    menu_1 = st.sidebar.selectbox("시군구명 1", ch_list)
    menu_2 = st.sidebar.selectbox("시군구명 2", ch_list)
    selected_year = st.sidebar.selectbox("년도", ['2019', '2020', '2021', '2022'])

    st.title('충청남도 월별 운영가맹점비율 현황 분석')
    st.text('마지막 새로고침 시간 : ' + str(datetime.datetime.now()))

    month_per_store['기준연월'] = month_per_store['기준연월'].astype(str).apply(lambda x: f'{x[:4]}년 {x[4:]}월')
    month_per_store['운영가맹점수'] = month_per_store['가맹점수'] - (month_per_store['휴업가맹점수'] + month_per_store['폐업가맹점수'])
    month_per_store['운영가맹점비율'] = (month_per_store['운영가맹점수'] / month_per_store['가맹점수']) * 100
    month_per_store = month_per_store.groupby(['기준연월', '시군구명']).mean().reset_index()
    month_per_store_pivot = month_per_store.pivot(index='기준연월', columns='시군구명', values='운영가맹점비율')

    if st.button('전체 데이터 보기'):
        st.write(month_per_store_pivot)
    else:
        st.write("")
    
    fig, ax = plt.subplots(figsize=(15, 9))
    start_index = (int(selected_year) - 2019) * 12
    end_index = start_index + 12
    for i, item in enumerate(ch_list):
        if menu_1 == item or menu_2 == item:
            ax.plot(month_per_store_pivot.index[start_index:end_index], month_per_store_pivot[start_index:end_index][item], label=item, alpha=1)
            if st.checkbox(item):
                st.write(month_per_store[month_per_store['시군구명'] == item].set_index(['기준연월'])[start_index:end_index])
        else:
            ax.plot(month_per_store_pivot.index[start_index:end_index], month_per_store_pivot[start_index:end_index][item], label=item, alpha=0.1)

    ax.set_xlabel('기준 연월')
    ax.set_ylabel('운영가맹점비율')
    ax.set_title('월별 운영가맹점비율 현황 지역별 비교')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    st.pyplot(fig)
    
#여섯 번째 서비스 구현
def service_6():
    month_per_store = pd.read_csv("C:/Users/SEC/Desktop/충청남도 데이터포털 올담 데이터 활용 시각화 경진대회/충남 월별 휴폐업가맹점수 현황.csv", encoding='cp949')
    ch_list = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시',
           '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군']
    menu_1 = st.sidebar.selectbox("시군구명 1", ch_list)
    menu_2 = st.sidebar.selectbox("시군구명 2", ch_list)
    selected_year = st.sidebar.selectbox("년도", ['2019', '2020', '2021', '2022'])

    st.title('충청남도 월별 휴업가맹점비율 현황 분석')
    st.text('마지막 새로고침 시간 : ' + str(datetime.datetime.now()))

    month_per_store['기준연월'] = month_per_store['기준연월'].astype(str).apply(lambda x: f'{x[:4]}년 {x[4:]}월')
    month_per_store['운영가맹점수'] = month_per_store['가맹점수'] - (month_per_store['휴업가맹점수'] + month_per_store['폐업가맹점수'])
    month_per_store['휴업가맹점비율'] = (month_per_store['휴업가맹점수'] / month_per_store['가맹점수']) * 100
    month_per_store = month_per_store.groupby(['기준연월', '시군구명']).mean().reset_index()
    month_per_store_pivot = month_per_store.pivot(index='기준연월', columns='시군구명', values='휴업가맹점비율')

    if st.button('전체 데이터 보기'):
        st.write(month_per_store_pivot)
    else:
        st.write("")
    
    fig, ax = plt.subplots(figsize=(15, 9))
    start_index = (int(selected_year) - 2019) * 12
    end_index = start_index + 12
    for i, item in enumerate(ch_list):
        if menu_1 == item or menu_2 == item:
            ax.plot(month_per_store_pivot.index[start_index:end_index], month_per_store_pivot[start_index:end_index][item], label=item, alpha=1)
            if st.checkbox(item):
                st.write(month_per_store[month_per_store['시군구명'] == item].set_index(['기준연월'])[start_index:end_index])
        else:
            ax.plot(month_per_store_pivot.index[start_index:end_index], month_per_store_pivot[start_index:end_index][item], label=item, alpha=0.1)

    ax.set_xlabel('기준 연월')
    ax.set_ylabel('휴업가맹점비율')
    ax.set_title('월별 휴업가맹점비율 현황 지역별 비교')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    st.pyplot(fig)

#일곱 번째 서비스 구현
def service_7():
    month_per_store = pd.read_csv("C:/Users/SEC/Desktop/충청남도 데이터포털 올담 데이터 활용 시각화 경진대회/충남 월별 휴폐업가맹점수 현황.csv", encoding='cp949')
    ch_list = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시',
           '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군']
    menu_1 = st.sidebar.selectbox("시군구명 1", ch_list)
    menu_2 = st.sidebar.selectbox("시군구명 2", ch_list)
    selected_year = st.sidebar.selectbox("년도", ['2019', '2020', '2021', '2022'])

    st.title('충청남도 월별 폐업가맹점비율 현황 분석')
    st.text('마지막 새로고침 시간 : ' + str(datetime.datetime.now()))

    month_per_store['기준연월'] = month_per_store['기준연월'].astype(str).apply(lambda x: f'{x[:4]}년 {x[4:]}월')
    month_per_store['운영가맹점수'] = month_per_store['가맹점수'] - (month_per_store['휴업가맹점수'] + month_per_store['폐업가맹점수'])
    month_per_store['폐업가맹점비율'] = (month_per_store['폐업가맹점수'] / month_per_store['가맹점수']) * 100
    month_per_store = month_per_store.groupby(['기준연월', '시군구명']).mean().reset_index()
    month_per_store_pivot = month_per_store.pivot(index='기준연월', columns='시군구명', values='폐업가맹점비율')

    if st.button('전체 데이터 보기'):
        st.write(month_per_store_pivot)
    else:
        st.write("")
    
    fig, ax = plt.subplots(figsize=(15, 9))
    start_index = (int(selected_year) - 2019) * 12
    end_index = start_index + 12
    for i, item in enumerate(ch_list):
        if menu_1 == item or menu_2 == item:
            ax.plot(month_per_store_pivot.index[start_index:end_index], month_per_store_pivot[start_index:end_index][item], label=item, alpha=1)
            if st.checkbox(item):
                st.write(month_per_store[month_per_store['시군구명'] == item].set_index(['기준연월'])[start_index:end_index])
        else:
            ax.plot(month_per_store_pivot.index[start_index:end_index], month_per_store_pivot[start_index:end_index][item], label=item, alpha=0.1)

    ax.set_xlabel('기준 연월')
    ax.set_ylabel('폐업가맹점비율')
    ax.set_title('월별 폐업가맹점비율 현황 지역별 비교')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.grid(True)
    st.pyplot(fig)
    
# 메인 애플리케이션
def main():
    app_mode = st.sidebar.selectbox("보고 싶은 분석 현황을 선택하세요.", ["충청남도 거주자의 충청남도 소비 현황 분석", "충청남도 거주자의 충청남도외 소비 현황 분석", "충청남도외 거주자의 충청남도 소비 현황 분석", 
                                                            "충청남도 월별 카드 소비 현황 분석", "충청남도 월별 운영가맹점비율 현황 분석", "충청남도 월별 휴업가맹점비율 현황 분석", "충청남도 월별 폐업가맹점비율 현황 분석"])
    if app_mode == "충청남도 거주자의 충청남도 소비 현황 분석":
        service_1()
    elif app_mode == "충청남도 거주자의 충청남도외 소비 현황 분석":
        service_2()
    elif app_mode == "충청남도외 거주자의 충청남도 소비 현황 분석":
        service_3()
    elif app_mode == "충청남도 월별 카드 소비 현황 분석":
        service_4()
    elif app_mode == "충청남도 월별 운영가맹점비율 현황 분석":
        service_5()
    elif app_mode == "충청남도 월별 휴업가맹점비율 현황 분석":
        service_6()
    elif app_mode == "충청남도 월별 폐업가맹점비율 현황 분석":
        service_7()

if __name__ == '__main__':
    main()
