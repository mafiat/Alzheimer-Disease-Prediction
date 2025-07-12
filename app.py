import streamlit as st 
import joblib as jb
import streamlit_option_menu as som


init_state = 1

# Initialize session state
if 'inputs' not in st.session_state:
    
    # Initialize at 0
    if init_state == 0:
        
        st.session_state.inputs = {

            'Age' : 0, 'Gender'  : 0, 'Ethnicity' : 0, 'EducationLevel' : 0, 'BMI' : 0, 'Smoking' : 0, 'AlcoholConsumption' : 0, 'PhysicalActivity' : 0, 'DietQuality' : 0, 
            'SleepQuality' : 0, 'FamilyHistoryAlzheimers' : 0, 'CardiovascularDisease' : 0, 'Diabetes' : 0, 'Depression' : 0, 'HeadInjury' : 0, 'Hypertension' : 0, 
            'SystolicBP' : 0, 'DiastolicBP' : 0, 'CholesterolTotal' : 0, 'CholesterolLDL' : 0, 'CholesterolHDL' : 0, 'CholesterolTriglycerides': 0, 'MMSE' : 0, 
            'FunctionalAssessment' : 0, 'MemoryComplaints': 0, 'BehavioralProblems' : 0, 'ADL' : 0, 
            'Confusion' : 0, 'Disorientation' : 0, 'PersonalityChanges' : 0, 'DifficultyCompletingTasks' : 0, 'Forgetfulness' : 0
        }

    elif init_state == 1:

        # Initialize at Positive Diagnosis
        st.session_state.inputs = {
        
            'Age': 75, 'Gender': 0, 'Ethnicity': 1, 'EducationLevel': 1, 'BMI': 37.82358359433992, 'Smoking': 0, 
            'AlcoholConsumption': 16.304243474496573, 'PhysicalActivity': 9.365582915067233, 'DietQuality': 9.270864301354187, 
            'SleepQuality': 5.975956455105875, 'FamilyHistoryAlzheimers': 0, 'CardiovascularDisease': 0, 'Diabetes': 0, 
            'Depression': 0, 'HeadInjury': 0, 'Hypertension': 1, 'SystolicBP': 126, 'DiastolicBP': 116, 
            'CholesterolTotal': 150.57569546009037, 'CholesterolLDL': 123.26605517737944, 
            'CholesterolHDL': 85.50912659504417, 'CholesterolTriglycerides': 132.67012493888328, 'MMSE': 16.042137912629553, 
            'FunctionalAssessment': 0.4485933639995765, 'MemoryComplaints': 1, 'BehavioralProblems': 0, 'ADL': 3.9685096195269782, 
            'Confusion': 0, 'Disorientation': 0, 'PersonalityChanges': 0, 'DifficultyCompletingTasks': 0, 'Forgetfulness': 1
        
        }

    elif init_state == -1:

        # Initialize at Positive Diagnosis
        st.session_state.inputs = {
        
            'Age': 88, 'Gender': 1, 'Ethnicity': 1, 'EducationLevel': 0, 'BMI': 26.341456947179157, 'Smoking': 0, 
            'AlcoholConsumption': 17.79386563482942, 'PhysicalActivity': 1.0160872463134385, 'DietQuality': 5.708031590789324, 
            'SleepQuality': 9.325018261775718, 'FamilyHistoryAlzheimers': 0, 'CardiovascularDisease': 0, 'Diabetes': 0, 
            'Depression': 0, 'HeadInjury': 0, 'Hypertension': 0, 'SystolicBP': 176, 'DiastolicBP': 77, 
            'CholesterolTotal': 210.94903637664044, 'CholesterolLDL': 58.110510626425295, 
            'CholesterolHDL': 96.68184989926915, 'CholesterolTriglycerides': 206.73335215654765, 'MMSE': 14.48864071302017, 
            'FunctionalAssessment': 7.307850829651147, 'MemoryComplaints': 0, 'BehavioralProblems': 0, 'ADL': 6.800702841611061, 
            'Confusion': 1, 'Disorientation': 0, 'PersonalityChanges': 0, 'DifficultyCompletingTasks': 0, 'Forgetfulness': 1
        
        }

if 'model' not in st.session_state:
    st.session_state.model = jb.load('model_gb.joblib')

# Sidebar menu
with st.sidebar:
    menu_option = ['Prediction']
    selected_option = som.option_menu('Alzheimer Desease Prediction System', options=menu_option, icons=['hospital'], menu_icon='bandaid')

