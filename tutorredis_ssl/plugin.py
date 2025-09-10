# from tutor import hooks

# # Simplified Redis SSL Plugin for Tutor Open edX
# __version__ = "1.0.0"

# # ============================================================================
# # 1. TUTOR CONFIGURATION DEFAULTS
# # ============================================================================

# hooks.Filters.CONFIG_DEFAULTS.add_items([
#     # Disable internal Redis by default when using external Redis
#     ("RUN_REDIS", False),
    
#     # Redis connection configuration
#     ("REDIS_HOST", ""),
#     ("REDIS_PORT", 6380),
#     ("REDIS_USERNAME", ""),
#     ("REDIS_PASSWORD", ""),
#     ("REDIS_DATABASE", 0),
#     ("REDIS_SSL", True),
# ])

# # ============================================================================
# # 2. DOCKER COMPOSE ENVIRONMENT VARIABLE PATCHES
# # ============================================================================

# hooks.Filters.ENV_PATCHES.add_items([
    
#     # LMS Worker Environment
#     (
#         "local-docker-compose-lms-worker-environment",
#         """
# {% if REDIS_HOST %}
# {% if REDIS_SSL %}
# {% if REDIS_USERNAME and REDIS_PASSWORD %}
# CELERY_BROKER_URL: "rediss://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "rediss://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "rediss://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% elif REDIS_PASSWORD %}
# CELERY_BROKER_URL: "rediss://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "rediss://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "rediss://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% else %}
# CELERY_BROKER_URL: "rediss://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "rediss://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "rediss://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% endif %}
# {% else %}
# {% if REDIS_USERNAME and REDIS_PASSWORD %}
# CELERY_BROKER_URL: "redis://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "redis://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "redis://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% elif REDIS_PASSWORD %}
# CELERY_BROKER_URL: "redis://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "redis://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "redis://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% else %}
# CELERY_BROKER_URL: "redis://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "redis://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "redis://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% endif %}
# {% endif %}
# {% endif %}
# """
#     ),
    
#     # CMS Worker Environment (same logic)
#     (
#         "local-docker-compose-cms-worker-environment",
#         """
# {% if REDIS_HOST %}
# {% if REDIS_SSL %}
# {% if REDIS_USERNAME and REDIS_PASSWORD %}
# CELERY_BROKER_URL: "rediss://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "rediss://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "rediss://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% elif REDIS_PASSWORD %}
# CELERY_BROKER_URL: "rediss://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "rediss://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "rediss://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% else %}
# CELERY_BROKER_URL: "rediss://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "rediss://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "rediss://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% endif %}
# {% else %}
# {% if REDIS_USERNAME and REDIS_PASSWORD %}
# CELERY_BROKER_URL: "redis://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "redis://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "redis://{{ REDIS_USERNAME }}:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% elif REDIS_PASSWORD %}
# CELERY_BROKER_URL: "redis://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "redis://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "redis://:{{ REDIS_PASSWORD }}@{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% else %}
# CELERY_BROKER_URL: "redis://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# CELERY_RESULT_BACKEND: "redis://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# REDIS_URL: "redis://{{ REDIS_HOST }}:{{ REDIS_PORT }}/{{ REDIS_DATABASE }}"
# {% endif %}
# {% endif %}
# {% endif %}
# """
#     ),
# ])

# # ============================================================================
# # 3. DJANGO SETTINGS PATCHES
# # ============================================================================

# hooks.Filters.ENV_PATCHES.add_items([
#     (
#         "openedx-common-settings",
#         '''
# # Redis SSL Plugin - Simplified Tutor Config Driven
# import logging
# import ssl  
# import os

# log = logging.getLogger(__name__)

# # Read Redis configuration from Tutor config
# REDIS_HOST = "{{ REDIS_HOST }}"
# REDIS_PORT = {{ REDIS_PORT }}
# REDIS_USERNAME = "{{ REDIS_USERNAME }}"
# REDIS_PASSWORD = "{{ REDIS_PASSWORD }}"
# REDIS_DATABASE = {{ REDIS_DATABASE }}
# REDIS_SSL = {{ REDIS_SSL }}

# if REDIS_HOST:
#     log.info("Redis SSL Plugin: Loading external Redis configuration...")
    
#     # Build the connection string
#     if REDIS_SSL:
#         protocol = "rediss"
#     else:
#         protocol = "redis"

#     if REDIS_USERNAME and REDIS_PASSWORD:
#         auth_part = f"{REDIS_USERNAME}:{REDIS_PASSWORD}@"
#     elif REDIS_PASSWORD:
#         auth_part = f":{REDIS_PASSWORD}@"
#     else:
#         auth_part = ""

#     REDIS_CONNECTION_STRING = f"{protocol}://{auth_part}{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}"

