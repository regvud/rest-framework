REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "core.pagination.PagePagination",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
