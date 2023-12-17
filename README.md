# YouTube Convertor

The YouTube Video Converter is a user-friendly utility designed to seamlessly convert and download either the audio or video version of content posted on the YouTube website. It operates with the explicit intention of respecting the rights and permissions of the original publishers. The author of this script unequivocally discourages any form of piracy.

Our utility emphasizes responsible usage, ensuring that users only download videos with the explicit consent of the original content creators. It upholds ethical standards, aiming to foster a respectful environment for content consumption.

By using this tool, you are supporting the work of content creators while enjoying the flexibility to access and store your favorite content in a format that suits your preferences. It's our commitment to ethical practices that sets this utility apart, providing users with a reliable and conscientious solution for their video and audio conversion needs.


## Usage

You can either run the code by itself or using the binary from the release

```
python3 youtube_converter.py --youtube_url "URL to the video" --output_path "./landing_zone" --only_audio "y"
```

The code accepts three arguments:

* --youtube_url : The URL of the youtube video that you want to convert
* --output_path : The output where the converted audio or video file gets stored
* --only_audio : This takes either y/n as the input. If you just need audio it ocnverts the video to mp4

## Formatting
This repository uses black for consistent code formatting and flake8 for linting. These tools ensure a unified code style, catch potential issues early, and maintain high-quality code. By enforcing these standards, we promote collaboration, streamline development, and enhance overall code reliability. Automated checks during continuous integration guarantee that contributions align with established coding conventions.

## License

For comprehensive details regarding licensing, please refer to the [LICENSE](./LICENSE) file. This document provides in-depth information about the terms and conditions governing the use of this utility. It is crucial to review and understand these licensing terms to ensure compliance and responsible usage.
