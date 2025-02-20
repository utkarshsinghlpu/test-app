from flask import Flask
import os, datetime, subprocess, pwd

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Utkarsh Singh"
    username = pwd.getpwuid(os.getuid())[0]  # Alternative to os.getlogin()
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <h1>System Monitoring</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time:</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
