from autodoc.app import ViewerApp
from autodoc.cli import PARSER, generate_config


def main():
    args = PARSER.parse_args()
    config = generate_config(f"{args.src_dir}/{args.file}" if args.file else ".autodoc")
    app = ViewerApp(args.src_dir, config)
    app.run()


if __name__ == "__main__":
    main()
