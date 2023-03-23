#!/usr/bin/env python3

from autopkglib import Processor, ProcessorError
import subprocess
import os

__all__ = ["RebrandedMunkiPkgCreator"]

class RebrandedMunkiPkgCreator(Processor):
    description = "Creates a rebranded Munki package using Munki Rebrand."
    input_variables = {
        "rebrand_script": {
            "required": True,
            "description": "Path to the Munki Rebrand script.",
        },
        "input_pkg": {
            "required": True,
            "description": "Path to the input Munki package.",
        },
        "icon_file": {
            "required": True,
            "description": "Path to the custom icon file.",
        },
        "executable": {
            "required": True,
            "description": "Path to the Python 3 executable.",
        },
    }
    output_variables = {
        "rebranded_pkg_path": {
            "description": "Path to the rebranded Munki package.",
        },
    }

    def main(self):
        rebrand_script = self.env["rebrand_script"]
        input_pkg = self.env["input_pkg"]
        icon_file = self.env["icon_file"]
        executable = self.env["executable"]

        try:
            self.output(f"Rebranding Munki package: {input_pkg}")
            cmd = [
                executable,
                rebrand_script,
                "--appname",
                "COLOR IT",
                "--pkg",
                input_pkg,
                "--icon-file",
                icon_file,
                "--output-file",
                "COLOR_IT.pkg",
            ]
            subprocess.run(cmd, check=True)

            rebranded_pkg_path = os.path.abspath("COLOR_IT.pkg")
            if os.path.exists(rebranded_pkg_path):
                self.env["rebranded_pkg_path"] = rebranded_pkg_path
                self.output(f"Rebranded package created at {rebranded_pkg_path}")
            else:
                raise ProcessorError("Rebranded package not found")

        except subprocess.CalledProcessError as e:
            raise ProcessorError(f"An error occurred during rebranding: {e}")

if __name__ == "__main__":
    processor = RebrandedMunkiPkgCreator()
    processor.execute_shell()
