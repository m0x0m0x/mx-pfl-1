# Setting up Redish Upstash as Rate Limiter1. [Setting up Redish Upstash as Rate Limiter](#setting-up-redish-upstash-as-rate-limiter)

1. [Setting up Redish Upstash as Rate Limiter1. Setting up Redish Upstash as Rate Limiter](#setting-up-redish-upstash-as-rate-limiter1-setting-up-redish-upstash-as-rate-limiter)
   1. [Step-by-Step Guide to Deploy Rate Limiting with Upstash Redis on Vercel](#step-by-step-guide-to-deploy-rate-limiting-with-upstash-redis-on-vercel)
      1. [**Step 1: Create Upstash Redis Database**](#step-1-create-upstash-redis-database)
      2. [**Step 2: Add Environment Variables to Vercel**](#step-2-add-environment-variables-to-vercel)
         1. [**Option A: Via Vercel Dashboard (Easier)**](#option-a-via-vercel-dashboard-easier)
         2. [**Option B: Via Vercel CLI (Faster for developers)**](#option-b-via-vercel-cli-faster-for-developers)
      3. [**Step 3: Update Your Flask App Code**](#step-3-update-your-flask-app-code)
      4. [**Step 4: Create Requirements File**](#step-4-create-requirements-file)
      5. [**Step 5: Create Vercel Configuration**](#step-5-create-vercel-configuration)
      6. [**Step 6: Test Locally (Optional but Recommended)**](#step-6-test-locally-optional-but-recommended)
      7. [**Step 7: Deploy to Vercel**](#step-7-deploy-to-vercel)
      8. [**Step 8: Verify Deployment**](#step-8-verify-deployment)
      9. [**Step 9: Monitor and Debug**](#step-9-monitor-and-debug)
      10. [**Step 10: Production Optimization**](#step-10-production-optimization)
      11. [**Quick Checklist Before Deploying:**](#quick-checklist-before-deploying)

## Step-by-Step Guide to Deploy Rate Limiting with Upstash Redis on Vercel

### **Step 1: Create Upstash Redis Database**

1. Go to [upstash.com](https://upstash.com) (free tier available)
2. Click "Create Database"
3. Choose region closest to your Vercel deployment
4. Name it (e.g., "flask-rate-limiter")
5. Click "Create"
6. After creation, you'll see your credentials:
   - `UPSTASH_REDIS_REST_URL` (looks like: `https://xxx.upstash.io`)
   - `UPSTASH_REDIS_REST_TOKEN` (long string)

### **Step 2: Add Environment Variables to Vercel**

#### **Option A: Via Vercel Dashboard (Easier)**

1. Go to your project on [vercel.com](https://vercel.com)
2. Click on your project
3. Go to **Settings** → **Environment Variables**
4. Add each variable:

   **First variable:**
   - Name: `UPSTASH_REDIS_REST_URL`
   - Value: (paste from Upstash)
   - Environments: Production, Preview, Development (check all)
   - Click "Add"

   **Second variable:**
   - Name: `UPSTASH_REDIS_REST_TOKEN`
   - Value: (paste from Upstash)
   - Environments: Production, Preview, Development (check all)
   - Click "Add"

5. Click "Save"

#### **Option B: Via Vercel CLI (Faster for developers)**

```bash
# Install Vercel CLI if you haven't
npm i -g vercel

# Login
vercel login

# Add environment variables
vercel env add UPSTASH_REDIS_REST_URL production
# (paste the URL when prompted)

vercel env add UPSTASH_REDIS_REST_TOKEN production
# (paste the token when prompted)

# Repeat for preview and development if needed
vercel env add UPSTASH_REDIS_REST_URL preview
vercel env add UPSTASH_REDIS_REST_TOKEN preview
```

### **Step 3: Update Your Flask App Code**

Create or update `app.py`:

```python
from flask import Flask, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import urllib.parse

app = Flask(__name__)

def custom_429_response(request_limit):
    """Custom HTML response when rate limit is exceeded"""
    html = f'''
    <html>
    <body style="background:black; color:red; text-align:center; padding-top:10%">
        <h1 style="text-shadow:0 0 20px red">RATE LIMIT REACHED!</h1>
        <p>Limit: {request_limit.limit}</p>
        <p>Please try again later.</p>
        <img src="https://i.ibb.co/hxYyJHVv/image.png" width="900">
    </body>
    </html>
    '''
    return make_response(html, 429)

# Redis Configuration
redis_url = os.getenv("UPSTASH_REDIS_REST_URL")
redis_token = os.getenv("UPSTASH_REDIS_REST_TOKEN")

if redis_url and redis_token:
    # Production: Use Upstash Redis
    parsed = urllib.parse.urlparse(redis_url)
    host = parsed.netloc
    storage_uri = f"rediss://default:{redis_token}@{host}:443"
    print(f"✅ Using Upstash Redis: {host}")
else:
    # Development: Use memory
    storage_uri = "memory://"
    print("⚠️ Using memory storage (set env vars for Redis)")

# Initialize limiter
limiter = Limiter(
    key_func=get_remote_address,
    app=app,  # Attach to Flask app
    default_limits=["100 per day", "10 per hour", "5 per minute"],
    on_breach=custom_429_response,
    storage_uri=storage_uri,
    strategy="fixed-window",
    swallow_errors=True,
    headers_enabled=True,
)

# Example route with rate limiting
@app.route("/")
@limiter.limit("5 per minute")  # Override default for this route
def home():
    return {"message": "Hello World!", "status": "success"}

@app.route("/api/data")
@limiter.limit("3 per minute")
def get_data():
    return {"data": "This is rate limited to 3 requests per minute"}

# For Vercel serverless
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

# Vercel needs this
def handler(request):
    return app(request)
```

### **Step 4: Create Requirements File**

Create `requirements.txt`:

```txt
Flask==2.3.3
flask-limiter==3.5.0
redis==5.0.1
urllib3==2.0.7
```

### **Step 5: Create Vercel Configuration**

Create `vercel.json` in your project root:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "UPSTASH_REDIS_REST_URL": "@upstash_redis_rest_url",
    "UPSTASH_REDIS_REST_TOKEN": "@upstash_redis_rest_token"
  }
}
```

### **Step 6: Test Locally (Optional but Recommended)**

Install dependencies and test before deploying:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Create .env file for local testing
echo "UPSTASH_REDIS_REST_URL=your_url_here" > .env
echo "UPSTASH_REDIS_REST_TOKEN=your_token_here" >> .env

# Install python-dotenv for local testing
pip install python-dotenv

# Add to top of app.py for local testing:
from dotenv import load_dotenv
load_dotenv()  # Remove this line when deploying to Vercel

# Run locally
python app.py
```

### **Step 7: Deploy to Vercel**

```bash
# Deploy from your project directory
vercel

# For production deployment
vercel --prod

# Or connect your GitHub repo to Vercel for automatic deploys
```

### **Step 8: Verify Deployment**

1. After deployment, check Vercel deployment logs:
   - Go to your project on vercel.com
   - Click on the latest deployment
   - Check "Functions" logs
   - You should see "✅ Using Upstash Redis: xxx.upstash.io"

2. Test rate limiting:

```bash
# Make multiple fast requests
for i in {1..6}; do
  curl https://your-app.vercel.app/
  echo "Request $i"
done
```

After 5 requests in a minute, you should see the 429 HTML error page.

### **Step 9: Monitor and Debug**

**Check if Redis is working:**

```python
# Add this debug route temporarily
@app.route("/debug/redis")
def debug_redis():
    redis_url = os.getenv("UPSTASH_REDIS_REST_URL")
    redis_token = os.getenv("UPSTASH_REDIS_REST_TOKEN")

    return {
        "redis_url_exists": bool(redis_url),
        "redis_token_exists": bool(redis_token),
        "storage_type": "redis" if (redis_url and redis_token) else "memory",
        "redis_url_prefix": redis_url[:20] + "..." if redis_url else None
    }
```

**Common Issues & Solutions:**

1. **Redis connection fails**:
   - Check if `UPSTASH_REDIS_REST_URL` has `https://` prefix
   - Verify token is correct
   - Check Upstash dashboard for connection limits

2. **Rate limits reset on every request**:
   - Make sure storage_uri is using `rediss://` not `redis://`
   - Check Vercel logs for connection errors

3. **Environment variables not loading**:
   - Re-deploy after adding env vars (Vercel needs redeploy)
   - Check Vercel dashboard → Settings → Environment Variables

### **Step 10: Production Optimization**

For better performance, add these to your `app.py`:

```python
# Cache control for Vercel edge
@app.after_request
def add_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache'
    return response

# Health check endpoint
@app.route("/health")
def health():
    return {"status": "healthy", "rate_limiting": "active"}
```

### **Quick Checklist Before Deploying:**

- [ ] Upstash database created
- [ ] Environment variables added in Vercel
- [ ] `requirements.txt` includes all dependencies
- [ ] `vercel.json` created
- [ ] Rate limits configured appropriately for your use case
- [ ] Custom 429 response looks good
- [ ] Tested locally with `.env` file

That's it! Your rate limiting should now work on Vercel with Upstash Redis. The free tier of Upstash gives you 10,000 commands per day which is plenty for most applications.
