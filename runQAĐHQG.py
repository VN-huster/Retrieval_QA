from flask import Flask, render_template, request, redirect, url_for
import response
import process_input
app = Flask(__name__)

@app.route('/GPT')
def index():
    return render_template('index.html')

@app.route('/GPT_handle', methods=['POST'])
def process_user_input():
    data = request.get_json()
    user_input = data.get('user_input')

    # Process user input as needed
    result = response.answer(user_input)

    print(result)
    result = result.replace("\n", "<br/>")

    answer = process_input.answer_base_content(user_input, result)
    # Return a plain text response
    if answer.strip() == "Tôi không có thông tin.":
        return process_input.sort_score(user_input)
    return answer + "<br/><br/>" + "Trích: " + result.split("<br/>")[0]


@app.route('/VietCuna')
def another_page():
    # Add the logic for rendering another page here
    return render_template('index2.html')


@app.route('/VietCuna_handle', methods=['POST'])
def process_another_user_input():
    data = request.get_json()
    user_input = data.get('user_input')

    # Process user input on the /Another page
    return "Hello " + user_input


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8705)
