import openai

# Replace with your OpenAI API key
api_key = "####"

# Initialize the OpenAI API client with your API key
openai.api_key = api_key

def generate_nutrition_info(food_item):
    model = "text-davinci-002"

    # Construct a prompt for GPT-3.5
    prompt = f"Given a food item, provide its nutritional information in the following format:\n"
    prompt += f"Enter a food item: Apple\n"
    prompt += f"Nutrition info for Apple:\n"
    prompt += "Calories: 52\n"
    prompt += "Serving Size: 100g\n"
    prompt += "Total Fat: 0.2g\n"
    prompt += "Saturated Fat: 0.03g\n"
    prompt += "Protein: 0.3g\n"
    prompt += "Sodium: 1mg\n"
    prompt += "Potassium: 107mg\n"
    prompt += "Cholesterol: 0mg\n"
    prompt += "Total Carbohydrates: 14g\n"
    prompt += "Fiber: 2.4g\n"
    prompt += "Sugar: 10g\n"
    prompt += f"\nNow, your turn:\n"
    prompt += f"Enter a food item: {food_item}\n"

    # Generate a response from the GPT-3.5 model
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,  # Adjust as needed based on the desired response length
        temperature=0.3   # Lower temperature will make output more focused and deterministic
    )

    # Extract the nutrition information from the GPT-3.5 response
    nutrition_info = response.choices[0].text.strip()

    return nutrition_info

# Get user input for a food item
food_item = input("Enter a food item: ")

# Generate nutrition information using GPT-3.5
nutrition_info = generate_nutrition_info(food_item)

# Print the generated nutrition information
print(nutrition_info)
