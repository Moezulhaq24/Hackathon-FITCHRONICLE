import streamlit as st
import anthropic
import os
import re
from dotenv import load_dotenv
load_dotenv()

# cl_api_key = os.getenv("CLAUDE_API_KEY")
cl_api_key = st.secrets["CLAUDE_API_KEY"]
# Function to get response from Claude for fitness plan

from fpdf import FPDF
def format_schedule_as_heading(text):
    # Define a regular expression pattern to match the schedule format
    pattern = re.compile(r'(\w+day) - (.+?) (\d{1,2}:\d{2} [APM]{2}) - (\d{1,2}:\d{2} [APM]{2})')
    
    # Replace the matched schedule with Markdown heading
    formatted_text = re.sub(pattern, r'## \1 - \2', text)
    
    return formatted_text
# Function to create and save PDF
def save_to_pdf(response, filename):
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    
    # Set font and size
    pdf.set_font("Arial", size=12)
    
    # Add a cell for each line of the response
    for line in response.split('\n'):
        pdf.multi_cell(0, 10, line)
    
    # Save the PDF to a file
    pdf.output(filename)


def get_fitness_plan_response(prompt, api_key):
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4000,  # Adjust based on prompt length
        temperature=0,
        system=f"""
As an elite fitness trainer, please provide a detailed weekly fitness plan based on the following information. The plan should be organized by specific days of the week (e.g., Monday, Tuesday, etc.) and include the following:

Exercise Routine:

Warm-up: Include types and duration of warm-up exercises.
Main Workout: Specify exercises, sets, reps, and weights (if applicable) for each day.
Cool Down: Describe cool-down exercises and stretching routines.
Rest Days:

Clearly indicate which days are designated for rest or active recovery, and suggest appropriate activities if any.
Specific Goals:

Tailor the plan to meet the primary fitness goals specified: e.g., weight loss, muscle gain, improved endurance.
Equipment:

Mention any exercise equipment needed for each day or suggest alternative exercises if certain equipment is not available.
Progression:

Outline how the plan will progress over the weeks, including any planned increases in intensity or volume.
BMI Calculation:

Calculate the Body Mass Index (BMI) using the following information:
Height: {height} (cm)
Weight: {weight} (kg)
Provide recommendations based on the calculated BMI to adjust the fitness plan as necessary to align with the user's goals.""",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )
    return message.content[0].text

# Function to get response from Claude for meal plan
def get_meal_plan_response(prompt, api_key):
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4000,  # Adjust based on prompt length
        temperature=0,
        system=f"""
As a nutrition expert, please create a detailed meal plan based on the following diet requirements. The plan should cover all weekdays with a single set of meals that can be used for each day. The meal plan should include:

1. **Meal Structure**:
   - **Breakfast**: Include specific foods, portion sizes, and nutritional information.
   - **Lunch**: Provide detailed meal options, including ingredients and serving sizes.
   - **Dinner**: Describe complete dinner recipes with portion sizes and nutritional details.
   - **Snacks**: Suggest healthy snack options, including portion sizes and nutritional information.

2. **Dietary Goals**:
   - Ensure the meal plan meets the specified dietary goals such as balanced nutrition, calorie control, or specific macronutrient targets.

3. **Dietary Preferences and Restrictions**:
   - Adapt the meal plan to accommodate any dietary preferences or restrictions mentioned (e.g., vegetarian, vegan, gluten-free, etc.).

4. **Portion Sizes**:
   - Specify portion sizes for each meal and snack to align with the user's dietary needs.

5. **Rationale**:
   - Provide a brief explanation for each meal and snack choice, detailing how it contributes to overall nutrition and health goals.
""",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )
    return message.content[0].text

