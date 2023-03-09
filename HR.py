import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("HR.pkl","rb")
rfc=pickle.load(pickle_in)

def predict_employee_turnover(satisfaction_level, last_evaluation, number_project, average_montly_hours, time_spend_company, Work_accident, promotion_last_5years, salary, sales_IT, sales_RandD, sales_accounting, sales_hr, sales_management, sales_marketing, sales_product_mng, sales_sales, sales_support, sales_technical):
    
    prediction=rfc.predict([[satisfaction_level, last_evaluation, number_project, average_montly_hours, time_spend_company, Work_accident, promotion_last_5years, salary, sales_IT, sales_RandD, sales_accounting, sales_hr, sales_management, sales_marketing, sales_product_mng, sales_sales, sales_support, sales_technical]])
    print(prediction)
    return prediction




def main():
    st.title("Прогнозирование текучести кадров в компании")
    html_temp = """
    <div style = "background-color:maroon     ;padding:10px">
    <h2 style="color:white;text-align:center;">Forecasting employee turnover in the company. Based on data from kaggle.com, algorithm RandomForest </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    satisfaction_level=st.radio("Уровень удовлетворенности сотрудника:", 
               key="satisfaction_level",
               options=["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0"], )
    if satisfaction_level=="0.1":
        satisfaction_level=0.1
    elif satisfaction_level=="0.2":
        satisfaction_level=0.2
    elif satisfaction_level=="0.3":
        satisfaction_level=0.3
    elif satisfaction_level=="0.4":
        satisfaction_level=0.4
    elif satisfaction_level=="0.5":
        satisfaction_level=0.5
    elif satisfaction_level=="0.6":
        satisfaction_level=0.6
    elif satisfaction_level=="0.7":
        satisfaction_level=0.7
    elif satisfaction_level=="0.8":
        satisfaction_level=0.8
    elif satisfaction_level=="0.9":
        satisfaction_level=0.9
    elif satisfaction_level=="1.0":
        satisfaction_level=1.0
       
    last_evaluation=st.radio("Оценка работодателя:",
               key="last_evaluation",
               options=["0.1","0.2","0.3","0.4","0.5","0.6","0.7","0.8","0.9","1.0"], )
    if last_evaluation=="0.1":
        last_evaluation=0.1
    elif last_evaluation=="0.2":
        last_evaluation=0.2
    elif last_evaluation=="0.3":
        last_evaluation=0.3
    elif last_evaluation=="0.4":
        last_evaluation=0.4
    elif last_evaluation=="0.5":
        last_evaluation=0.5
    elif last_evaluation=="0.6":
        last_evaluation=0.6
    elif last_evaluation=="0.7":
        last_evaluation=0.7
    elif last_evaluation=="0.8":
        last_evaluation=0.8
    elif last_evaluation=="0.9":
        last_evaluation=0.9
    elif last_evaluation=="1.0":
        last_evaluation=1.0
        
    number_project = st.text_input("Количество выполняемых проектов","")
    average_montly_hours = st.text_input("Среднее количество рабочих часов за месяц","")
    time_spend_company = st.text_input("Время работы в компании в годах","")
    
    Work_accident=st.radio("Был ли несчастный случай на рабочем месте:",
               key="Work_accident",
               options=["Да", "Нет"], )
    if Work_accident=="Да":
        Work_accident=1
    elif Work_accident=="Нет":
        Work_accident=0
    
    promotion_last_5years=st.radio("Было повышение за последние 5 лет:",
               key="promotion_last_5years",
               options=["Да", "Нет"], )
    if promotion_last_5years=="Да":
        promotion_last_5years=1
    elif promotion_last_5years=="Нет":
        promotion_last_5years=0
    
    salary=st.radio("Уровень заработной платы:",
               key="salary",
               options=["Низкий", "Средний", "Высокий"], )
    if salary=="Низкий":
        salary=0
    elif salary=="Средний":
        salary=1
    elif salary=="Высокий":
        salary=2
        
        
    sales_IT=st.radio("Отдел IT:",
               key="sales_IT",
               options=["Да", "Нет"], )
    if sales_IT=="Да":
        sales_IT=1
    elif sales_IT=="Нет":
        sales_IT=0
        
        
    sales_RandD=st.radio("Отдел исследований и разработок:",
               key="sales_RandD",
               options=["Да", "Нет"], )
    if sales_RandD=="Да":
        sales_RandD=1
    elif sales_RandD=="Нет":
        sales_RandD=0
        
       
    sales_accounting=st.radio("Бухгалтерия:",
               key="sales_accounting",
               options=["Да", "Нет"], )
    if sales_accounting=="Да":
        sales_accounting=1
    elif sales_accounting=="Нет":
        sales_accounting=0
    
        
    sales_hr=st.radio("Отдел кадров:",
               key="sales_hr",
               options=["Да", "Нет"], )
    if sales_hr=="Да":
        sales_hr=1
    elif sales_hr=="Нет":
        sales_hr=0
        
        
    sales_management=st.radio("Отдел управления:",
               key="sales_management",
               options=["Да", "Нет"], )
    if sales_management=="Да":
        sales_management=1
    elif sales_management=="Нет":
        sales_management=0    
  

    sales_marketing=st.radio("Отдел маркетинга:",
               key="sales_marketing",
               options=["Да", "Нет"], )
    if sales_marketing=="Да":
        sales_marketing=1
    elif sales_marketing=="Нет":
        sales_marketing=0 
        
        
    sales_product_mng=st.radio("Отдел управления продуктом:",
               key="sales_product_mng",
               options=["Да", "Нет"], )
    if sales_product_mng=="Да":
        sales_product_mng=1
    elif sales_product_mng=="Нет":
        sales_product_mng=0        
        
        
    sales_sales=st.radio("Отдел продаж:",
               key="sales_sales",
               options=["Да", "Нет"], )
    if sales_sales=="Да":
        sales_sales=1
    elif sales_sales=="Нет":
        sales_sales=0
        
        
    sales_support=st.radio("Отдел поддержки:",
               key="sales_support",
               options=["Да", "Нет"], )
    if sales_support=="Да":
        sales_support=1
    elif sales_support=="Нет":
        sales_support=0

        
    sales_technical=st.radio("Технический отдел:",
               key="sales_technical",
               options=["Да", "Нет"], )
    if sales_technical=="Да":
        sales_technical=1
    elif sales_technical=="Нет":
        sales_technical=0

        
    result=""
    if st.button("Predict"):
        result=int(predict_employee_turnover(satisfaction_level, last_evaluation, number_project, average_montly_hours, time_spend_company, Work_accident, promotion_last_5years, salary, sales_IT, sales_RandD, sales_accounting, sales_hr, sales_management, sales_marketing, sales_product_mng, sales_sales, sales_support, sales_technical))
    
    st.success('Forecasting employee turnover in the company is {}'. format(result))
       
    

if __name__=='__main__':
    main()
    
    