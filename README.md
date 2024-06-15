## Setup

1. Install packages with `poetry` or `uv` or `pip`
2. Run server with `gunicorn` (`gunicorn mre.wsgi`) or `granian` (`granian --interface wsgi --host 0.0.0.0 --port 8000 mre.wsgi:application`)
3. Attach to process via PID with `memray` (`memray attach <PID>`)
3. Send `curl` request to API -  `curl -v -F file=@"/Users/<user>/large-video.mp4" http://localhost:8000/files/`
3.1 Please, take a large video to see an impact on memory instantly (like 100+ MB, I used ~750 MB)
