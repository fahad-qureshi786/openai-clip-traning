import openai
import base64

openai.api_key = "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"

# Open the image file
with open("download.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Specify the prompt and the image data
prompt = "Complete the sentence:"
data = {
    "prompt": prompt,
    "image": encoded_string,

}

# Generate a response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    data=data
)

# Print the response
print(response["choices"][0]["text"])
