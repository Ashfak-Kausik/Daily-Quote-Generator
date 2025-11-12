import random
import json
import argparse
from datetime import datetime

# Load quotes from JSON file
with open('quotes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Set up command-line arguments
parser = argparse.ArgumentParser(description='Daily Quote Generator')
parser.add_argument('--category', '-c', 
                    choices=['motivation', 'life', 'wisdom', 'success', 'random'],
                    default='random',
                    help='Choose a quote category')
parser.add_argument('--list', '-l', 
                    action='store_true',
                    help='List all available categories')

args = parser.parse_args()

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
    exit()

# Select quotes based on category
if args.category == 'random':
    # Get all quotes from all categories
    all_quotes = []
    for quotes_list in data['categories'].values():
        all_quotes.extend(quotes_list)
    quotes = all_quotes
    category_name = "Random"
else:
    quotes = data['categories'][args.category]
    category_name = args.category.capitalize()

# Select a random quote
quote_data = random.choice(quotes)
quote = quote_data['text']
author = quote_data['author']

# Display in terminal
print("=" * 50)
print(f"📖 DAILY QUOTE - {category_name}")
print("=" * 50)
print(f"\"{quote}\"")
print(f"\n- {author}")
print("=" * 50)

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
print("Open it in your browser to see your quote!")