import streamlit as st
import pickle
model=pickle.load(open('Heart.pkl','rb'))
def predict_attack(h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13):
    if h2=='male':
        h2=0
    else:
        h2=1
    if h3=='angina':
        h3=0
    elif h3=='atypical anigna':
       h3=1
    elif h3=='non-anignal pain':
       h3=2
    else:
        h3=3
    if h6=='greater than 120':
        h6=1
    else:
        h6=0
    if h7=='normal':
        h7=0
    elif h7=='ST-t normal':
        h7=1
    else:
        h7=2
    if h13=='yes':
        h13=1
    else:
        h13=0
    res=model.predict([[h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13]])
    return res
def heart():
    st.write('heart')
    html_temp="""
    <div style='background-color:yellow;padding:13px'>
    <h1 style='color:black;text-align:center;'>Heart attack predictor </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    h1=st.text_input('Age')
    h2=st.selectbox('sex',['male','female'])
    h3=st.selectbox('type of chest pain',['angina','atypical anigna','non-anignal pain','asymptomatic'])
    h4=st.text_input('blood pressure')
    h5=st.text_input('cholesterol')
    h6=st.selectbox('blood sugar',['greater than 120',' less than120'])
    h7=st.selectbox('ecg results',['normal','ST-t normal','left ventricular hypertrophy'])
    h8=st.text_input('max heart rate')
    h9=st.text_input('old peak value ranges(0 to 4.5)')
    h10=st.text_input('slope value (0,1,2)')
    h11=st.text_input('no.of vessels (0,1,2,3)')
    h12=st.text_input('stress result (0,1,2)')
    h13=st.selectbox('excerise induced anigna',['yes','no'])
    result=" "
    
    if st.button('Predict'):
        result=predict_attack(h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13)
        
        if result==0:
            st.write(' # There is no chance of heart attack in near future ')
        else:
            st.write(' # You might get heart attack consult Doctor Please......')
if __name__=='__main__':
    heart()