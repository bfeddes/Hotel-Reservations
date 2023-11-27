from flask import Flask, render_template 

# Create an instance of Flask class
app = Flask(__name__)

# Default route when application loads
@app.route('/')

# Function to render the HTML template
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)