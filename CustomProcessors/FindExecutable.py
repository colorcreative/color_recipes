#!/usr/bin/env python

import os
from autopkglib import Processor, ProcessorError

__all__ = ["FindExecutable"]

class FindExecutable(Processor):
    description = "Finds the specified executable within the provided path."
    input_variables = {
        "start_path": {
            "required": True,
            "description": "Path to start the search for the executable.",
        },
        "executable_name": {
            "required": True,
            "description": "Name of the executable to search for.",
        },
    }
    output_variables = {
        "found_executable": {
            "description": "The full path to the found executable.",
        },
    }

    def find_executable(self, start_path, executable_name):
        for root, dirs, files in os.walk(start_path):
            if executable_name in files:
                return os.path.join(root, executable_name)
        return None

    def main(self):
        start_path = self.env["start_path"]
        executable_name = self.env["executable_name"]

        found_executable = self.find_executable(start_path, executable_name)
        if found_executable:
            self.output("Found executable at: {}".format(found_executable))
            self.env["found_executable"] = found_executable
        else:
            raise ProcessorError("Unable to find the specified executable: {}".format(executable_name))

if __name__ == "__main__":
    processor = FindExecutable()
    processor.execute_shell()
