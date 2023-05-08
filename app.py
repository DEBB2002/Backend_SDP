from flask import Flask,request,jsonify, render_template
import re
import spacy
import pickle
import urllib.request
import pickle


import PyPDF2

model = pickle.load(open('cv.pkl','rb'))

app = Flask(__name__)



   
@app.route('/cv')
def get_users():
    
    if 'file' not in request.files:
        return 'No file uploaded', 400

    # Get file object from request
    file = request.files['file']

    # Check if file is a pdf
    if file.filename.split('.')[-1].lower() != 'pdf':
        return 'File must be a pdf', 400

    # Read pdf file
    pdf = PyPDF2.PdfReader(file)
    text = ''

    # Iterate through all pages and extract text
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        text += page.extract_text()

   

    
    
    
    
    text.replace(" ", "")
    print("Using jsonify")
    cv=request.files.getlist('file')
    file=cv[0]
    

    

    #r=request.form.get("text")
    print(text)
    doc=model(text)
    #m1=load_nlp(text)
    #from spacy import displacy
    #displacy.render(m1, style="ent", jupyter=True)
    dict_data={}
    
    for ent in doc.ents:
        if ent.label_.upper() not in dict_data:
            dict_data[ent.label_.upper()]=[str(ent.text)]
        else:
            dict_data[ent.label_.upper()].append(str(ent.text))
    #print(f"{ent.label_.upper():{30}}-{ent.text}")
            
    return jsonify({'data': dict_data})
 

if __name__ == '__main__':
    app.run(debug=True,port=5000)


