from .base import TuyaDevice


class TuyaCover(TuyaDevice):

    def open_cover(self):
        """Open the cover."""
        if self._control_device("turnOnOff", {"value": "1"}):
            self._update_data("state", True)

    def close_cover(self):
        """Close cover."""
        if self._control_device("turnOnOff", {"value": "0"}):
            self._update_data("state", False)

    def stop_cover(self):
        """Stop the cover."""
        if self._control_device("startStop", {"value": "0"}):
            self._update_data("state", False)

    def support_stop(self):
        support = self.data.get("support_stop")
        if support is None:
            return False
        return support

    def update(self):
        return self._update(use_discovery=True)
