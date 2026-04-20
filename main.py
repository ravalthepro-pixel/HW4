from openai import OpenAI

# Create client (uses your API key from environment variable)
client = OpenAI()

def run_experiment(prompt, temperature, system_message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content


# Prompts to test
prompts = [
    "Explain recursion simply.",
    "Explain recursion like I'm 5 years old.",
    "Explain recursion in a technical way."
]

# Different settings to experiment with
temperatures = [0.2, 0.7, 0.9]

system_messages = [
    "You are a helpful assistant.",
    "You are a sarcastic assistant.",
    "You are a strict professor."
]

# Save results to file
with open("results.txt", "w") as f:
    for system in system_messages:
        f.write(f"\n===== System: {system} =====\n\n")
        print(f"\n===== System: {system} =====")

        for temp in temperatures:
            f.write(f"\n--- Temperature: {temp} ---\n\n")
            print(f"\n--- Temperature: {temp} ---")

            for prompt in prompts:
                result = run_experiment(prompt, temp, system)

                # Print to terminal
                print(f"\nPrompt: {prompt}")
                print(f"Response: {result}")

                # Save to file
                f.write(f"Prompt: {prompt}\n")
                f.write(f"Response: {result}\n\n")

print("\nDone! Results saved to results.txt")
