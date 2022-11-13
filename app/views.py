from flask import request, render_template, flash, redirect, url_for, session
from app import app
from .forms import RegisterForm


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # get info on the app the was requested
            app_requested = request.form['button']
            print(app_requested)
            # redirect to the appropriate app
            return redirect(url_for(app_requested))
        except Exception as e:
            flash("Try again! An error occured")

    return render_template('index.html',
                           title='Simple template example')


@app.route('/form')
def form():
    user = {'name': 'Sam Wilson'}
    form = RegisterForm()
    # save results into session
    session['score'] = 100
    return render_template('form.html',
                           title='Form page',
                           form=form)


responses = {"good": "a good fit for this initiative. Your company clearly aligns with our mission to provide positive growth to LEDCs",
             "bad": " ",
             "ok": " ", }


@app.route('/about')
def about():
    user = {'name': 'Sam Wilson'}
    return render_template('about.html'
                           )


self_care = ['https://www.thespruce.com/how-to-create-a-daily-routine-2648007',
'https://www.nhs.uk/live-well/eat-well/how-to-eat-a-balanced-diet/eight-tips-for-healthy-eating/',
'https://www.counselling-directory.org.uk/memberarticles/knowing-your-limits-what-are-boundaries-and-why-are-they-important',
'https://www.newhealthadvisor.org/how-to-stop-using-your-phone-so-much.html']


pr = ['https://www.howtomakefriends.co.uk/',
'https://selfcarefundamentals.com/how-to-improve-relationships-with-your-parents/',
'https://professional.dce.harvard.edu/blog/eight-things-you-can-do-to-improve-your-communication-skills/',
'https://www.healthline.com/health/mental-health/how-to-control-anger'
]

emotion = ['https://www.healthline.com/health/how-to-control-your-emotions',
'https://www.nhs.uk/mental-health/self-help/tips-and-support/cope-with-depression/',
'https://www.healthline.com/health/how-to-stop-being-lazy',
'https://www.nhs.uk/mental-health/self-help/tips-and-support/how-to-be-happier/']


social=[
'https://myh.org.uk/how-to-reduce-social-media-usage/',
'https://erickimphotography.com/blog/2017/03/05/how-to-be-less-addicted-to-social-media/',
'https://www.headspace.com/mindfulness/negative-effects-of-social-media',
'https://www.healthline.com/health/mental-health/how-to-cope-with-anxiety'
]

areas = {
    'Social Media':social,
    'Self Care':self_care,
    'Personal Relationships':pr,
    'Emotions':emotion
}

@app.route('/results')
def results():
    score = session.get('score')
    suggestion = "N/A"
    return render_template('results.html',
                           score=score,
                           suggestion=suggestion)
