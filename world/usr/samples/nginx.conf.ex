# Place this file in the `/etc/nginx/conf.d/` directory and update nginx
# configurations: sudo nginx -s reload

upstream <NGINX_UPSTREAM_NAME> {
    # http://nginx.org/ru/docs/http/ngx_http_upstream_module.html#upstream
    # For an UNIX socket:
    # server unix:<SOCKET> fail_timeout=0;

    # For a TCP/IP:
    server 127.0.0.1:<PORT> fail_timeout=0;
}

server {
    # Redirection of http://www.<HOST> on http://<HOST>
    # i.e. without `www` as 301 redirect.
    listen 80;
    server_name www.<HOST>;
    return 301 http://<HOST>$request_uri;
}

server {
    # DEFAULTS
    listen 80;
    keepalive_timeout 5;
    client_max_body_size 4G;
    server_name <HOST> *.<HOST>;

    root <BASE_DIR>/world/var/www;
    access_log <BASE_DIR>/world/var/log/nginx_access.log;
    # access_log <BASE_DIR>/world/var/log/$host;

    # OPTIMIZATION
    proxy_connect_timeout 16;
    proxy_send_timeout 16;
    proxy_read_timeout 16;
    send_timeout 16;

    # HANDLERS
    location ~ ^/(media|static)/  {
        # Buffering the static data for 7 minutes.
        expires 7m;
    }

    location / {
        # Checks for static file, if not found proxy to app.
        try_files $uri @django_app_proxy;
    }

    location @django_app_proxy {
        # DEFAULTS
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_buffering off;
        proxy_redirect off;

        # OPTIMIZATION
        # fastcgi_read_timeout 300;
        # limit_req zone=one burst=5;
        proxy_read_timeout 300;

        # HANDLERS
        proxy_pass http://<NGINX_UPSTREAM_NAME>;
    }
}