#     # Force environment variables (affects Celery workers directly)
#     os.environ["CELERY_BROKER_URL"] = REDIS_CONNECTION_STRING
#     os.environ["CELERY_RESULT_BACKEND"] = REDIS_CONNECTION_STRING
#     os.environ["REDIS_URL"] = REDIS_CONNECTION_STRING

#     # SSL connection pool options (only for SSL connections)
#     if REDIS_SSL:
#         SSL_POOL_OPTIONS = {
#             "ssl_cert_reqs": None,
#             "ssl_check_hostname": False,
#         }
#     else:
#         SSL_POOL_OPTIONS = {}

#     # Override ALL cache configurations
#     CACHES = {
#         "default": {
#             "BACKEND": "django_redis.cache.RedisCache",
#             "LOCATION": REDIS_CONNECTION_STRING,
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 "CONNECTION_POOL_KWARGS": SSL_POOL_OPTIONS,
#             }
#         },
#         "general": {
#             "KEY_PREFIX": "general",
#             "BACKEND": "django_redis.cache.RedisCache",
#             "LOCATION": REDIS_CONNECTION_STRING,
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 "CONNECTION_POOL_KWARGS": SSL_POOL_OPTIONS,
#             }
#         },
#         "mongo_metadata_inheritance": {
#             "KEY_PREFIX": "mongo_metadata_inheritance",
#             "TIMEOUT": 300,
#             "BACKEND": "django_redis.cache.RedisCache",
#             "LOCATION": REDIS_CONNECTION_STRING,
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 "CONNECTION_POOL_KWARGS": SSL_POOL_OPTIONS,
#             }
#         },
#         "configuration": {
#             "KEY_PREFIX": "configuration",
#             "BACKEND": "django_redis.cache.RedisCache",
#             "LOCATION": REDIS_CONNECTION_STRING,
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 "CONNECTION_POOL_KWARGS": SSL_POOL_OPTIONS,
#             }
#         },
#         "celery": {
#             "KEY_PREFIX": "celery",
#             "TIMEOUT": 7200,
#             "BACKEND": "django_redis.cache.RedisCache", 
#             "LOCATION": REDIS_CONNECTION_STRING,
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 "CONNECTION_POOL_KWARGS": SSL_POOL_OPTIONS,
#             }
#         },
#         "course_structure_cache": {
#             "KEY_PREFIX": "course_structure",
#             "TIMEOUT": 604800,  # 1 week
#             "BACKEND": "django_redis.cache.RedisCache",
#             "LOCATION": REDIS_CONNECTION_STRING,
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 "CONNECTION_POOL_KWARGS": SSL_POOL_OPTIONS,
#             }
#         },
#         "ora2-storage": {
#             "KEY_PREFIX": "ora2-storage",
#             "BACKEND": "django_redis.cache.RedisCache",
#             "LOCATION": REDIS_CONNECTION_STRING,
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#                 "CONNECTION_POOL_KWARGS": SSL_POOL_OPTIONS,
#             }
#         }
#     }

#     # Celery configuration
#     CELERY_BROKER_URL = REDIS_CONNECTION_STRING
#     CELERY_RESULT_BACKEND = REDIS_CONNECTION_STRING

#     # Celery SSL settings (only for SSL connections)
#     if REDIS_SSL:
#         CELERY_BROKER_USE_SSL = {
#             "ssl_cert_reqs": ssl.CERT_NONE,
#             "ssl_check_hostname": False,
#         }
#         CELERY_REDIS_BACKEND_USE_SSL = {
#             "ssl_cert_reqs": ssl.CERT_NONE,
#             "ssl_check_hostname": False,
#         }

#     log.info("Redis SSL Plugin: External Redis configuration complete!")
#     log.info(f"Redis Host: {REDIS_HOST}:{REDIS_PORT}")
#     log.info(f"SSL Enabled: {REDIS_SSL}")
    
# else:
#     log.info("Redis SSL Plugin: No external Redis configured. Using internal Redis.")
#     log.info("To configure external Redis, run:")
#     log.info("   tutor config save --set REDIS_HOST=your-redis-host.com")
#     log.info("   tutor config save --set REDIS_PASSWORD=your-password")
#     log.info("   tutor config save --set REDIS_SSL=true")
# '''
#     ),
# ])

# __doc__ = """
# Simplified Redis SSL Plugin for Tutor Open edX

# This plugin configures Open edX to connect to an external Redis server using
# Tutor's configuration system with template logic for connection string building.

# Usage:
# 1. tutor plugins enable redis-ssl-simple
# 2. tutor config save --set REDIS_HOST=your-redis-host.com
# 3. tutor config save --set REDIS_PASSWORD=your-password
# 4. tutor config save && tutor local reboot
# """
