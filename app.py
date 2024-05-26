import os
from tabpy.tabpy_server.app import TabPy

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    tabpy = TabPy()
    tabpy.run(host='0.0.0.0', port=port)
