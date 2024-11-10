import webview

def create_window(title: str, url: str, debug: bool = True, width: int = 800, height: int = 600 ): 
    webview.create_window(title, url, width=width, height=height)
    webview.start(debug=debug)