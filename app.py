from flask import Flask, render_template, request, send_file
import generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_data():
    # Get selected data fields
    final_data = [key for key in request.form if key != 'number_of_data' and key != 'file_format']
    number_of_data = int(request.form.get('number_of_data'))
    file_format = request.form.get('file_format')

    if file_format == 'sql':
        generator.random_data_to_sql(final_data, number_of_data)
        return send_file('random_generated_data.sql', as_attachment=True)
    elif file_format == 'csv':
        generator.random_data_to_csv(final_data, number_of_data)
        return send_file('random_generated_data.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
