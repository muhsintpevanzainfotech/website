import os

file_path = 'c:/Users/ADMIN/Downloads/FaunaFlora-1.0.0 (2)/FaunaFlora-1.0.0/public/blog.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'Harnessing the Power of SEO: Exploring the World of Search Engine Optimization': 'Harnessing the Power of SEO in India: Local Search Strategies for 2024',
    'Harnessing the\n                  Power of SEO: Exploring the World of Search Engine Optimization': 'Harnessing the\n                  Power of SEO in India: Local Search Strategies for 2024',
    "SEO is revolutionizing the way we find businesses. In this blog\n                  post, we'll delve into the incredible potential of search optimization, its online impact...": "SEO is revolutionizing how Indian businesses connect with customers. In this post, we explore the potential of local search in rapidly growing markets...",
    'Social Media:\n                    A Breath of Fresh Air for Digital Enthusiasts': 'Social Media Marketing in India:\n                    Engaging a Billion Digital Users',
    'Social Media:\n                    A Breath of Fresh Air for Digital Enthusiasts': 'Social Media Marketing in India:\n                    Engaging a Billion Digital Users',
    'Social Media: A Breath of Fresh Air for Digital Enthusiasts': 'Social Media Marketing in India: Engaging a Billion Digital Users',
    'From Visitors\n                    to Customers: The Promising World of Conversion Optimization': 'From Visitors\n                    to Customers: E-commerce Strategies for the Indian Market',
    'From Visitors to Customers: The Promising World of Conversion Optimization': 'From Visitors to Customers: E-commerce Strategies for the Indian Market',
    'Mobile Apps:\n                    Fueling the Digital Revolution': "Mobile Apps:\n                    Fueling India's Mobile-First Digital Revolution",
    'Mobile Apps: Fueling the Digital Revolution': "Mobile Apps: Fueling India's Mobile-First Digital Revolution",
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Blog contents successfully updated to India-based topics!")
