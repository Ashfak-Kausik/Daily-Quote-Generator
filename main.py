import random 

quotes = [
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Get busy living or get busy dying. - Stephen King",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "Many of life's failures are people who did not realize how close they were to success when they gave up. - Thomas A. Edison"
    "In the end, we only regret the chances we didn't take. - Lewis Carroll",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "Do not take life too seriously. You will never get out of it alive. - Elbert Hubbard"
    "Life itself is the most wonderful fairy tale. - Hans Christian Andersen"
    "To live is the rarest thing in the world. Most people exist, that is all. - Oscar Wilde"
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost"
    "Life is really simple, but we insist on making it complicated. - Confucius"
    "The biggest adventure you can take is to live the life of your dreams. - Oprah Winfrey"
    "Life is made of ever so many partings welded together. - Charles Dickens"
]

quote, author = random.choice(quotes).rsplit(" - ", 1)
print("Daily Quote")
print(f"\"{quote}\" - {author}")