#!/usr/bin/env python

from autopkglib import Processor, ProcessorError
import os
import shutil

__all__ = ["MoveExecutable"]

class MoveExecutable(Processor):
    description = "Moves the specified executable to the desired directory."
    input_variables = {
        "source_path": {
            "required": True,
            "description": "Path to the source executable.",
        },
        "destination_dir": {
            "required": True,
            "description": "Path to the destination directory.",
        },
    }
    output_variables = {}

    def main(self):
        source_path = self.env["source_path"]
        destination_dir = self.env["destination_dir"]

        try:
            shutil.move(source_path, destination_dir)
            self.output("Moved {} to {}.".format(source_path, destination_dir))
        except Exception as e:
            raise ProcessorError("Unable to move executable: {}".format(e))

if __name__ == "__main__":
    processor = MoveExecutable()
    processor.execute_shell()