# Apply custom CSS for gradient background, title styling, and sidebar
st.markdown("""
    <style>
    /* Background gradient */
    .main {
        background: linear-gradient(to right, #00C9FF, #92FE9D); /* Cool ocean gradient */
        height: 100vh;
        padding: 2rem;
        color: #000000; /* Black text color */
    }
    
    /* Title styling */
    .title {
        font-family: 'Arial Black', sans-serif;
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        color: #000000; /* Black color */
        margin-top: 30px;
    }
    
    /* Input description styling */
    .input-description {
        font-size: 14px; /* Slightly larger font size */
        color: #333333; /* Dark gray color for better contrast */
        margin-bottom: 10px; /* Space below each description */
        line-height: 1.5; /* Increase line height for better readability */
        font-family: 'Arial', sans-serif; /* Use a clean, sans-serif font */
        padding: 5px; /* Add some padding for better spacing */
        border-left: 3px solid #FFA500; /* Add a colored left border for emphasis */
        background-color: #F9F9F9; /* Light gray background for the description area */
    }
    
    /* Sidebar styling */
    .sidebar-container {
        background-color: #2C2C2C !important; /* Darker gray for sidebar */
        color: #FFFFFF !important; /* White text color */
        padding: 1rem;
    }

    .sidebar-container h1, .sidebar-container h2, .sidebar-container h3 {
        color: #FFA500 !important; /* Orange color for headers */
    }

    .sidebar-container .stButton {
        background-color: #FFA500 !important; /* Orange button background */
        color: #FFFFFF !important; /* White button text */
    }

    .sidebar-container .stSelectbox, .sidebar-container .stNumberInput, .sidebar-container .stTextArea {
        background-color: #2C2C2C !important; /* Darker gray background */
        color: #FFFFFF !important; /* White text color */
    }

    .sidebar-container .stNumberInput input {
        background-color: #2C2C2C !important; /* Darker gray background for input */
        color: #FFFFFF !important; /* White text color */
    }

    .sidebar-container .stSelectbox select {
        background-color: #2C2C2C !important; /* Darker gray background for selectbox */
        color: #FFFFFF !important; /* White text color */
    }

    .sidebar-container .stTextArea textarea {
        background-color: #2C2C2C !important; /* Darker gray background for text area */
        color: #FFFFFF !important; /* White text color */
    }

    /* Specific styling for sidebar labels */
    .sidebar-label {
        font-size: 16px; /* Slightly larger font size */
        color: #FFA500 !important; /* Orange color for labels */
        font-weight: bold; /* Bold text */
    }
    </style>
    """, unsafe_allow_html=True)


# App Title (Styled with CSS)
st.markdown('<h1 class="title">FITCHRONICLE 📓💪</h1>', unsafe_allow_html=True)

# App Description
st.write("""
FitChronicle is a comprehensive fitness planner designed to track your journey towards optimal health and performance. 
This planner allows you to document daily workouts, set specific fitness goals, and monitor your progress over time. 
With sections dedicated to exercise routines, nutrition plans, and personal reflections, 
FitChronicle empowers you to stay focused, motivated, and organized.
Whether you're aiming to build muscle, lose weight, or improve overall wellness, 
FitChronicle provides the structure and inspiration you need to reach new heights in your fitness journey.
""")

# Sidebar Inputs
st.sidebar.header("Personal Fitness Information")
st.sidebar.write("Please fill all the given fields...")
height = st.sidebar.number_input("Height (in cm)")
st.sidebar.markdown('<p class="input-description">Enter your height. You can specify in centimeters.</p>', unsafe_allow_html=True)

weight = st.sidebar.number_input("Weight (in kg)")
st.sidebar.markdown('<p class="input-description">Enter your current weight. You can specify in kilograms.</p>', unsafe_allow_html=True)

age = st.sidebar.number_input("Age")
st.sidebar.markdown('<p class="input-description">Enter your age in years.</p>', unsafe_allow_html=True)

medical_history = st.sidebar.text_area("Relevant Medical History or Conditions")
st.sidebar.markdown('<p class="input-description">Mention any medical history or conditions that might affect your fitness routine, such as asthma, diabetes, or back pain.</p>', unsafe_allow_html=True)

primary_fitness_goals = st.sidebar.text_area("Primary Fitness Goals")
st.sidebar.markdown('<p class="input-description">Specify your main fitness goals, such as weight loss, muscle gain, or improved endurance.</p>', unsafe_allow_html=True)

current_fitness_level = st.sidebar.selectbox("Current Fitness Level", ["Beginner", "Intermediate", "Advanced"])
st.sidebar.markdown('<p class="input-description">Select your current fitness level based on your experience with exercise.</p>', unsafe_allow_html=True)

exercise_experience = st.sidebar.text_area("Exercise Experience")
st.sidebar.markdown('<p class="input-description">Briefly describe your past experience with exercise routines or sports.</p>', unsafe_allow_html=True)

dietary_preferences = st.sidebar.text_area("Dietary Restrictions or Preferences")
st.sidebar.markdown('<p class="input-description">Mention any dietary preferences, restrictions, or allergies, such as vegetarian, vegan, or lactose intolerance.</p>', unsafe_allow_html=True)

available_time = st.sidebar.text_area("Available Time for Exercise and Meal Prep")
st.sidebar.markdown('<p class="input-description">Indicate how much time you can dedicate daily or weekly to exercise and meal preparation.</p>', unsafe_allow_html=True)

access_to_equipment = st.sidebar.text_area("Access to Exercise Equipment or Gym Facilities")
st.sidebar.markdown('<p class="input-description">Describe any exercise equipment you have at home or whether you have access to a gym.</p>', unsafe_allow_html=True)

