from flask import Flask,request,jsonify, render_template
import re
import spacy
import pickle
import urllib.request
import pickle
import questions

import PyPDF2

model = pickle.load(open('cv.pkl','rb'))

app = Flask(__name__)



@app.route('/cv',methods=['POST'])
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
            dict_data[ent.label_.upper()]=[str(ent.text).lower()]
        else:
            dict_data[ent.label_.upper()].append(str(ent.text).lower())
        dict_data[ent.label_.upper()]=list(set(dict_data[ent.label_.upper()]))    
    #print(f"{ent.label_.upper():{30}}-{ent.text}")
    



    ques=[]
    ques_fillup=[]
    if "SKILL" in dict_data:
        l1=list(set(dict_data['SKILL']))
        dict_question=questions.question_datas
        dict_question_fill=questions.question_fillup
        i=0
        import random
# generating a random integer between 0 and 9 without using a loop


        while i<10:
            if 'java'in l1:
                randomNumber = random.randint(0, 9)
                ques.append(dict_question['java'][randomNumber])
                i=i+1
            if i==10:
                break
            if 'python' in l1:
                randomNumber = random.randint(0, 9)
                ques.append(dict_question['python'][randomNumber])
                i=i+1
            if i==10:
                break
            if 'html' in l1 or 'web' in l1 or 'web app' in l1 :
                randomNumber = random.randint(0, 9)
                ques.append(dict_question['web'][randomNumber])
                i=i+1
            if i==10:
                break
            if 'ml' in l1 or 'machine learning' in l1 or 'm.l' in l1 :
                randomNumber = random.randint(0, 9)
                ques.append(dict_question['ml'][randomNumber])
                i=i+1    
            if i==10:
                break    
            if 'ml' in l1 or 'machine learning' in l1 or 'm.l' in l1 :
                randomNumber = random.randint(0, 9)
                ques.append(dict_question['ml'][randomNumber])
                i=i+1  
            if i==10:
                break  
        i=0
        while i<10:
            if 'java'in l1:
                randomNumber = random.randint(0, 9)
                ques_fillup.append(dict_question_fill['java'][randomNumber])
                i=i+1
            if i==10:
                break
            if 'python' in l1:
                randomNumber = random.randint(0, 9)
                ques_fillup.append(dict_question_fill['python'][randomNumber])
                i=i+1
            if i==10:
                break
            if 'html' in l1 or 'web' in l1 or 'web app' in l1 :
                randomNumber = random.randint(0, 9)
                ques_fillup.append(dict_question_fill['web'][randomNumber])
                i=i+1
            if i==10:
                break
            if 'ml' in l1 or 'machine learning' in l1 or 'm.l' in l1 :
                randomNumber = random.randint(0, 9)
                ques_fillup.append(dict_question_fill['ml'][randomNumber])
                i=i+1    
            if i==10:
                break    
            if 'ml' in l1 or 'machine learning' in l1 or 'm.l' in l1 :
                randomNumber = random.randint(0, 9)
                ques_fillup.append(dict_question_fill['ml'][randomNumber])
                i=i+1  
            if i==10:
                break


    dict_data['ques']=ques
    dict_data['ques_f']=ques_fillup


                









    return jsonify({'data': dict_data})

@app.route('/question')
def question():
    dict_data={}
    top_skill=request.form.get("skill")
    if top_skill=="java":
        dict_data={}
        dict_data['Q1']={"Question":"Number of primitive data types in Java are?","Option":["6","7","8","9"],"Correct":["8"]}
        dict_data['Q2']={"Question":"What is the size of float and double in java?","Option":["32 and 32","32 and 64","64 and 64","64 and 32"],"Correct":["32 and 64"]}
    return(jsonify(dict_data))    


if __name__ == '__main__':
    app.run(debug=True,port=5000)


