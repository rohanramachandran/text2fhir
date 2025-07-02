from packaging.version import Version

class LooseVersion:
    """A very small subset of distutils' LooseVersion for marshmallow>=3.2"""
    def __init__(self, v: str):
        self._v = Version(v)
        # replicate distutils LooseVersion.version attribute used by marshmallow
        self.version = list(self._v.release)

    def _cmp(self, other):
        other_v = Version(str(other))
        if self._v < other_v:
            return -1
        if self._v > other_v:
            return 1
        return 0

    def __lt__(self, other):
        return self._cmp(other) < 0

    def __le__(self, other):
        return self._cmp(other) <= 0

    def __eq__(self, other):
        return self._cmp(other) == 0

    def __ne__(self, other):
        return self._cmp(other) != 0

    def __gt__(self, other):
        return self._cmp(other) > 0

    def __ge__(self, other):
        return self._cmp(other) >= 0

    def __str__(self):
        return str(self._v)

