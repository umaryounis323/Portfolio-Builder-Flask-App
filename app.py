from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Umar Younis | DevOps Engineer</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
            min-height: 100vh;
            color: white;
        }

        header {
            text-align: center;
            padding: 60px 20px;
            background: rgba(255,255,255,0.05);
            border-bottom: 2px solid #e94560;
        }

        header h1 {
            font-size: 48px;
            color: #e94560;
            margin-bottom: 10px;
        }

        header p {
            font-size: 20px;
            color: #a8dadc;
        }

        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 0 20px;
        }

        .section {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            border-left: 4px solid #e94560;
        }

        .section h2 {
            font-size: 28px;
            color: #e94560;
            margin-bottom: 20px;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
        }

        .skill-card {
            background: linear-gradient(135deg, #e94560, #0f3460);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            font-size: 16px;
            font-weight: bold;
            transition: transform 0.3s;
        }

        .skill-card:hover {
            transform: scale(1.05);
        }

        .skill-card span {
            font-size: 30px;
            display: block;
            margin-bottom: 8px;
        }

        .project-card {
            background: rgba(255,255,255,0.08);
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
            border: 1px solid #e94560;
        }

        .project-card h3 {
            color: #a8dadc;
            margin-bottom: 8px;
            font-size: 20px;
        }

        .badge {
            display: inline-block;
            background: #e94560;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            margin: 4px;
        }

        footer {
            text-align: center;
            padding: 30px;
            color: #a8dadc;
            border-top: 1px solid rgba(255,255,255,0.1);
        }
    </style>
</head>
<body>

    <header>
        <h1>Umar Younis</h1>
        <p>🚀 Aspiring DevOps Engineer | Cloud & Automation Enthusiast</p>
    </header>

    <div class="container">

        <div class="section">
            <h2>👨‍💻 About Me</h2>
            <p style="font-size:16px; line-height:1.8; color:#a8dadc;">
                I am a passionate DevOps learner from Rawalpindi, Pakistan. 
                I am building my skills in Linux, Docker, Cloud, and automation 
                to become a professional DevOps Engineer.
            </p>
        </div>

        <div class="section">
            <h2>🛠️ Skills</h2>
            <div class="skills-grid">
                <div class="skill-card"><span>🐧</span>Linux</div>
                <div class="skill-card"><span>🐳</span>Docker</div>
                <div class="skill-card"><span>☁️</span>AWS EC2</div>
                <div class="skill-card"><span>🔧</span>Git & GitHub</div>
                <div class="skill-card"><span>🐍</span>Flask</div>
                <div class="skill-card"><span>🚂</span>Railway</div>
                <div class="skill-card"><span>🌐</span>Nginx</div>
                <div class="skill-card"><span>🔑</span>SSH</div>
                <div class="skill-card"><span>💻</span>WSL</div>
            </div>
        </div>

        <div class="section">
            <h2>🚀 Projects</h2>
            <div class="project-card">
                <h3>Flask App — Docker Deployment</h3>
                <p style="color:#ccc; margin-bottom:10px;">
                    Built a Python Flask web app, containerized it with Docker, 
                    pushed to GitHub, and deployed live on Railway.
                </p>
                <span class="badge">Docker</span>
                <span class="badge">Flask</span>
                <span class="badge">GitHub</span>
                <span class="badge">Railway</span>
            </div>
            <div class="project-card">
                <h3>Static Website — AWS EC2 + Nginx</h3>
                <p style="color:#ccc; margin-bottom:10px;">
                    Launched an EC2 instance, connected via SSH, installed Nginx, 
                    and deployed a live website on the internet.
                </p>
                <span class="badge">AWS EC2</span>
                <span class="badge">Nginx</span>
                <span class="badge">Linux</span>
                <span class="badge">SSH</span>
            </div>
        </div>

    </div>

    <footer>
        <p>Made with ❤️ by Umar Younis | Rawalpindi, Pakistan</p>
    </footer>

</body>
</html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