# Additional Inputs
stress_level = st.sidebar.selectbox("Stress Level", ["High", "Moderate", "Low"])
st.sidebar.markdown('<p class="input-description">Select your current stress level.</p>', unsafe_allow_html=True)

sleep_pattern = st.sidebar.text_area("Sleep Pattern")
st.sidebar.markdown('<p class="input-description">Describe your sleep pattern, including average hours of sleep and sleep quality.</p>', unsafe_allow_html=True)

body_type = st.sidebar.selectbox("Body Type", ["Ectomorph", "Mesomorph", "Endomorph"])
st.sidebar.markdown("""
    <p class="input-description">
        Select your body type. If you don't know what a body type is, please visit this website: 
        <a href="https://www.healthline.com/health/male-body-types" target="_blank">
            Healthline - Male Body Types
        </a>
    </p>
""", unsafe_allow_html=True)

daily_activity_level = st.sidebar.selectbox("Daily Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])
st.sidebar.markdown("""
    <p class="input-description">
        Select your daily activity level. If you don't know what daily activity levels are, please visit this website: 
        <a href="https://funnmedia.zendesk.com/hc/en-us/articles/360040360231-What-Are-Activity-Levels-and-How-Do-They-Work" target="_blank">
            What Are Activity Levels and How Do They Work
        </a>
    </p>
""", unsafe_allow_html=True)

# Generating a response from Claude based on user inputs
fitness_prompt = f"""
Height: {height}
Weight: {weight}
Age: {age}
Medical History: {medical_history}
Primary Fitness Goals: {primary_fitness_goals}
Current Fitness Level: {current_fitness_level}
Exercise Experience: {exercise_experience}
Dietary Preferences: {dietary_preferences}
Available Time: {available_time}
Access to Equipment: {access_to_equipment}
Stress Level: {stress_level}
Sleep Pattern: {sleep_pattern}
Body Type: {body_type}
Daily Activity Level: {daily_activity_level}
"""

meal_prompt = "Craft a detailed meal plan for breakfast, lunch, and dinner, ensuring balanced nutrition and optimal results. Include rationale behind each recommendation."

if st.sidebar.button("Get Personalized Fitness Plan"):
    api_key = os.getenv("CLAUDE_API_KEY")  # Ensure you've set your Claude API key as an environment variable
    
    # Fetch responses for each section
    fitness_response = get_fitness_plan_response(fitness_prompt, cl_api_key)
    meal_response = get_meal_plan_response(meal_prompt, cl_api_key)
    save_to_pdf(fitness_response, "Fitness_Plan.pdf")

# Save the meal response to a separate PDF file
    save_to_pdf(meal_response, "Meal_Plan.pdf")
    # Modify the response to ensure proper formatting
    fitness_response = fitness_response.replace("Based on the information provided, ", "")
    meal_response = meal_response.replace("Based on the information provided, ", "")

    # Adding headingsFT
    fitness_response = fitness_response.replace("BMI Calculation:", "### BMI Calculation:")
    fitness_response = fitness_response.replace("Weekly Fitness Plan:", "## Weekly Fitness Plan")
    fitness_response = fitness_response.replace("Monday", "**Monday**")
    fitness_response = fitness_response.replace("Tuesday", "**Tuesday**")
    fitness_response = fitness_response.replace("Wednesday", "**Wednesday**")
    fitness_response = fitness_response.replace("Thursday", "**Thursday**")
    fitness_response = fitness_response.replace("Friday", "**Friday**")
    fitness_response = fitness_response.replace("Saturday", "**Saturday**")
    fitness_response = fitness_response.replace("Sunday", "**Sunday**")

    fitness_response = fitness_response.replace("Equipment Needed:", "### Equipment Needed")
    fitness_response = fitness_response.replace("Progression:", "### Progression")
    fitness_response = fitness_response.replace("Additional Recommendations:", "### Additional Recommendations")

    # Adding headings

    
    meal_response = meal_response.replace("Weekday Meal Plan:", "## Weekday Meal Plan")
    meal_response = meal_response.replace("Breakfast:", "### Breakfast")
    meal_response = meal_response.replace("Lunch:", "### Lunch")
    meal_response = meal_response.replace("Dinner:", "### Dinner")
    meal_response = meal_response.replace("Snacks (choose two per day):", "### Snacks")
    #meal_response = re.sub(r"Snacks:(.*)", r"### Snacks\1", meal_response)

    
    
    st.markdown("### Your Personalized Fitness Plan", unsafe_allow_html=True)
    # st.markdown(bmi,unsafe_allow_html=True)
    st.markdown(fitness_response, unsafe_allow_html=True)
    st.markdown(meal_response, unsafe_allow_html=True)
