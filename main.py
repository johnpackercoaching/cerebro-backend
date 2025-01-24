from flask import Flask, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)


@app.route("/send", methods=["POST"])
def handle_post():
    data = request.get_json()
    # Get JSON data from the request
    if "message" in data:
        message = data["message"]
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[{"role": "user", "content": "write a haiku about ai"}],
        )

        print(completion.choices[0].message)
        return jsonify(
            {
                "received_messages": message,
                "response": completion.choices[0].message.content,
            }
        )
    else:
        return jsonify({"error": "No messages field provided"}), 400


if __name__ == "__main__":
    app.run(debug=True)
