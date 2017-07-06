# openshift-nginx-django-channels
nginx 1.12.0, Python 3.6.1, Django 1.11.2, channels 1.1.5


1. Run 'rhc create-app' to create your application
```BASH
rhc create-app <app name> http://cartreflect-claytondev.rhcloud.com/reflect?github=ccltw/openshift-cartridge-nginx
```

2. Run 'rhc cartridge-add' to add python cartridge to your application
```BASH
rhc cartridge-add http://cartreflect-claytondev.rhcloud.com/reflect?github=ccltw/openshift-cartridge-python --app <app name>
```

3. Run 'rhc cartridge-add' to add redis cartridge to your application (https://github.com/gerardogc2378/openshift-redis-cart)
```BASH
rhc cartridge-add http://cartreflect-claytondev.rhcloud.com/reflect?github=gerardogc2378/openshift-redis-cart --app <app name>
```

4. Add this upstream repo
```BASH
cd <app name>
git remote add upstream -m master git@github.com:ccltw/openshift-django-channels.git
git pull -s recursive -X theirs upstream master
```

5. Then push the repo upstream
```BASH
git push
```

6. SSH into the application and run this command to create a django superuser.
```BASH
python $OPENSHIFT_REPO_DIR/wsgi/myproject/manage.py createsuperuser
```


## WebSocket examples

```js
socket = new WebSocket("ws://" + window.location.host + ":8000/ws");
socket.onmessage = function(e) {
    alert(e.data);
}
socket.onopen = function() {
    console.log('WebSockets connection created.'); 
    socket.send("Hello world");
}
```