# Prediction page
if selected_option == 'Prediction':
    st.header('Alzheimer Desease Prediction System')
    
    with st.form(key='prediction_form'):
        st.subheader('Health Information')

        # Input fields for health information
        ### Demographic Details
        with st.expander("Demographic Details", expanded=True):
            st.session_state.inputs['Age'] = st.slider('Age:', min_value=60, max_value=90, value=st.session_state.inputs['Age'])
            st.session_state.inputs['Gender'] = st.radio('Gender:', options=[0, 1], format_func=lambda x: 'Male' if x == 0 else 'Female', index=st.session_state.inputs['Gender'])
            st.session_state.inputs['Ethnicity'] = st.selectbox(
                'Ethnicity:',
                options=[0, 1, 2, 3],
                format_func=lambda x: ['Caucasian', 'African American', 'Asian', 'Other'][x],
                index=st.session_state.inputs['Ethnicity']
            )
            st.session_state.inputs['EducationLevel'] = st.selectbox(
                'Education Level:',
                options=[0, 1, 2, 3],
                format_func=lambda x: ['None', 'High School', "Bachelor's", 'Higher'][x],
                index=st.session_state.inputs['EducationLevel']
            )

        ### Lifestyle Factors
        with st.expander("Lifestyle Factors", expanded=True):
            st.session_state.inputs['BMI'] = st.number_input(
                'BMI:', min_value=15.0, max_value=40.0, 
                value=float(st.session_state.inputs['BMI']) if 15.0 <= float(st.session_state.inputs['BMI']) <= 40.0 else 15.0, 
                step=0.1
            )
            st.session_state.inputs['Smoking'] = st.radio('Smoking (0: No, 1: Yes):', [0, 1], index=st.session_state.inputs['Smoking'])
            st.session_state.inputs['AlcoholConsumption'] = st.number_input(
                'Alcohol Consumption (units per week):', min_value=0, max_value=20, 
                value=int(st.session_state.inputs['AlcoholConsumption']) if 0 <= int(st.session_state.inputs['AlcoholConsumption']) <= 20 else 0
            )
            st.session_state.inputs['PhysicalActivity'] = st.number_input(
                'Physical Activity (hours per week):', min_value=0, max_value=10, 
                value=int(st.session_state.inputs['PhysicalActivity']) if 0 <= int(st.session_state.inputs['PhysicalActivity']) <= 10 else 0
            )
            st.session_state.inputs['DietQuality'] = st.number_input(
                'Diet Quality (score):', min_value=0, max_value=10, 
                value=int(st.session_state.inputs['DietQuality']) if 0 <= int(st.session_state.inputs['DietQuality']) <= 10 else 0
            )
            st.session_state.inputs['SleepQuality'] = st.number_input(
                'Sleep Quality (score):', min_value=4, max_value=10, 
                value=int(st.session_state.inputs['SleepQuality']) if 4 <= int(st.session_state.inputs['SleepQuality']) <= 10 else 4
            )

        ### Medical History
        with st.expander("Medical History", expanded=True):
            st.session_state.inputs['FamilyHistoryAlzheimers'] = st.radio(
            "Family history of Alzheimer's Disease (0: No, 1: Yes):",
            [0, 1], index=st.session_state.inputs['FamilyHistoryAlzheimers']
            )
            st.session_state.inputs['CardiovascularDisease'] = st.radio(
            "Presence of cardiovascular disease (0: No, 1: Yes):",
            [0, 1], index=st.session_state.inputs['CardiovascularDisease']
            )
            st.session_state.inputs['Diabetes'] = st.radio(
            "Presence of diabetes (0: No, 1: Yes):",
            [0, 1], index=st.session_state.inputs['Diabetes']
            )
            st.session_state.inputs['Depression'] = st.radio(
            "Presence of depression (0: No, 1: Yes):",
            [0, 1], index=st.session_state.inputs['Depression']
            )
            st.session_state.inputs['HeadInjury'] = st.radio(
            "History of head injury (0: No, 1: Yes):",
            [0, 1], index=st.session_state.inputs['HeadInjury']
            )
            st.session_state.inputs['Hypertension'] = st.radio(
            "Presence of hypertension (0: No, 1: Yes):",
            [0, 1], index=st.session_state.inputs['Hypertension']
            )

        ### Clinical Measurements
        with st.expander("Clinical Measurements", expanded=True):
            st.session_state.inputs['SystolicBP'] = st.slider(
            'Systolic Blood Pressure (mmHg):', min_value=90, max_value=180, value=int(st.session_state.inputs['SystolicBP'])
            )
            st.session_state.inputs['DiastolicBP'] = st.slider(
            'Diastolic Blood Pressure (mmHg):', min_value=60, max_value=120, value=int(st.session_state.inputs['DiastolicBP'])
            )
            st.session_state.inputs['CholesterolTotal'] = st.slider(
            'Total Cholesterol (mg/dL):', min_value=150.0, max_value=300.0, value=float(st.session_state.inputs['CholesterolTotal']) if 150.0 <= float(st.session_state.inputs['CholesterolTotal']) <= 300.0 else 150.0
            )
            st.session_state.inputs['CholesterolLDL'] = st.slider(
            'LDL Cholesterol (mg/dL):', min_value=50, max_value=200, value=int(st.session_state.inputs['CholesterolLDL']) if 50 <= int(st.session_state.inputs['CholesterolLDL']) <= 200 else 50
            )
            st.session_state.inputs['CholesterolHDL'] = st.slider(
            'HDL Cholesterol (mg/dL):', min_value=20, max_value=100, value=int(st.session_state.inputs['CholesterolHDL']) if 20 <= int(st.session_state.inputs['CholesterolHDL']) <= 100 else 20
            )
            st.session_state.inputs['CholesterolTriglycerides'] = st.slider(
            'Triglycerides (mg/dL):', min_value=50, max_value=400, value=int(st.session_state.inputs['CholesterolTriglycerides']) if 50 <= int(st.session_state.inputs['CholesterolTriglycerides']) <= 400 else 50
            )

        ### Cognitive and Functional Assessments
        with st.expander("Cognitive and Functional Assessments", expanded=True):
            st.session_state.inputs['MMSE'] = st.slider(
            'Mini-Mental State Examination (MMSE) score:', min_value=0.0, max_value=30.0, value=st.session_state.inputs['MMSE']
            )
            st.session_state.inputs['FunctionalAssessment'] = st.slider(
            'Functional Assessment score:', min_value=0.0, max_value=10.0, value=st.session_state.inputs['FunctionalAssessment']
            )
            st.session_state.inputs['MemoryComplaints'] = st.radio(
            'Memory Complaints (0: No, 1: Yes):', [0, 1], index=st.session_state.inputs['MemoryComplaints']
            )
            st.session_state.inputs['BehavioralProblems'] = st.radio(
            'Behavioral Problems (0: No, 1: Yes):', [0, 1], index=st.session_state.inputs['BehavioralProblems']
            )
            st.session_state.inputs['ADL'] = st.slider(
            'Activities of Daily Living (ADL) score:', min_value=0.0, max_value=10.0, value=st.session_state.inputs['ADL']
            )

        ### Symptoms
        with st.expander("Symptoms", expanded=True):
            st.session_state.inputs['Confusion'] = st.radio(
            'Confusion (0: No, 1: Yes):', [0, 1], index=st.session_state.inputs['Confusion']
            )
            st.session_state.inputs['Disorientation'] = st.radio(
            'Disorientation (0: No, 1: Yes):', [0, 1], index=st.session_state.inputs['Disorientation']
            )
            st.session_state.inputs['PersonalityChanges'] = st.radio(
            'Personality Changes (0: No, 1: Yes):', [0, 1], index=st.session_state.inputs['PersonalityChanges']
            )
            st.session_state.inputs['DifficultyCompletingTasks'] = st.radio(
            'Difficulty Completing Tasks (0: No, 1: Yes):', [0, 1], index=st.session_state.inputs['DifficultyCompletingTasks']
            )
            st.session_state.inputs['Forgetfulness'] = st.radio(
            'Forgetfulness (0: No, 1: Yes):', [0, 1], index=st.session_state.inputs['Forgetfulness']
            )

        submit_button = st.form_submit_button(label='Make Prediction')

    if submit_button:
        def prediction(inputs):
            # Ensure all values are float or int as required by the model
            data = []
            for v in inputs.values():
                try:
                    data.append(float(v))
                except ValueError:
                    data.append(0.0)
            pred = st.session_state.model.predict([data])
            return pred[0]

        dia_prediction = prediction(st.session_state.inputs)
        if dia_prediction == 0:
            #st.success(st.session_state.inputs)
            st.success('You are not at risk of Alzheimer\'s disease')
        elif dia_prediction == 1:
            #st.success(st.session_state.inputs)
            st.error('You are of high risk of Alzheimer\'s disease')
