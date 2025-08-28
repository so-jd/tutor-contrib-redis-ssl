from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-common-settings",
        """
# Update all Redis cache connections to use SSL
for cache_name, cache_config in CACHES.items():
    if cache_config.get('BACKEND') == 'django_redis.cache.RedisCache':
        # Change redis:// to rediss://
        location = cache_config['LOCATION']
        if location.startswith('redis://'):
            cache_config['LOCATION'] = location.replace('redis://', 'rediss://', 1)
        
        # Add SSL options
        if 'OPTIONS' not in cache_config:
            cache_config['OPTIONS'] = {}
        if 'CONNECTION_POOL_KWARGS' not in cache_config['OPTIONS']:
            cache_config['OPTIONS']['CONNECTION_POOL_KWARGS'] = {}
        
        cache_config['OPTIONS']['CONNECTION_POOL_KWARGS'].update({
            'ssl_cert_reqs': 'required',
            # Add other SSL options as needed
        })
""",
    )
)