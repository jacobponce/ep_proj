from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_text = request.form['input_text']
        # Process the input and generate the output
        output_text = process_input(input_text)
        return render_template('index.html', output_text=output_text)
    return render_template('index.html')

def process_input(input_text):
    # Add your logic to process the input and generate the output
    # For example, you can perform some calculations or call an external API
    output_text = input_text.upper()
    return output_text

if __name__ == '__main__':
    app.run(debug=True)
