import logging
from chalice import Chalice
from chalicelib.analyze import analyze_book

app = Chalice(app_name="book-analyzer")

logging.getLogger().setLevel(logging.INFO)


# Runs when a new text file gets uploaded to the bucket
@app.on_s3_event(
    bucket="public-shx2jx",
    events=["s3:ObjectCreated:*"],
    suffix=".txt"
)
def analyze_new_book(event):
    bucket = event.bucket
    key = event.key

    logging.info(f"New book uploaded: {key}")

    # The analysis code handles downloading and saving of the book
    stats = analyze_book(bucket, key)

    logging.info(f"Finished {key}, total words: {stats['word_count']}")


