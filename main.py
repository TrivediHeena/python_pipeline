# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import psutil
from flask import Flask, request, render_template

flask = Flask(__name__)


@flask.route('/')
def watch():
    cpu_monitor = psutil.cpu_percent()
    memory_monitor = psutil.virtual_memory().percent
    message = None
    if cpu_monitor > 80 or memory_monitor > 80:
        message = "High CPU or Memmory Utilized"
    return f'CPU Utilization {cpu_monitor} and Memory Utilization {memory_monitor}'
    # return render_template('index.html', cpu_monitor=cpu_monitor,memory_monitor=memory_monitor,message=message)


def main():
    flask.run(debug=True, host='0.0.0.0')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
