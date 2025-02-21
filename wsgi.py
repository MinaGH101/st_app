import os
import subprocess

def application(environ, start_response):
    # Start Streamlit if it's not running
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    # Run Streamlit as a subprocess
    streamlit_cmd = "streamlit run app.py"
    subprocess.Popen(streamlit_cmd, shell=True)

    return [b"Streamlit is launching... Visit your server on port 8501."]
