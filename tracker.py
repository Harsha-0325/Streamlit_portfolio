from flask import Flask, request, redirect
import requests
import json
import time

app = Flask(__name__)

# Cache to store IP lookups (avoid repeated API calls)
ip_cache = {}
CACHE_TIMEOUT = 3600  # 1 hour

def get_ip_info(ip):
    current_time = time.time()
    # Check if IP info is already cached
    if ip in ip_cache and (current_time - ip_cache[ip]['timestamp'] < CACHE_TIMEOUT):
        return ip_cache[ip]['data']
    
    # Fetch data from ipinfo.io
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        # Fallback to ip-api.com if ipinfo.io fails
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json() if response.status_code == 200 else {}
    
    # Store in cache
    ip_cache[ip] = {'data': data, 'timestamp': current_time}
    return data

@app.route('/')
def track_click():
    user_ip = request.remote_addr  # Get user IP
    ip_info = get_ip_info(user_ip)  # Get IP details
    
    location = ip_info.get('city', 'Unknown') + ", " + ip_info.get('country', 'Unknown')
    isp = ip_info.get('org', ip_info.get('isp', 'Unknown ISP'))
    
    print(f"IP: {user_ip}, Location: {location}, ISP: {isp}")
    
    # Redirect to portfolio after tracking
    return redirect("https://harshavardhan-reddy-portfolio.streamlit.app/")

if __name__ == '__main__':
    app.run(debug=True)
    

