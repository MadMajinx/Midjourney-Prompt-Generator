# Midjourney-Prompt-Generator

Midjourney Prompt Generator is a versatile user interface (UI) script that assists in generating and enhancing prompts for generative AI art models like MidJourney, allowing users to draw inspiration and unleash their creativity. It is compatible with multiple platforms and operates independently.

## Availablity

This app is available as the following:

1. A Streamit App
2. A Discord Bot

## Features for Streamlit App
The app in full can be seen below:

![FullView](https://user-images.githubusercontent.com/121183743/230941046-1d7fe1f6-cec5-42fe-9c0f-aa7b7ece190c.png)

1.  Content Input
In this section i provide the functionality to the user to input a content idea around which ChatGPT can generate a prompt. However, in case of any lack of ideas or just to have fun the user can also opt to generate the idea randomly using ChatGPT.

![ContentView](https://user-images.githubusercontent.com/121183743/230941621-ce79985d-e6a2-42ad-b2b3-790d2ee38555.png)

2. Attributes Section
First of all I provide a slider to decide the randomness of the generated prompt using the hyperparameter i.e. Temperature. Higher the temperature value the higher the randomness and creativity and vice versa.

     Then there are multiple dropdown boxes to include various attributes for the image prompt such as style,color,lighting,material,quality etc.

![SlidersView](https://user-images.githubusercontent.com/121183743/230942218-3c75259b-c3c6-49ba-ae91-0fa3d56001be.png)

3. Idea Exclusion
There is also a section for the user if they want to tell ChatGPT to avoid any idea/content from the generated prompt

![ExclusionView](https://user-images.githubusercontent.com/121183743/230942354-7e251a03-063b-46cb-a1a7-9aaddf118e7a.png)

4. Generator Button
Finally after the user has chosen all the necessary details above, ChatGPT generates the prompt and adds the attributes to the prompt in the end.

## Installation & Startup (Streamlit App)
### Prerequisites
To run the script, you need the following:
1. Python3
2. OpenAi library
3. Streamlit

### To run the script
All you need to do is run the PromptGenerator script as follows:
streamlit run PromptGenerator.py

