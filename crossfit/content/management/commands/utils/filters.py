def starts_with(text):
    def f(c):
        return c.data.startswith(text)
    return f
