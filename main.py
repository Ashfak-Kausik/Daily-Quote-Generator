import random 

quotes = [
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Get busy living or get busy dying. - Stephen King",
    "You only live once, but if you do it right, once is enough. -
    "In the end, we only regret the chances we didn't take. - Lewis Carroll",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
]

quote, author = random.choice(quotes).rsplit(" - ", 1)
print("Daily Quote")
print(f"\"{quote}\" - {author}")