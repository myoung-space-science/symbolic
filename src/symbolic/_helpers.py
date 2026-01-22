import numbers
import typing


def standard(
    this,
    missing: str | None = None,
    joiner: str='*',
) -> str:
    """Convert `this` to a standard format.
    
    Parameters
    ----------
    this : string or iterable
        The object to convert.

    missing : string, optional
        The value to return if `this` is null.

    joiner : string, default='*'
        The string token to use when joining parts of an iterable argument.

    See Also
    --------
    `~symbolic.Expression`: A class that represents one or more terms joined by
    symbolic operators and grouped by separator characters. Instances support
    multiplication and division with strings or other instances, and
    exponentiation by real numbers. Instantiation automatically calls this
    function.
    """
    if isnull(this):
        return missing
    if isinstance(this, str):
        return this
    try:
        iter(this)
    except TypeError:
        return str(this)
    else:
        return joiner.join(f"({part})" for part in this)


def isnull(this: typing.Any) -> bool:
    """True if `this` is empty but not if it's 0.

    This function allows the calling code to programmatically test for objects
    that are logically `False` except for numbers equivalent to 0.
    """
    if isinstance(this, numbers.Number):
        return False
    size = getattr(this, 'size', None)
    if size is not None:
        return size == 0
    try:
        result = not bool(this)
    except ValueError:
        result = all((isnull(i) for i in this))
    return result


