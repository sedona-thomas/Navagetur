from my_app import app
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        app.run(host="0.0.0.0", port=int(sys.argv[1]), debug=True)
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)
