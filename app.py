import pickle
import streamlit as st
import numpy as np

#loading the saved models
with open('C:/Users/tharu/OneDrive/Desktop/streamlit/credit_2.pkl', 'rb') as f:
    cc_model = pickle.load(f)

def cc_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = cc_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is will do attrition'
    else:
      return 'The person will continue to use'   

def main():
    
    
    # giving a title
    st.title('Credit Card Attrition Prediction using ML')
    
    # getting the input data from the user
    
    
     
    
    # Create the input fields for the user to input values
gender = st.selectbox('Gender', ['Male', 'Female'])
#education_level = st.selectbox('Education Level', ['High School', 'Graduate', 'Uneducated', 'College', 'Post-Graduate', 'Doctorate'])
marital_status = st.selectbox('Marital Status', ['Divorced', 'Married', 'Single','Unknown'])
#Income_Category = st.selectbox('Income Category', ['$120K+', '$40k-$60k', '$60K-$80K', '$80K-$120K', 'Less than $40K'])
Card_Category = st.selectbox('Card Category', ['Blue', 'Gold', 'Platinum','Unknown'])

dependent_count = st.text_input('Dependent Count', '0')
total_relationship_count = st.text_input('Total Relationship Count', '0')
months_inactive_12_mon = st.text_input('Months Inactive 12 Months', '0')
contacts_count_12_mon = st.text_input('Contacts Count 12 Months', '0')
total_amt_chng_q4_q1 = st.text_input('Total Amount Change Q4 Q1', '0')
total_trans_ct = st.text_input('Total Transaction Count', '0')
total_ct = st.text_input('Total Transaction Change','0')

# convert input data to numeric types
dependent_count = int(dependent_count)
total_relationship_count = int(total_relationship_count)
months_inactive_12_mon = int(months_inactive_12_mon)
contacts_count_12_mon = int(contacts_count_12_mon)
total_amt_chng_q4_q1 = int(total_amt_chng_q4_q1)
total_trans_ct = int(total_trans_ct)
total_ct = int(total_ct)

gender_val = 1 if gender == 'Male' else 0
#edu_val = 0 if education_level == 'High School' else 1 if education_level == 'Graduate' else 2 if education_level == 'Uneducated' else 3 if education_level == 'College' else 4 if Education_Level == 'Post-Graduate' else 5 if Education_Level == 'Doctorate' else 6
mrg_val = 0 if marital_status == 'Divorced' else 1 if marital_status == 'Married' else 2 if marital_status == 'Single' else 3 
#inc_val = 0 if Income_Category == '$120K+' else 1 if Income_Category == '$40k-$60k' else 2 if Income_Category == '$60K-$80K' else 3 if Income_Category == '$80K-$120K' else 4 if Income_Category == 'Less than $40K' else 5 
ctg_val = 0 if Card_Category == 'Blue' else 1 if Card_Category == 'Gold' else 2 if Card_Category == 'Platinum' else 3 
    
    
    # code for Prediction
attrition = ''
    
    # creating a button for Prediction
    
if st.button('Attrition Prediction Result'):
        attrition = cc_prediction([gender_val,dependent_count,mrg_val,ctg_val,total_relationship_count,months_inactive_12_mon,contacts_count_12_mon,total_amt_chng_q4_q1,total_trans_ct,total_ct])
        
        
st.success(attrition)
    
    
    
    
    
if __name__ == '__main__':
    main()