# FitChronicle 📓💪

FitChronicle is a comprehensive fitness planner designed to track your journey towards optimal health and performance. This Streamlit app allows users to input personal fitness details and receive personalized fitness and meal plans generated using Claude AI.

## Features

- **Personalized Fitness Plan**: Generates a detailed weekly fitness plan based on user inputs.
- **Personalized Meal Plan**: Provides a meal plan including breakfast, lunch, dinner, and snacks.
- **Customizable Inputs**: Users can specify height, weight, age, fitness goals, medical history, and more.
- **Enhanced Styling**: App features a gradient background, custom title, and styled sidebar inputs.

## Requirements

- Python 3.7 or higher
- Streamlit
- `anthropic` (for interacting with Claude AI)
- `python-dotenv` (for loading environment variables)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fitchronicle.git
   cd fitchronicle
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install required packages**:
   ```bash
   pip install streamlit anthropic python-dotenv
   ```

5. **Create a `.env` file** in the root directory of your project with the following content:
   ```ini
   CLAUDE_API_KEY=your_claude_api_key_here
   ```

6. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Open the app**: Navigate to the URL provided by Streamlit in your terminal (usually `http://localhost:8501`).

2. **Fill out the sidebar inputs**:
   - Enter your height, weight, age, medical history, fitness goals, and other details.
   - Specify dietary preferences, available time for exercise, and access to equipment.

3. **Get Personalized Plans**:
   - Click on the "Get Personalized Fitness Plan" button to generate your customized fitness and meal plans.

4. **View Results**: The app will display your personalized fitness and meal plans, formatted with clear headings and detailed recommendations.

## Configuration

- **API Key**: Ensure you have a valid Claude API key. Store it in the `.env` file as described in the Installation section.

- **CSS Customization**: The app includes custom CSS for styling. Modify the `st.markdown` section with your preferred styles if needed.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the existing style and passes all tests.


Happy fitness planning with FitChronicle! 💪📓
```

