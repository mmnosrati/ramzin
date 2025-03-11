import Ramzin
def main():
    """
    Main function to handle command-line interface for steganography tool.
    Parses arguments and executes embedding or extraction based on user input.
    """
    # Create argument parser with a custom description
    parser = Ramzin.argparse.ArgumentParser(
        description="Stealthy Steganography Tool v.1 - Hide your secrets in images!",
        epilog="Created by MohamadMahdi Nosrati (mmnosrati) - https://github.com/mmnosrati - Sneakily hiding messages since 2025!",
        formatter_class=Ramzin.argparse.RawDescriptionHelpFormatter
    )

    # Add arguments with custom help messages
    parser.add_argument(
        "mode",
        choices=["embed", "extract"],
        help="Choose your mission: 'embed' to embedding a message in image, 'extract' to reveal it"
    )
    parser.add_argument(
        "--img",
        required=True,
        help="Your image Path."
    )
    parser.add_argument(
        "--out",
        help="Where to save your output image. Required for embed mode."
    )
    parser.add_argument(
        "--msg",
        help="The secret message you want to hide. Required for embed mode."
    )

    # Parse arguments
    args = parser.parse_args()

    # Handle the logic
    try:
        if args.mode == "embed":
            if not args.out or not args.msg:
                parser.error("For 'embed' mode, --out and --msg are mandatory!")
            Ramzin.embed_message(args.img, args.msg, args.out)
        elif args.mode == "extract":
            extracted_message = Ramzin.extract_message(args.img)
            print(f"Extracted secret: {extracted_message}")
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")


if __name__ == "__main__":
    main()
