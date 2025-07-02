from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Simple Web Calculator</h2>
        <form action="/calculate" method="get">
            <input name="a" type="number" step="any" required>
            <select name="op">
                <option value="add">+</option>
                <option value="sub">-</option>
                <option value="mul">*</option>
                <option value="div">/</option>
            </select>
            <input name="b" type="number" step="any" required>
            <button type="submit">Calculate</button>
        </form>
    '''

@app.route('/calculate')
def calculate():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        op = request.args.get('op')
        
        if op == 'add':
            result = a + b
        elif op == 'sub':
            result = a - b
        elif op == 'mul':
            result = a * b
        elif op == 'div':
            if b == 0:
                return "Cannot divide by zero."
            result = a / b
        else:
            return "Invalid operation."
        
        return f"<h3>Result: {result}</h3><a href='/'>Back</a>"

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
