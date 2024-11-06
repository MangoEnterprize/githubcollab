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
    from portal import db, app
    app.app_context().push()
    
    #Delete database
    db.drop_all()

    # Create database
    db.create_all()

    # Create objects
    from portal.models import  User
    u1 = User(firstname='Lillian', lastname="Chen", password_hash='1234', email_address='lchen45@uncc.edu')
    
    # Add item ansd save database
    db.session.add(u1)
    db.session.commit()

    #View items
    Item.query.all()

    # Search item
    for item in Item.query.filter_by()

    # Set attributes
    # first() gets user object
    item1.owner = User.query.filter_by(username='user').first().id

    # Rollback db
    from portal.models import db
    db.session.rollback()
```

