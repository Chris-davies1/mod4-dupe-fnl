from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

manga = Blueprint('manga', __name__)

@manga.route('/all_manga', methods=['GET', 'POST'])
def all_manga():
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        manga_name = request.form['manga_name']
        manga_genre = request.form['manga_genre']
        manga_price = request.form['manga_price']
        author = request.form['author']

        cursor.execute('INSERT INTO manga (Manga_Name, Manga_Genre, Manga_Price, Author) VALUES (%s, %s, %s, %s)',
                       (manga_name, manga_genre, manga_price, author))
        db.commit()

        flash('New manga added successfully!', 'success')
        return redirect(url_for('manga.all_manga'))

    cursor.execute('SELECT * FROM manga')
    all_manga = cursor.fetchall()
    return render_template('all_manga.html', all_manga=all_manga)

@manga.route('/update_manga/<int:manga_id>', methods=['GET', 'POST'])
def update_manga(manga_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        manga_name = request.form['manga_name']
        manga_genre = request.form['manga_genre']
        manga_price = request.form['manga_price']
        author = request.form['author']

        cursor.execute('UPDATE manga SET Manga_Name = %s, Manga_Genre = %s, Manga_Price = %s, Author = %s WHERE manga_id = %s',
                       (manga_name, manga_genre, manga_price, author, manga_id))
        db.commit()

        flash('Manga updated successfully!', 'success')
        return redirect(url_for('manga.all_manga'))

    cursor.execute('SELECT * FROM manga WHERE manga_id = %s', (manga_id,))
    manga_item = cursor.fetchone()
    return render_template('update_manga.html', manga=manga_item)

@manga.route('/delete_manga/<int:manga_id>', methods=['POST'])
def delete_manga(manga_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute('DELETE FROM manga WHERE manga_id = %s', (manga_id,))
    db.commit()

    flash('Manga deleted!', 'danger')
    return redirect(url_for('manga.all_manga'))