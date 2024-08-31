# FitChronicle

FitChronicle is a comprehensive fitness planner application built with Streamlit. It provides users with personalized fitness and meal plans based on their inputs. The application utilizes the Claude AI API for generating fitness and meal plans, and offers the functionality to download these plans as a PDF file.

## Features

- **Personalized Fitness Plan:** Generates a weekly fitness plan tailored to the user's height, weight, age, fitness goals, and other inputs.
- **Meal Plan Generation:** Creates a detailed meal plan that includes breakfast, lunch, dinner, and snacks, based on dietary preferences and restrictions.
- **PDF Download:** Allows users to download their personalized fitness and meal plans as a combined PDF document.
- **Custom Styling:** Includes a gradient background, custom sidebar styling, and responsive design for a better user experience.

## Requirements

- Python 3.8+
- Streamlit
- Anthropoc API (Claude AI)
- Python-dotenv
- FPDF
- Any other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fitchronicle.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd fitchronicle
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

4. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file in the project root and add your Claude API key:**

   ```
   CLAUDE_API_KEY=your_claude_api_key_here
   ```

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Access the app in your web browser at:**

   ```
   http://localhost:8501
   ```

3. **Fill out the form in the sidebar with your personal fitness information and click "Get Personalized Fitness Plan".**

4. **Download the combined PDF containing your personalized fitness and meal plans using the provided download button.**

## Code Overview

- **`app.py`:** Main Streamlit application file containing the logic for fetching fitness and meal plans, styling, and PDF generation.
- **`requirements.txt`:** Lists the Python packages required to run the application.
- **`.env`:** Configuration file to store environment variables such as API keys.

## Troubleshooting

- **Dependency Errors:** Ensure all dependencies are correctly listed in `requirements.txt` and that your virtual environment is activated.
- **API Key Issues:** Verify that your Claude API key is correctly set in the `.env` file and that it's valid.

## Contributors
   Sarim Ul Haq  Gmail: sarimulhaq331@gmail.com
   Mahnoor       Gmail: mah.syed04@gmail.com
