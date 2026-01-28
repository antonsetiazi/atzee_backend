def permission_required(app: str, resource: str, action: str):
    """
    Declare required permission for a view method.
    Checked later by permission middleware.
    """
    def decorator(view_func):
        setattr(view_func, "required_permission", {
            "app": app,
            "resource": resource,
            "action": action,
        })
        return view_func
    return decorator
