class JournalError(Exception):
    """Base journal exception."""


class JournalNotBalancedError(JournalError):
    """Debit != Credit."""


class JournalAlreadyPostedError(JournalError):
    """Journal already posted."""


class JournalImmutableError(JournalError):
    """Attempt to modify immutable journal."""


class JournalAlreadyReversedError(JournalError):
    """Journal already reversed."""