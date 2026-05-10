from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'  # Required for flash messages

# Sample blog posts data (in a real app, use a database)
blog_posts = [
    {
        'id': 1,
        'title': 'Getting Started with Flask',
        'content': 'Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. In this post, we will explore the basics of Flask and build a simple web application.',
        'author': 'John Doe',
        'date': '2024-01-15',
        'likes': 42
    },
    {
        'id': 2,
        'title': 'Modern Web Design Trends 2024',
        'content': "Discover the latest trends in web design including glassmorphism, neumorphism, and kinetic typography. Learn how to implement these modern design patterns to create stunning user interfaces that stand out in 2024.",
        'author': 'Jane Smith',
        'date': '2024-01-20',
        'likes': 87
    },
    {
        'id': 3,
        'title': 'Python Tips for Beginners',
        'content': 'Learn essential Python programming tips that will make your code more efficient and readable. From list comprehensions to context managers, these tips will help you write better Python code from day one.',
        'author': 'Alex Johnson',
        'date': '2024-01-25',
        'likes': 63
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In a real app, you would send an email or save to database
        flash(f'Thank you {name}! Your message has been sent.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    flash('Post not found!', 'error')
    return redirect(url_for('index'))

@app.route('/like/<int:post_id>')
def like_post(post_id):
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if post:
        post['likes'] += 1
        flash('You liked this post!', 'success')
    return redirect(url_for('index'))

@app.route('/create-post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')
        
        if title and content and author:
            new_post = {
                'id': len(blog_posts) + 1,
                'title': title,
                'content': content,
                'author': author,
                'date': datetime.now().strftime('%Y-%m-%d'),
                'likes': 0
            }
            blog_posts.append(new_post)
            flash('Your post has been created successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Please fill in all fields!', 'error')
    
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
