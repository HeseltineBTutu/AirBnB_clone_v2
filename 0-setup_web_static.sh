#!/usr/bin/env bash
# This script sets up web servers for deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create fake HTML file
echo "<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <p>This is a test page.</p>
</body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ folder to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
config_block="location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html index.htm;
}"
# Check if the config block already exists
if ! grep -q "$config_block" "$config_file"; then
    sed -i "/^\s*server\s*{/a $config_block" "$config_file"
fi

# Restart Nginx
service nginx restart

exit 0
