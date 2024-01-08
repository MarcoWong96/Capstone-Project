import streamlit as st
import pandas as pd
import joblib
import numpy as np
import shap
import matplotlib.pyplot as plt

# Load your trained model
loaded_model = joblib.load('final_model.pkl')  
loaded_scaler = joblib.load('scaler.pkl') 

# Set title
st.title("Projecting Player Valuation using Statistics")

# Descriptor
st.write('This app will predict a football players valuation. Please adjust the statistics on the left to required statistics.')

# Set X_train_select
df_columns = ['Comp_Premier League', 'Team_Middle', 'Team_Top', 'Age', 'Starts',
       '90s', 'Goals', 'Shots', 'PasTotCmp%', 'PasMedCmp%', 'SCA',
       'ScaPassLive', 'GCA', 'TouAtt3rd', 'TouAttPen', 'TouLive', 'Rec',
       'Recov', 'AerWon', '2023']

# Data Dictionary
# Define and display the data dictionary
data_dictionary = {
    'Comp_Premier League': 'Whether the player plays in the Premier League (1 if true, 0 if false)',
    'Team_Middle': 'Whether the player belongs to a middle-tier team (1 if true, 0 if false)',
    'Team_Top': 'Whether the player belongs to a top-tier team (1 if true, 0 if false)',
    'Age': 'The age of the player',
    'Starts': 'Number of games the player started',
    '90s': 'Number of 90-minute intervals the player participated in',
    'Goals': 'Number of goals scored by the player per 90',
    'Shots': 'Number of shots taken by the player per 90',
    'PasTotCmp%': 'Pass completion percentage of total passes',
    'PasMedCmp%': 'Pass completion percentage of medium-length passes',
    'SCA': 'Shot creating actions by the player',
    'ScaPassLive': 'Shot creating actions from live passes',
    'GCA': 'Goal creating actions by the player',
    'TouAtt3rd': 'Number of ball touches in the attacking third',
    'TouAttPen': 'Number of ball touches in the penalty area',
    'TouLive': 'Number of live ball touches',
    'Rec': 'Number of recoveries by the player',
    'Recov': 'Number of loose balls recovered',
    'AerWon': 'Number of aerial duels won by the player',
    '2023': 'Whether it is the year 2023 (1 if true, 0 if false)',
}

# Function to scale user_data
def scale_user_input(user_input):
    # Create a DataFrame with original column names
    user_input_df = pd.DataFrame(user_input, columns=df_columns)
    
    # Scale user input using the loaded scaler
    scaled_input = loaded_scaler.transform(user_input_df)
    return scaled_input

def main():
    st.title('Player Valuation Predictor')

    # Collect user input
    st.sidebar.title('Player Statistics')

    # Display checkbox title
    st.sidebar.write('Check if applies')

    # Create checkboxes for binary features
    feature3 = st.sidebar.checkbox('Comp_Premier League')
    feature4 = st.sidebar.checkbox('Team_Middle')
    feature5 = st.sidebar.checkbox('Team_Top')
    feature20 = st.sidebar.checkbox('2023')

    # Display input sliders
    st.sidebar.write('Slider scale')

    # Create input fields for numeric features
    feature1 = st.sidebar.slider('Age', min_value=18, max_value=40, value=25)
    feature2 = st.sidebar.slider('Starts', min_value=0, max_value=38, value=20)
    feature6 = st.sidebar.slider('90s', min_value=0, max_value=38, value=20)
    feature7 = st.sidebar.slider('Goals', min_value=0, max_value=20, value=5)
    feature8 = st.sidebar.slider('Shots', min_value=0, max_value=5, value=1)
    feature9 = st.sidebar.slider('PasTotCmp%', min_value=0, max_value=100, value=50)
    feature10 = st.sidebar.slider('PasMedCmp%', min_value=0, max_value=100, value=50)
    feature11 = st.sidebar.slider('SCA', min_value=0, max_value=20, value=10)
    feature12 = st.sidebar.slider('ScaPassLive', min_value=0, max_value=20, value=10)
    feature13 = st.sidebar.slider('GCA', min_value=0, max_value=20, value=5)
    feature14 = st.sidebar.slider('TouAtt3rd', min_value=0, max_value=100, value=15)
    feature15 = st.sidebar.slider('TouAttPen', min_value=0, max_value=50, value=10)
    feature16 = st.sidebar.slider('TouLive', min_value=0, max_value=150, value=40)
    feature17 = st.sidebar.slider('Rec', min_value=0, max_value=150, value=30)
    feature18 = st.sidebar.slider('Recov', min_value=0, max_value=35, value=10)
    feature19 = st.sidebar.slider('AerWon', min_value=0, max_value=20, value=5)

    # Create a callback for live updates
    @st.cache_data()
    def predict_valuation(user_input):
            scaled_user_input = scale_user_input(user_input)
            prediction = loaded_model.predict(scaled_user_input)
            return prediction

   # Create a DataFrame with the user input
    user_input = np.array([1 if feature3 else 0, 1 if feature4 else 0, 1 if feature5 else 0,
                           feature1, feature2, feature6, feature7, feature8, feature9,
                           feature10, feature11, feature12, feature13, feature14, feature15,
                           feature16, feature17, feature18, feature19, 1 if feature20 else 0]).reshape(1, -1)

    # Display the prediction
    st.success(f'Predicted Valuation: {np.round(np.exp(predict_valuation(user_input)[0])/1_000_000, 1)} Million €')

    # Write description
    st.write('The below graph shows the effect of each statistic on the players valuation.')
    # Generate SHAP force plot based on the user input
    explainer = shap.Explainer(loaded_model)
    shap_values = explainer.shap_values(user_input)
    
    # Function to generate SHAP plot
    def generate_shap_plot(user_input):
        explainer = shap.Explainer(loaded_model)
        shap_values = explainer.shap_values(user_input)

        # Create a summary plot of SHAP values
        fig, ax = plt.subplots()
        shap.summary_plot(shap_values, features=user_input, feature_names=df_columns, show=False)
        st.pyplot(fig)

    generate_shap_plot(user_input)  # Initial SHAP plot based on default values


    # Use Streamlit's "st.slider" to detect changes in the slider values
    if st.button('Update SHAP Plot'):
        user_input = np.array([1 if feature3 else 0, 1 if feature4 else 0, 1 if feature5 else 0,
                               feature1, feature2, feature6, feature7, feature8, feature9,
                               feature10, feature11, feature12, feature13, feature14, feature15,
                               feature16, feature17, feature18, feature19, 1 if feature20 else 0]).reshape(1, -1)

        generate_shap_plot(user_input)  # Update SHAP plot on button click
    
    # Put Data Dictionary
    st.write('### Data Dictionary')
    for feature, description in data_dictionary.items():
        st.write(f"- **{feature}:** {description}")
if __name__ == "__main__":
    main()




