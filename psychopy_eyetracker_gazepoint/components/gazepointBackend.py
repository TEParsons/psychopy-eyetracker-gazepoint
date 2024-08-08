from psychopy.localization import _translate
from psychopy.experiment import Param
try:
    from psychopy.experiment.components.settings.eyetracking import EyetrackerBackend
except ModuleNotFoundError:
    # EyetrackerBackend didn't exist before 2025.1, so just use the base object class
    EyetrackerBackend = object


class GazepointEyetrackerBackend(EyetrackerBackend):
    label = "GazePoint"
    key = "eyetracker.gazepoint.gp3.EyeTracker"

    @classmethod
    def getParams(cls):
        # define order
        order = [
            "gpAddress",
            "gpPort"
        ]
        # define params
        params = {}
        params['gpAddress'] = Param(
            '127.0.0.1', valType='str', inputType="single",
            hint=_translate("IP Address of the computer running GazePoint Control."),
            label=_translate("GazePoint IP address"), categ="Eyetracking"
        )

        params['gpPort'] = Param(
            4242, valType='num', inputType="single",
            hint=_translate("Port of the GazePoint Control server. Usually 4242."),
            label=_translate("GazePoint port"), categ="Eyetracking"
        )

        return params, order

    @classmethod
    def writeDeviceCode(cls, inits, buff):
        code = (
            "ioConfig[%(eyetracker)s] = {\n"
            "    'name': 'tracker',\n"
            "    'network_settings': {\n"
            "        'ip_address': %(gpAddress)s,\n"
            "        'port': %(gpPort)s,\n"
            "    },\n"
            "}\n"
        )
        buff.writeIndentedLines(code % inits)
