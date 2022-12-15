import dataclasses
from typing import List, Callable

import extractor
import injector
from utils import error


@dataclasses.dataclass
class Command:
    name: str
    args: List[str]
    description: str
    method: Callable

    def usage(self) -> str:
        return f'{self.name} {" ".join([f"[{arg}]" for arg in self.args])}'

    def execute(self, *p_args) -> None:
        if len(p_args) < len(self.args):
            error(f"missing arguments\nUsage: {self.usage()}")
        elif len(p_args) > len(self.args):
            error(f"too many arguments\nUsage: {self.usage()}")
        self.method(*p_args)


commands = [
    Command(
        'inject',
        ['input.jpg', 'payload.*', 'output.jpg'],
        'Injects the specified payload into the specified JPG',
        injector.inject
    ),
    Command(
        'extract',
        ['injected.jpg', 'extracted_payload.*'],
        'Extracts injected payload from the specified JPG into a separate file',
        extractor.extract
    )
]


def createCommand(name: str) -> Command:
    global commands

    if name == "inject":
        return commands[0]
    elif name == "extract":
        return commands[1]
    else:
        error(f"unknown command {name}")


def docs():
    res = "JPG Injector\n\n"
    res += "by Youssef Atta'i\n"
    res += "https://github.com/youssef-attai\n\n"
    res += "Commands:\n\n"
    for i, command in enumerate(commands):
        res += f"- {command.usage()}\n\n"
        res += f"\t{command.description}" + ("\n\n" if i != len(commands) - 1 else "")
    return res + '\n'
