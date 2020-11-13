import webbrowser
def select_class():
    class_name = str(input('class: '))
    
    classes = {'class name': 'https://us02web.zoom.us/j/id?pwd=password'}
    
    if class_name not in list(classes.keys()):
        print('valid class names:')
        print(list(classes.keys()))
        select_class()
    url = classes.get(class_name)
    return url

def join_class():
    url = select_class()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

join_class()
