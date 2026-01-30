import pytest


def pytest_configure(config: pytest.Config):
    """Set pytest configuration values at runtime."""
    config.addinivalue_line(
        "markers", "term: tests of symbolic terms"
    )
    config.addinivalue_line(
        "markers", "expression: tests of symbolic expressions"
    )


@pytest.fixture
def greek():
    """Greek letters and associated dexadecimal codes.
    
    Notes
    -----
    The associated unicode value is `U+0HEX`, where HEX is the three-digit
    hexadecimal value (i.e., the three-digit number following `\\x` in the
    hexidecimal code).
    """
    aslist = [
        # upper-case standard
        {'symbol': 'Α', 'hex': r'\x391'},
        {'symbol': 'Β', 'hex': r'\x392'},
        {'symbol': 'Γ', 'hex': r'\x393'},
        {'symbol': 'Δ', 'hex': r'\x394'},
        {'symbol': 'Ε', 'hex': r'\x395'},
        {'symbol': 'Ζ', 'hex': r'\x396'},
        {'symbol': 'Η', 'hex': r'\x397'},
        {'symbol': 'Θ', 'hex': r'\x398'},
        {'symbol': 'Ι', 'hex': r'\x399'},
        {'symbol': 'Κ', 'hex': r'\x39A'},
        {'symbol': 'Λ', 'hex': r'\x39B'},
        {'symbol': 'Μ', 'hex': r'\x39C'},
        {'symbol': 'Ν', 'hex': r'\x39D'},
        {'symbol': 'Ξ', 'hex': r'\x39E'},
        {'symbol': 'Ο', 'hex': r'\x39F'},
        {'symbol': 'Π', 'hex': r'\x3A0'},
        {'symbol': 'Ρ', 'hex': r'\x3A1'},
        {'symbol': 'Σ', 'hex': r'\x3A3'},
        {'symbol': 'Τ', 'hex': r'\x3A4'},
        {'symbol': 'Υ', 'hex': r'\x3A5'},
        {'symbol': 'Φ', 'hex': r'\x3A6'},
        {'symbol': 'Χ', 'hex': r'\x3A7'},
        {'symbol': 'Ψ', 'hex': r'\x3A8'},
        {'symbol': 'Ω', 'hex': r'\x3A9'},
        # lower-case standard
        {'symbol': 'α', 'hex': r'\x3B1'},
        {'symbol': 'β', 'hex': r'\x3B2'},
        {'symbol': 'γ', 'hex': r'\x3B3'},
        {'symbol': 'δ', 'hex': r'\x3B4'},
        {'symbol': 'ε', 'hex': r'\x3B5'},
        {'symbol': 'ζ', 'hex': r'\x3B6'},
        {'symbol': 'η', 'hex': r'\x3B7'},
        {'symbol': 'θ', 'hex': r'\x3B8'},
        {'symbol': 'ι', 'hex': r'\x3B9'},
        {'symbol': 'κ', 'hex': r'\x3BA'},
        {'symbol': 'λ', 'hex': r'\x3BB'},
        {'symbol': 'μ', 'hex': r'\x3BC'},
        {'symbol': 'ν', 'hex': r'\x3BD'},
        {'symbol': 'ξ', 'hex': r'\x3BE'},
        {'symbol': 'ο', 'hex': r'\x3BF'},
        {'symbol': 'π', 'hex': r'\x3C0'},
        {'symbol': 'ρ', 'hex': r'\x3C1'},
        {'symbol': 'σ', 'hex': r'\x3C3'},
        {'symbol': 'τ', 'hex': r'\x3C4'},
        {'symbol': 'υ', 'hex': r'\x3C5'},
        {'symbol': 'φ', 'hex': r'\x3C6'},
        {'symbol': 'χ', 'hex': r'\x3C7'},
        {'symbol': 'ψ', 'hex': r'\x3C8'},
        {'symbol': 'ω', 'hex': r'\x3C9'},
    ]
    return tuple(aslist)
