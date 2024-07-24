import numpy as np
import pickle
import streamlit as st


#load the pickle fine
loaded_model = pickle.load(open('Xg_model.sav', 'rb')) 


#Creating a function for prediction
def diabetic_prediction(input_data):
      
    #changing input_data to np array
    input_data_array = np.asarray(input_data)
    #reshape array as we are predicting for one instance
    input_data_reshaped = input_data_array.reshape(1,-1)

    predictions = loaded_model.predict(input_data_reshaped)
    print(predictions)

    if(predictions[0]==0):
        return 'The person is not diabetic'
    else:
        return 'According to the input data the person might be diabetic, please get a test done!'
    



def main():

    #Giving a title
    st.title('Risk of Developing Diabetes Web App')

    Age =  st.number_input("Please enter your age")
    
    Gender = st.radio('Gender', ['Male', 'Female'])
    Gender = 0 if Gender == 'Male' else 1

    Polyuria = st.selectbox("Polyuria",['Yes','No'])
    Polyuria = 1 if Polyuria == 'Yes' else 0

    Polydipsia = st.selectbox("Polydipsia",['Yes','No'])
    Polydipsia = 1 if Polydipsia == 'Yes' else 0

    suddenweightloss = st.selectbox("sudden weight loss",['Yes','No'])
    suddenweightloss = 1 if suddenweightloss == 'Yes' else 0

    weakness = st.selectbox("weakness",['Yes','No'])
    weakness = 1 if weakness == 'Yes' else 0

    Polyphagia = st.selectbox("Polyphagia",['Yes','No'])
    Polyphagia = 1 if Polyphagia == 'Yes' else 0

    Genitalthrush = st.selectbox("Genital thrush",['Yes','No'])
    Genitalthrush = 1 if Genitalthrush == 'Yes' else 0

    visualblurring = st.selectbox("visual blurring",['Yes','No'])
    visualblurring = 1 if visualblurring == 'Yes' else 0

    Itching = st.selectbox("Itching",['Yes','No'])
    Itching = 1 if Itching == 'Yes' else 0

    Irritability = st.selectbox("Irritability",['Yes','No'])
    Irritability = 1 if Irritability == 'Yes' else 0

    delayedhealing = st.selectbox("delayed healing",['Yes','No'])
    delayedhealing = 1 if delayedhealing == 'Yes' else 0

    partialparesis = st.selectbox("partial paresis",['Yes','No'])
    partialparesis = 1 if partialparesis == 'Yes' else 0

    musclestiffness = st.selectbox("muscle stiffness",['Yes','No'])
    musclestiffness = 1 if musclestiffness == 'Yes' else 0

    Alopecia = st.selectbox("Alopecia",['Yes','No'])
    Alopecia = 1 if Alopecia == 'Yes' else 0

    Obesity = st.selectbox("Obesity",['Yes','No'])
    Obesity = 1 if Obesity == 'Yes' else 0



    #Code for prediction
    diagnosis = ''

    #Creating a button for prediction
    if st.button('Sumbit'):
        diagnosis = diabetic_prediction([Age,Gender,Polyuria,Polydipsia,suddenweightloss,weakness,Polyphagia,Genitalthrush,visualblurring,Itching,Irritability,delayedhealing,partialparesis,musclestiffness,Alopecia,Obesity])
    
    st.success(diagnosis)


if __name__ =='__main__':
    main()

