import os

# Sample HTML content with dark-themed text box and copy button
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Page</title>
    <style>
        body {
            background-color: #333;
            color: #fff;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        textarea {
            margin: 20px;
            width: 100%;
            max-width: 800px;
            height: 500px;
            min-height: 200px;
            background-color: #444;
            color: #fff;
            border: 1px solid #666;
            padding: 10px;
            margin-bottom: 10px;
            box-sizing: border-box;
            resize: none;
        }
        button {
            background-color: #555;
            color: #fff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }
        button:hover {
            background-color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <textarea id="code" readonly>
import os
from openai import OpenAI

client = OpenAI(
    api_key="KEY",
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "(a) Build Two different decision trees for the given data set, one tree by splitting the space using information gain and the other tree using Gini index. Conclude which gives the correct classification by taking some test data. Use 75% of the given data for training. Give code alone",
        }
    ],
    model="gpt-3.5-turbo",
)

print(response.choices[0].message.content)
        </textarea>
        <button onclick="copyCode()">Copy Code</button>
    </div>
    <script>
        function copyCode() {
            var code = document.getElementById('code').value;
            var textarea = document.createElement("textarea");
            textarea.textContent = code;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand("copy");
            document.body.removeChild(textarea);
        }
    </script>
</body>
</html>
"""

def write_html_file():
    with open("index.html", "w") as file:
        file.write(html_content)

def serve_website():
    # Change directory to the location of the HTML file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Start a simple HTTP server on port 80
    os.system("python3 -m http.server 80")

if __name__ == "__main__":
    write_html_file()
    serve_website()
