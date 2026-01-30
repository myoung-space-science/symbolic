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
        {'symbol': 'Α', 'hex': r'\x391'}, # Alpha
        {'symbol': 'Β', 'hex': r'\x392'}, # Beta
        {'symbol': 'Γ', 'hex': r'\x393'}, # Gamma
        {'symbol': 'Δ', 'hex': r'\x394'}, # Delta
        {'symbol': 'Ε', 'hex': r'\x395'}, # Epsilon
        {'symbol': 'Ζ', 'hex': r'\x396'}, # Zeta
        {'symbol': 'Η', 'hex': r'\x397'}, # Eta
        {'symbol': 'Θ', 'hex': r'\x398'}, # Theta
        {'symbol': 'Ι', 'hex': r'\x399'}, # Iota
        {'symbol': 'Κ', 'hex': r'\x39A'}, # Kappa
        {'symbol': 'Λ', 'hex': r'\x39B'}, # Lambda
        {'symbol': 'Μ', 'hex': r'\x39C'}, # Mu
        {'symbol': 'Ν', 'hex': r'\x39D'}, # Nu
        {'symbol': 'Ξ', 'hex': r'\x39E'}, # Xi
        {'symbol': 'Ο', 'hex': r'\x39F'}, # Omicron
        {'symbol': 'Π', 'hex': r'\x3A0'}, # Pi
        {'symbol': 'Ρ', 'hex': r'\x3A1'}, # Rho
        {'symbol': 'Σ', 'hex': r'\x3A3'}, # Sigma
        {'symbol': 'Τ', 'hex': r'\x3A4'}, # Tau
        {'symbol': 'Υ', 'hex': r'\x3A5'}, # Upsilon
        {'symbol': 'Φ', 'hex': r'\x3A6'}, # Phi
        {'symbol': 'Χ', 'hex': r'\x3A7'}, # Chi
        {'symbol': 'Ψ', 'hex': r'\x3A8'}, # Psi
        {'symbol': 'Ω', 'hex': r'\x3A9'}, # Omega
        {'symbol': 'Ϛ', 'hex': r'\x3DA'}, # Stigma
        {'symbol': 'α', 'hex': r'\x3B1'}, # alpha
        {'symbol': 'β', 'hex': r'\x3B2'}, # beta
        {'symbol': 'γ', 'hex': r'\x3B3'}, # gamma
        {'symbol': 'δ', 'hex': r'\x3B4'}, # delta
        {'symbol': 'ε', 'hex': r'\x3B5'}, # varepsilon
        {'symbol': 'ζ', 'hex': r'\x3B6'}, # zeta
        {'symbol': 'η', 'hex': r'\x3B7'}, # eta
        {'symbol': 'θ', 'hex': r'\x3B8'}, # theta
        {'symbol': 'ι', 'hex': r'\x3B9'}, # iota
        {'symbol': 'κ', 'hex': r'\x3BA'}, # kappa
        {'symbol': 'λ', 'hex': r'\x3BB'}, # lambda
        {'symbol': 'μ', 'hex': r'\x3BC'}, # mu
        {'symbol': 'ν', 'hex': r'\x3BD'}, # nu
        {'symbol': 'ξ', 'hex': r'\x3BE'}, # xi
        {'symbol': 'ο', 'hex': r'\x3BF'}, # omicron
        {'symbol': 'π', 'hex': r'\x3C0'}, # pi
        {'symbol': 'ρ', 'hex': r'\x3C1'}, # rho
        {'symbol': 'ς', 'hex': r'\x3C2'}, # final sigma
        {'symbol': 'σ', 'hex': r'\x3C3'}, # sigma
        {'symbol': 'τ', 'hex': r'\x3C4'}, # tau
        {'symbol': 'υ', 'hex': r'\x3C5'}, # upsilon
        {'symbol': 'φ', 'hex': r'\x3C6'}, # varphi
        {'symbol': 'χ', 'hex': r'\x3C7'}, # chi
        {'symbol': 'ψ', 'hex': r'\x3C8'}, # psi
        {'symbol': 'ω', 'hex': r'\x3C9'}, # omega
        {'symbol': 'ϑ', 'hex': r'\x3D1'}, # vartheta
        {'symbol': 'ϒ', 'hex': r'\x3D2'}, # (Upsilon variant?)
        {'symbol': 'ϕ', 'hex': r'\x3D5'}, # phi
        {'symbol': 'ϖ', 'hex': r'\x3D6'}, # varpi
        {'symbol': 'ϛ', 'hex': r'\x3DB'}, # stigma
        {'symbol': 'ϰ', 'hex': r'\x3F0'}, # varkappa
        {'symbol': 'ϱ', 'hex': r'\x3F1'}, # varrho
        {'symbol': 'ϵ', 'hex': r'\x3F5'}, # (epsilon variant?)
        {'symbol': 'ϴ', 'hex': r'\x3F4'}, # (theta variant?)
    ]
    return tuple(aslist)

