from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-common-settings",
        """# Update all Redis cache connections to use SSL
for cache_name, cache_config in CACHES.items():
    if cache_config.get('BACKEND') == 'django_redis.cache.RedisCache':
        # Change redis:// to rediss://
        location = cache_config['LOCATION']
        if location.startswith('redis://'):
            cache_config['LOCATION'] = location.replace('redis://', 'rediss://', 1)
""",
    )
)