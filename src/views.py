@app.route('/')
def index():
    num_ratings = DBImage.select(fn.Sum(DBImage.num_ratings)).scalar()
    num_images = DBImage.select(fn.Count(DBImage.id)).scalar()
    return render_template('index.html', num_ratings=num_ratings, num_images=num_images)


@app.route('/image')
def image():
    """
    Responds with the path to a generated or retrieved image, optionally filtered as pretty.
    """
    mode = request.args.get('mode', 'filtered')
    if mode == 'hybrid':
        pass
    elif mode == 'standard':
        num_images = DBImage.select(fn.Count(DBImage.id)).scalar()
        if num_images < MAX_IMAGES:
            filename = generate_image()
            DBImage.create(filename=filename)
        else:
            to_rate = (DBImage.select()
                              .order_by(DBImage.num_ratings, fn.Random())
                              .limit(1))[0]
            filename = to_rate.filename
    elif mode == 'filtered':
        filename = generate_pretty_image()
        DBImage.create(filename=filename)

    return ('/image/' + filename, 200, {})


@app.route('/image/<string:image_filename>')
def download_image(image_filename):
    return send_from_directory(os.path.abspath('images'), image_filename)


@app.route('/image/<string:image_filename>', methods=['POST'])
def image_label(image_filename):
    rating = int(request.form['label'])
    image = DBImage.get(filename=image_filename)
    image.score = ((image.score * image.num_ratings) + rating) / (image.num_ratings + 1)
    image.num_ratings += 1
    image.save()
    return "", 200, {}


@app.route('/pretty')
def pretty_gallery():
    best = DBImage.select(DBImage.filename).order_by(DBImage.score.desc()).limit(300)
    best = map(lambda i: i.filename, best)
    return render_template('gallery.html', images=best)


@app.route('/ugly')
def ugly_gallery():
    worst = DBImage.select(DBImage.filename).order_by(DBImage.score.asc()).limit(300)
    worst = map(lambda i: i.filename, worst)
    return render_template('gallery.html', images=worst)


@app.route('/smart_pretty')
def smart_pretty_gallery():
    """
    Generates a gallery of images that are classified as pretty.
    """
    images = [generate_pretty_image() for i in xrange(60)]
    return render_template('gallery.html', images=images)


@app.route('/sidebyside')
def side_by_side_gallery():
    pretty = DBImage.select().order_by(DBImage.score.desc()).limit(100)
    ugly = DBImage.select().order_by(DBImage.score.asc()).limit(100)
    smart_pretty =
