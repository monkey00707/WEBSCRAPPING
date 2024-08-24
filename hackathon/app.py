from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df=pd.read_csv("data.csv")
def get_data_by_key(key):
    if "arraylist" in key:
        return df["arraylist"][0]
    elif "string" in key:
        return df["string"][0]
    elif "linkedhashset" in key:
        return df["linkedhashset"][0]
    elif "stack" in key:
        return df["stack"][0]
    elif "queue" in key:
        return df["queue"][0]
    elif "linked" in key or "linkedlist" in key:
        return df["linked"][0]
    elif "tree" in key:
        return df["tree"][0]
    elif "graph" in key:
        return df["graph"][0]
    elif "hash" in key:
        return df["hash"][0]
    elif "heap" in key:
        return df["heap"][0]
    elif "array" in key:
        return df["array"][0]
    elif "vector" in key:
        return df["vector"][0]
    elif "hashset" in key:
        return df["hashset"][0]
    elif "priority queue" in key:
        return df["priority_queue"][0]
    elif "deque" in key:
        return df["deque"][0]
    elif "treeset" in key:
        return df["treeset"][0]
    
    else:
        return "Key not found"
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        key = request.form['key']
        
        value = get_data_by_key(key)
        if value:
            return render_template('result.html', key=key, value=value)
        else:
            return render_template('result.html', key=key, value="No data found for the provided key.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
