from matplotlib.figure import Figure
import numpy as np
from datetime import datetime
from flask import Flask, render_template, request, redirect, send_file

from io import BytesIO
import config


# CREATE APP
app = Flask(__name__)
app.config.from_object('config.ProductionConfig')


def set_figure(hz):
    """ Return plot with sine wave with frequency of hz.

    Parameters:
        hz (int): Frequency of sine wave.
    """
    time = np.linspace(0, 5, 1000)  # define sine wave
    amp = np.sin(time * hz)

    fig = Figure()  # set up figure for plot
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(time, amp)  # add sine wave to figure
    ax.set_title('Sinuskurve')  # formatting
    ax.set_xlabel('Tid (s)')
    ax.set_ylabel('Amplitude')
    ax.grid(True, which='both')
    ax.text(-1, -1.4, datetime.now())  # add time stamp
    return fig


@app.route('/')  # "Home page" gets redirected to /graf
def go_to_graf():
    """"Redirect to endpoint with graph."""
    return redirect('/graf')


@app.route('/graf')  # 1st endpoint
@app.route('/graf', methods=['GET'])  # endpoint for other frequencies
def graf():
    """Return graph with title."""
    frek = 1 if request.args.get('frekvens') is None \
        else request.args.get('frekvens')  # get frequency

    width = app.config['PLOT_WIDTH']  # size of plot
    height = app.config['PLOT_HEIGHT']

    return render_template('graf.html',
                           title='Sinuskurve ' + str(frek)+ 'Hz',
                           frek=frek, width=width, height=height)


@app.route('/plot.png')  # image/png endpoint
def figure():
    """Return plot(format=png)"""

    hz = 1 if request.args.get('frekvens') is None \
        else int(request.args.get('frekvens'))  # get frequency

    canvas = set_figure(hz)  # get plot
    out = BytesIO()  # buffer
    canvas.savefig(out)
    out.seek(0)
    return send_file(out, mimetype='image/png', cache_timeout=60)


if __name__ == '__main__':
    app.run()
