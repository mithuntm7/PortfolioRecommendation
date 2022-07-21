import pandas as pd
def get_score(option,que):
    if que == 14:
        if option == 'a' :
            return 'stock'
        else:
            return 'cryptocurrency'
    elif que == 13:
        if option == 'a':
            return 0
        elif option == 'b':
            return 1
        else:
            return 2
    elif que == 0:
        if(option == 'a'):
            return 4
        elif option == 'b':
            return 3
        elif option == 'c':
            return 2
        elif option == 'd':
            return 1
    elif que == 8 or que ==  9:
        if(option == 'a'):
            return 1
        if(option == 'b'):
            return 3
    else:
        if(option == 'a'):
            return 1
        elif option == 'b':
            return 2
        elif option == 'c':
            return 3
        elif option == 'd':
            return 4
def get_risk_profile(score):
    if score <= 18:
        return 'low risk tolerance'
    elif score <= 22:
        return 'Below average risk tolerance'
    elif score <= 28:
        return 'Average/moderate risk tolerance'
    elif score <= 32:
        return 'Above average risk tolerance'
    elif score >= 33:
        return 'High risk tolerance'
risk_profile_dict  = {'low risk tolerance':1,'Below average risk tolerance': 2,'Average/moderate risk tolerance' : 3,'Above average risk tolerance' : 4, 'High risk tolerance':5}
import streamlit as st
import re
st.set_page_config(
    page_title = "Dashboard",
    layout = "wide",
    page_icon = ":bar_chart:")
st.title("Portfolio Allocation")
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)
min_amt =  50000
fp = open("risk_profile_quiz.txt",'r')
a = fp.read()
split1 = re.split(r'\d+\. ',a)
q_op = []
for i in split1:
    if i != '':
        q_op.append(i.split('\n'))
ans = []
key_index = 1
df_stock = pd.read_csv('portfolio_recommendations.csv')
df_coins = pd.read_csv('coins_portfolio_recommendations.csv')

questions = st.empty()
with questions.expander("Questions",expanded=True):
    st.markdown(
    "**Please answer following questions to get your Risk Profile**"
)
    for que in q_op:
        st.write(str(key_index)+") " +que[0])
        ans.append(st.radio('Choose any one',que[1:-1],key = key_index))
        key_index += 1
    st.write(str(key_index)+") " +'How much money do you want to invest?')
    money = st.text_input("(in multiples of 50000 Rs)")
    if(money  ==  ''):
        money = 0
    submit = st.button('Submit')

if submit:
    questions.empty()
    print('money is', money)
    st.info("*Your answers have been submitted*")
    scores = []
    for i in range(0,len(ans)):
        scores.append(get_score(ans[i].split('.')[0],i))
    print("scores are",scores)
    risk_profile = get_risk_profile(sum(scores[:-2]))
    st.write('You fall under *'+risk_profile+'* category')
    if int(money) >= min_amt:
    # not doing error handling for money values which are not multiples of 50k
        st.write('Here is a recommendation for your investement amount of ' + str(money)+' Rs '+ 'based on your risk profile')
        multiple = int(money) // min_amt
        if scores[-1] == 'stock':
            df_stock['qty'] = df_stock['qty'] * multiple
            df_stock['total'] = df_stock['qty']*df_stock['latest_price']
            df_sub = df_stock[(df_stock['risk_perc'] == risk_profile_dict[risk_profile]) & (df_stock['hedge_category'] == scores[-2])]
            df_sub = df_sub[['Name','Asset_Name','latest_price','qty','total']]
            df_sub.rename(columns = {'Name':'Scrip code','Asset_Name':'Stock name','qty':'Quantity',
                'latest_price':'*Price','total':'Total'}, inplace = True)
        else:
            df_coins['qty'] = df_coins['qty'] * multiple
            df_coins['total'] = df_coins['qty']*df_coins['latest_price']
            df_sub = df_coins[(df_coins['risk_perc'] == risk_profile_dict[risk_profile]) & (df_coins['hedge_category'] == scores[-2])]
            df_sub = df_sub[['Name','Asset_Name','latest_price','qty','total']]
            df_sub.rename(columns = {'Name':'Scrip Code','Asset_Name':'Cryptocurrency name', 'qty':'Quantity',
                'latest_price':'*Price','total' : 'Total'}, inplace = True)
        df_sub = df_sub.reset_index(drop=True)
        df_sub.index = df_sub.index + 1
        st.table(df_sub)
        print(df_sub['Total'].values.sum())
        st.write('* *Price represents price as on 8th december 2021')
    else:
        st.warning('Investment amount should be greater than ' + str(min_amt)+' Rs for portfolio recommendation, Please refresh the page to go back to input investment amount')
