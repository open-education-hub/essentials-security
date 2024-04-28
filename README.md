# Essentials Security

These are open educational resources ([OER](https://en.wikipedia.org/wiki/Open_educational_resources)).
The repository should be used as a template for the your own classes.

## Using the Content

The content is located in the `chapters/` folder.
It currently consists of 4 chapters:

- [Scratch Linux](chapters/scratch-linux/)
- [Demystifying the Web](chapters/demystifying-web/)
- [Data](chapters/data/)
- [Binary Introduction](chapters/binary-introduction/)

Each chapter has its own folder.
Content for each chapter is split in subfolders according to each topic:
Each topic is further split into different kinds of materials that refer to it.
These may be any collection of the following:

- `reading/`: content to be assimilated by learners on their own
- `slides/`: content to be aggregated into presentations
- `drills/`: practical exercises for learners
- `media/`: images, videos, audio or auxiliary materials to be imported in text content
- `demos/`: snippets to be presented by educators
- `guides/`: tutorials for learners with guided steps towards the solution

## Chapter Contents

Lecture content consists of slides and demos.
Slides are written in [GitHub Markdown](https://guides.github.com/features/mastering-markdown/) and use [reveal-md](https://github.com/webpro/reveal-md) and [reveal.js](https://revealjs.com/) to render HTML output.
Lecture slides are built from the `slides.md` file using the `make` command (and the `Makefile`).
Demos are snippets of code and support files that showcase concepts and ideas related to the lecture.
Demos are located in the `demo/` folder.
Each demo has its own folder with source code, `Makefile` or other build files (if required) and support files.

Lab content consists of lab text and lab activities.
Lab text is placed in the `README.md` file.
Each lab activity has its own folder with source code, `Makefile` or other build files (if required) and support files.

## Contributing

Contributions are welcome.
See the [contribution guide](CONTRIBUTING.md) on how you could report or fix issues and on how you can improve the content.

Reviewers are requested to follow the [reviewing guide](REVIEWING.md).
