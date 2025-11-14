import random
import json
import argparse
from datetime import datetime
import os

# Load quotes from JSON file
with open('quotes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Favorites file path
FAVORITES_FILE = 'favorites.json'

def load_favorites():
    """Load favorite quotes from file"""
    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_favorite(quote, author, category):
    """Save a quote to favorites"""
    favorites = load_favorites()
    
    # Check if already in favorites
    for fav in favorites:
        if fav['text'] == quote and fav['author'] == author:
            print("❌ This quote is already in your favorites!")
            return
    
    # Add new favorite
    new_favorite = {
        'text': quote,
        'author': author,
        'category': category,
        'saved_on': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    favorites.append(new_favorite)
    
    with open(FAVORITES_FILE, 'w', encoding='utf-8') as f:
        json.dump(favorites, f, indent=2, ensure_ascii=False)
    
    print("💾 Quote saved to favorites!")

def show_favorites():
    """Display all favorite quotes"""
    favorites = load_favorites()
    
    if not favorites:
        print("\n📭 You don't have any favorite quotes yet!")
        print("Use --save flag to save quotes you like.\n")
        return
    
    print("\n" + "=" * 60)
    print(f"💖 YOUR FAVORITE QUOTES ({len(favorites)} total)")
    print("=" * 60)
    
    for i, fav in enumerate(favorites, 1):
        print(f"\n{i}. \"{fav['text']}\"")
        print(f"   — {fav['author']} [{fav['category']}]")
        print(f"   Saved on: {fav['saved_on']}")
    
    print("=" * 60 + "\n")

# Set up command-line arguments
parser = argparse.ArgumentParser(description='Daily Quote Generator')
parser.add_argument('--category', '-c', 
                    choices=['motivation', 'life', 'wisdom', 'success', 'random'],
                    default='random',
                    help='Choose a quote category')
parser.add_argument('--list', '-l', 
                    action='store_true',
                    help='List all available categories')
parser.add_argument('--save', '-s',
                    action='store_true',
                    help='Save the current quote to favorites')
parser.add_argument('--favorites', '-f',
                    action='store_true',
                    help='Show all your favorite quotes')

args = parser.parse_args()

# If user wants to see favorites
if args.favorites:
    show_favorites()
    exit()

# If user wants to see categories
if args.list:
    print("\n📚 Available Categories:")
    print("=" * 50)
    for category in data['categories'].keys():
        count = len(data['categories'][category])
        print(f"  • {category.capitalize()} ({count} quotes)")
    print("  • Random (all categories)")
    print("=" * 50)
    print("\nUsage: python main.py --category motivation")
    print("   Or: python main.py -c wisdom")
    print("   Or: python main.py --save (to save current quote)")
    exit()

# Select quotes based on category
if args.category == 'random':
    # Get all quotes from all categories
    all_quotes = []
    for cat_name, quotes_list in data['categories'].items():
        for q in quotes_list:
            q['category'] = cat_name
        all_quotes.extend(quotes_list)
    quotes = all_quotes
    category_name = "Random"
else:
    quotes = data['categories'][args.category]
    for q in quotes:
        q['category'] = args.category
    category_name = args.category.capitalize()

# Select a random quote
quote_data = random.choice(quotes)
quote = quote_data['text']
author = quote_data['author']
category = quote_data.get('category', args.category)

# Display in terminal
print("=" * 50)
print(f"📖 DAILY QUOTE - {category_name}")
print("=" * 50)
print(f"\"{quote}\"")
print(f"\n- {author}")
print("=" * 50)

# Save to favorites if requested
if args.save:
    save_favorite(quote, author, category)

# Generate HTML file
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Quote - {category_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        
        .container {{
            background: white;
            border-radius: 20px;
            padding: 60px 40px;
            max-width: 800px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }}
        
        .icon {{
            font-size: 60px;
            margin-bottom: 30px;
        }}
        
        .category {{
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 14px;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        h1 {{
            color: #333;
            font-size: 28px;
            margin-bottom: 40px;
            font-weight: 300;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}
        
        .quote {{
            font-size: 32px;
            line-height: 1.6;
            color: #2c3e50;
            margin-bottom: 30px;
            font-style: italic;
            position: relative;
        }}
        
        .quote::before {{
            content: '"';
            font-size: 80px;
            color: #667eea;
            opacity: 0.3;
            position: absolute;
            left: -40px;
            top: -20px;
        }}
        
        .author {{
            font-size: 20px;
            color: #667eea;
            font-weight: 600;
            margin-bottom: 40px;
        }}
        
        .date {{
            color: #95a5a6;
            font-size: 14px;
            margin-top: 40px;
        }}
        
        .refresh-btn {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 20px;
            transition: transform 0.2s;
        }}
        
        .refresh-btn:hover {{
            transform: scale(1.05);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">📖</div>
        <div class="category">{category_name}</div>
        <h1>Daily Quote</h1>
        <div class="quote">{quote}</div>
        <div class="author">— {author}</div>
        <button class="refresh-btn" onclick="location.reload()">Get Another Quote</button>
        <div class="date">Generated on {datetime.now().strftime("%B %d, %Y at %I:%M %p")}</div>
    </div>
</body>
</html>"""

# Save HTML file
with open('daily_quote.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

print(f"\n✅ HTML file generated: daily_quote.html")
print("\n💡 Tip: Use --save flag to save this quote to favorites!")
print("       Use --favorites to see all your saved quotes!")