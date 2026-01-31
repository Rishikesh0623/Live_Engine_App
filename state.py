"""
state.py
Shared application state for the Live Engine App.

Acts as a single source of truth for:
- Engine running status
- AC status
- Lock status
- Radio status
- Runtime tracking

All modules read from and write to this state.
"""

ENGINE_ON = False
AC_ON = False
LOCKED = True
RADIO_ON = False