# Shop (demo repository)

A tiny order-management service used by CodeWarden's demo. Conventions:

- All SQL goes through `app.db.run_query(sql, params)` (parameterised queries only).
- HTTP handlers must call `app.auth.require_login(request)` first.
- Uploaded file names go through `app.auth.sanitize_filename`.
- Secrets come from `app.config.get_secret(name)`, never from source code.
