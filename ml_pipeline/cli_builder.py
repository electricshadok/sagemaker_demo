import argparse
import inspect


class CLIBuilder:
    def __init__(self, cls, description, **kwargs) -> None:
        self.cls = cls
        self.description = description
        self.kwargs = kwargs

    def create_arg_parser(self):
        parser = argparse.ArgumentParser(description=self.description)

        # Get arguments from the class constructor
        constructor_args = inspect.signature(self.cls.__init__).parameters
        for arg_name, arg_param in constructor_args.items():
            if arg_name == "self":
                continue
            arg_type = arg_param.annotation
            default_value = arg_param.default

            if arg_type == inspect.Parameter.empty:
                raise ValueError(f"Argument '{arg_name}' in {self.cls.__name__} constructor does not have a type annotation.")

            # Get default value
            # Check whether the argument is overidden by kwargs or has a default
            default_value = None
            if arg_param.default != inspect.Parameter.empty:
                default_value = arg_param.default

            if arg_name in self.kwargs:
                default_value = self.kwargs[arg_name]

            # Add default value if available, otherwise argument will be required
            if default_value != inspect.Parameter.empty:
                parser.add_argument(f"--{arg_name}", type=arg_type, default=default_value)
            else:
                parser.add_argument(f"--{arg_name}", type=arg_type)

        return parser

    def show_example_command(self, cmd_filename: str):
        parser = self.create_arg_parser()
        example_args_with_defaults = [
            (arg.dest, arg.default) for arg in parser._actions if arg.default is not None and arg.default != argparse.SUPPRESS
        ]
        example_command = " ".join([f"--{arg_name} {arg_value}" for arg_name, arg_value in example_args_with_defaults])
        print("Example command:")
        print(f"python {cmd_filename} {example_command}")

    def get_cli(self):
        parser = self.create_arg_parser()
        args = parser.parse_args()
        kwargs = vars(args)
        cmd = self.cls(**kwargs)
        return cmd
