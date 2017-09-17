import os

from tutorialsharing.api.app import app


port = os.environ.get('PORT')
if port:
    port = int(os.environ.get('PORT'))
else:
    port = 4000


app.run(host='0.0.0.0', port=port, debug=True)
