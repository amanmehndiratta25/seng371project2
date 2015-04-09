from flask import Flask, render_template, request, redirect
from app import app
import GraphResults

@app.route('/')
def index():
    return render_template('page.html')
    
@app.route('/graph', methods=['POST'])
def graph():
    
    datasets = {}

    try:
        data = request.files['file1']
        desc = request.form['file1desc']
        if data and desc:
            datasets[desc] = data.read()
    except:
        pass
    
    try:
        data = request.files['file2']
        desc = request.form['file2desc']
        if data and desc:
            datasets[desc] = data.read()
    except:
        pass
        
    try:
        data = request.files['file3']
        desc = request.form['file3desc']
        if data and desc:
            datasets[desc] = data.read()
    except:
        pass
        
    try:
        data = request.files['file4']
        desc = request.form['file4desc']
        if data and desc:
            datasets[desc] = data.read()
    except:
        pass
    
    return render_template('graph.html', results = GraphResults.graph_results(datasets))
    

