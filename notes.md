## Notes

- set FLASK_APP env var and FLASK_DEBUG
- debug mode syncs on code change
- templates is a flask convention, auto detected
- decorator associates function with url
- save all files to reload changes

---

tutorial: modals, if request.method == post"

---

### Editing the Database with the Python Shell

```bash
    #Enter shell
    python
```
```python
    #Import database and app context
    from market import db, app
    app.app_context().push()
    
    #Delete database
    db.drop_all()

    # Create database
    db.create_all()

    # Create objects
    from market.models import Item, User
    item1 = Item(name="IPhone 10", price=500, barcode='1242353', desc="desc")
    u1 = User(username='user', password_hash='1234', email_address='asd@gmail.com')
    
    # Add item ansd save database
    db.session.add(item1)
    db.session.commit()

    #View items
    Item.query.all()

    # Search item
    for item in Item.query.filter_by()

    # Set attributes
    # first() gets user object
    item1.owner = User.query.filter_by(username='user').first().id

    # Rollback db
    from market.models import db
    db.session.rollback()
```

