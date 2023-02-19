from flask import Flask, render_template, request, session, redirect, url_for 
from flask_wtf import FlaskForm
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename
from wtforms import RadioField, SubmitField 
import cgi, os
import cgitb; cgitb.enable()
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = 'Uploads'
app.config['MAX_CONTENT_PATH'] = 50000000

class InfoForm(FlaskForm): 
  symptom1 = RadioField("How often are you unable to keep your mind on a task at hand?", choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField('Submit') 
  symptom2 = RadioField("How often do you find yourself forgetting things/tasks and losing items?", choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField('Submit')
  symptom3 = RadioField("How often do you find yourself excessively moving and talking in situations when it may not be appropriate?", choices = [('op1','Never'),('op2',"Sometimes"),('op3','Often'), ('op4','Always')])
  submit = SubmitField("Submit")
  symptom4 = RadioField("How often do you fidget in your seat or unnecessarily move?",choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField("Submit")
  symptom5 = RadioField("How often do you find yourself worrying about or fearing everyday situations?",choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField("Submit")
  symptom6 = RadioField("Have you experienced a faster heart rate, rapid breathing, sweating, or feeling tired as a result of being worried or frightened about a certain situation?",choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField("Submit")
  symptom7 = RadioField("How often do you find yourself feeling constantly tired or weak on a consistent basis (across days when you’re not sick)?",choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField("Submit")
  symptom8 = RadioField("How often do you find yourself being overly-tired during the day and wanting to sleep, interfering with your normal daily activities?",choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField("Submit")
  symptom9 = RadioField("Roughly, how often do you actively participate in your hobbies per week?",choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField("Submit")
  symptom10 = RadioField("How often do you find yourself withdrawing from social situations/activities?",choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField("Submit")
  symptom11 = RadioField("How often do you experience negative emotions and thoughts in a day?",choices = [('op1','Never'),('op2','Sometimes'),('op3','Often'),('op4','Always')])
  submit = SubmitField("Submit")
  symptom12 = RadioField("Rate your confidence level/self-esteem at the moment.",choices = [('op1','1'),('op2','4'),('op3','7'),('op4','10')])
  submit = SubmitField("Submit")

@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/diagnostictest', methods = ['GET','POST'])
def diagnostictest(): 
  symptom1 = False
  symptom2 = False
  symptom3 = False
  symptom4 = False
  symptom5 = False
  symptom6 = False
  symptom7 = False 
  symptom8 = False
  symptom9 = False 
  symptom10 = False 
  symptom11 = False
  symptom12 = False
  form = InfoForm()
  if form.validate_on_submit(): 
    session["symptom1"] = form.symptom1.data 
    session["symptom2"] = form.symptom2.data
    session["symptom3"] = form.symptom3.data
    session["symptom4"] = form.symptom4.data
    session["symptom5"] = form.symptom5.data
    session["symptom6"] = form.symptom6.data
    session["symptom7"] = form.symptom7.data
    session["symptom8"] = form.symptom8.data
    session["symptom9"] = form.symptom9.data
    session["symptom10"] = form.symptom10.data
    session["symptom11"] = form.symptom11.data
    session["symptom12"] = form.symptom12.data
    user_data = open('userdata.txt','w')
    user_data.write(form.symptom1.data) 
    user_data.write(form.symptom2.data)
    user_data.write(form.symptom3.data)
    user_data.write(form.symptom4.data)
    user_data.write(form.symptom5.data) 
    user_data.write(form.symptom6.data)
    user_data.write(form.symptom7.data)
    user_data.write(form.symptom8.data)
    user_data.write(form.symptom9.data) 
    user_data.write(form.symptom10.data)
    user_data.write(form.symptom11.data)
    user_data.write(form.symptom12.data)
    user_data.close()
    user_data = open("userdata.txt","r")
    user_data.seek(0)
    global data1
    data1 = user_data.read(3) 
    global data2
    data2 = user_data.read(3)
    global data3
    data3 = user_data.read(3)
    global data4
    data4 = user_data.read(3)
    global data5
    data5 = user_data.read(3)
    global data6
    data6 = user_data.read(3)
    global data7
    data7 = user_data.read(3)
    global data8
    data8 = user_data.read(3)
    global data9
    data9 = user_data.read(3)
    global data10
    data10 = user_data.read(3)
    global data11
    data11 = user_data.read(3)
    global data12
    data12 = user_data.read(3)
    user_data.close()
    return redirect(url_for('treatmentplan'))
  return render_template("diagnostictest.html", form = form)  
    
@app.route('/treatmentplan')
def treatmentplan():
  global attention
  attention = 0
  global hyperactivity
  hyperactivity = 0
  global nervousness
  nervousness = 0
  global fatigue
  fatigue = 0
  global interest
  interest = 0
  global mood 
  mood = 0
  global adhd
  adhd = False
  global anxiety
  anxiety = False
  global depression
  depression = False
  if data1 == "op3" or data1 == "op4": 
    attention = attention + 1
  if data2 == "op3" or data2 == "op4":
    attention = attention + 1
  if data3 == "op3" or data3 == "op4":
    hyperactivity = hyperactivity + 1
  if data4 == "op3" or data4 == "op4":
    hyperactivity = hyperactivity + 1
  if data5 == "op3" or data5 == "op4": 
    nervousness = nervousness +  1
  if data6 == "op3" or data6 == "op4":
    nervousness = nervousness + 1
  if data7 == "op3" or data7 == "op4":
    fatigue = fatigue + 1
  if data8 == "op3" or data8 == "op4":
    fatigue = fatigue + 1
  if data9 == "op1" or data9 == "op2": 
    interest = interest + 1
  if data10 == "op3" or data10 == "op4":
    interest = interest + 1
  if data11 == "op3" or data11 == "op4":
    mood = mood + 1 
  if data12 == "op1" or data12 == "op2":
    mood = mood + 1
  if attention + hyperactivity > 2:
    adhd = True
  if nervousness + fatigue > 2:
    anxiety = True
  if interest + mood > 2:
    depression = True
  return render_template("treatmentplan.html",attention=attention,hyperactivity=hyperactivity,nervousness=nervousness,fatigue=fatigue,interest=interest,mood=mood,adhd=adhd,anxiety=anxiety,depression=depression) 

@app.route('/fmriscan')
def fMRIscan():
   return render_template('fmriscan.html')
	
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
  disease = False
  if request.method == 'POST':
      f = request.files['filename']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))) 
      image = Image.open(f)
      arr=np.array(image)
      if arr.shape != 3:
        "This file type is not supported."
      if arr.shape[2] != 3:
        "This file type is not valid."
      if image.mode == "RGB":
        for x in arr:
          for pixel in x:
            if pixel[0] > 150:
              if pixel[1] < 60:
                if pixel[2] < 60:
                  disease = True
                  break
      else:
        print("Only RGB images are valid images to scan.")
      return render_template('scanresults.html', disease=disease)

@app.route('/scanresults/<image>')
def scanresults(image):
  print(image)
  return render_template('scanresults.html') 
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81) #port = '8080' if issue arises again
