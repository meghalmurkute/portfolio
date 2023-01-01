from flask import Flask, render_template, redirect, request
from urllib.request import urlopen
import re as r
import sqlite3

app = Flask(__name__)

@app.route('/')
def portfolio():
   ip = str(urlopen('http://checkip.dyndns.com/').read())
   ip_add = r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(ip).group(1)
   return render_template("welcome.html")

@app.route('/homePage')
def homePage():
   return render_template("portfolio.html")

@app.route('/linkedin')
def linkedin():
   return redirect('https://in.linkedin.com/in/meghalmurkute')

@app.route('/github')
def github():
   return redirect('https://github.com/meghalmurkute')

@app.route('/instagram')
def instagram():
   return redirect('https://www.instagram.com/meghalmurkute/')

@app.route('/facebook')
def facebook():
   return redirect('https://www.facebook.com/meghal.murkute.5')

@app.route('/twitter')
def twitter():
   return redirect('https://twitter.com/meghalmurkute')

@app.route('/youtube')
def youtube():
   return redirect('https://www.youtube.com/c/MeghalMurkute')

@app.route('/resume')
def resume():
   return redirect('https://drive.google.com/file/d/1F6zrvaOZG4Y3rQds4LGakl_ofN3LbX-3/view?usp=share_link')

@app.route('/researchPaper')
def researchPaper():
   return redirect('https://iaraedu.com/about-journal/ijair-volume-6-issue-1-xxxiv-january-march-2019.php')

if __name__ == '__main__':
   app.run(debug = True)