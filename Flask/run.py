import sys
from navagetur import app

if __name__ == '__main__':
    port = 5000 if len(sys.argv) == 1 else sys.argv[1]
    local = True
    if local:
        app.run(host="127.0.0.1", port=port, debug=True)
    else:
        app.run(host="0.0.0.0", port=port, debug=True)
