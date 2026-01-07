from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Czech Republic Flashy History")


@app.get("/", response_class=HTMLResponse)
async def pink_history():
    """Serve a single-page, pink, and flashy history blurb."""
    page = """
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Flashy Czech History</title>
      <style>
        :root {
          --hot-pink: #ff2fb3;
          --electric-pink: #ff6dd0;
          --neon-pink: #ff4fcb;
          --dark-ink: #1c0f1d;
        }
        * { box-sizing: border-box; }
        body {
          margin: 0;
          min-height: 100vh;
          display: grid;
          place-items: center;
          background: radial-gradient(circle at 20% 20%, #ff9be5, #ff4fcb 30%, #1c0f1d 70%);
          color: white;
          font-family: "Helvetica Neue", Arial, sans-serif;
          text-align: center;
          overflow: hidden;
        }
        .glow {
          position: absolute;
          width: 40vmax;
          height: 40vmax;
          background: var(--hot-pink);
          filter: blur(120px);
          opacity: 0.4;
          border-radius: 50%;
          animation: float 16s ease-in-out infinite alternate;
        }
        .glow:nth-child(2) {
          animation-duration: 18s;
          animation-delay: 2s;
          background: var(--electric-pink);
          top: 10%;
          left: 60%;
        }
        .glow:nth-child(3) {
          animation-duration: 20s;
          animation-delay: 4s;
          background: var(--neon-pink);
          top: 60%;
          left: 10%;
        }
        @keyframes float {
          from { transform: translate(-10%, -10%) scale(1); }
          to   { transform: translate(10%, 10%) scale(1.15); }
        }
        .card {
          position: relative;
          max-width: 900px;
          padding: 32px 36px;
          border-radius: 18px;
          background: rgba(28, 15, 29, 0.75);
          border: 2px solid rgba(255, 79, 203, 0.45);
          box-shadow:
            0 0 25px rgba(255, 111, 208, 0.45),
            0 0 80px rgba(255, 47, 179, 0.3);
          backdrop-filter: blur(12px);
          z-index: 1;
        }
        h1 {
          margin: 0 0 16px;
          font-size: clamp(32px, 4vw, 48px);
          letter-spacing: 1px;
          text-shadow: 0 0 12px rgba(255, 111, 208, 0.8);
        }
        p {
          margin: 0;
          font-size: clamp(18px, 2.3vw, 22px);
          line-height: 1.5;
        }
        .sparkle {
          position: absolute;
          inset: 0;
          background: repeating-linear-gradient(
            125deg,
            rgba(255, 255, 255, 0.08),
            rgba(255, 255, 255, 0.08) 12px,
            transparent 12px,
            transparent 22px
          );
          mix-blend-mode: screen;
          opacity: 0.25;
          pointer-events: none;
          animation: shimmer 6s linear infinite;
        }
        @keyframes shimmer {
          from { transform: translateX(-20px); }
          to   { transform: translateX(20px); }
        }
      </style>
    </head>
    <body>
      <div class="glow"></div>
      <div class="glow"></div>
      <div class="glow"></div>
      <div class="card">
        <div class="sparkle"></div>
        <h1>Czech Republic — Flash History</h1>
        <p>
          From the early Slavic settlements that formed Great Moravia through the Přemyslid and Luxembourg dynasties that crowned Prague a Gothic jewel under Charles IV, the Czech lands endured Hussite fervor, Habsburg rule, and a 19th-century national revival before declaring Czechoslovak independence in 1918; they then suffered Nazi occupation, Soviet-backed communism, and finally the Velvet Revolution of 1989, leading to the peaceful 1993 split that created today’s Czech Republic—now a democratic EU member with deep Bohemian, Moravian, and Silesian roots.
        </p>
      </div>
    </body>
    </html>
    """
    return HTMLResponse(page)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
