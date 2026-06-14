from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        url = request.form["url"]

        # Tambahkan https:// jika user lupa
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        try:
            response = requests.get(url, timeout=5)

            x_frame_options = response.headers.get("X-Frame-Options")
            csp = response.headers.get("Content-Security-Policy")

            if x_frame_options:
                result = f"✅ Terlindungi (X-Frame-Options: {x_frame_options})"

            elif csp and "frame-ancestors" in csp:
                result = "✅ Terlindungi (Content-Security-Policy)"

            else:
                result = "⚠️ Rentan terhadap Clickjacking"

        except requests.exceptions.RequestException as e:
            result = f"❌ Error: {e}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15000, debug=True)