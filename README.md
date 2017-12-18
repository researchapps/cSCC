# cSCC

This is the Stanford Squamous Cell Skin Cancer (cSCC) Recurrence Web Prediction Tool.

## Usage

If you want to use the tool, it is deployed at [https://researchapps.github.io/cSCC](https://researchapps.github.io/cSCC). For reproducibility, we also have packaged the tool in a Docker container. If you are familiar with Docker, you can run the container as follows:

```
docker run -d -p 80:80 vanessa/cscc
```

and then open your browser to [http://127.0.0.1](http://127.0.0.1) to see the application.

## Resources

 - [Use the tool](https://researchapps.github.io/cSCC)
 - [Get Help](https://researchapps.github.io/cSCC/issues)
 - [LICENSE](LICENSE)


<img src="docs/img/stanford_medicine.png" style="max-width:100px">

This tool is developed by [@vsoch](https://www.github.com/vsoch) from the [Stanford University Research Computer Center](https://srcc.stanford.edu).


## Development
The static tool is being served from Github pages. The algorithm steps are included in the [docs](docs) folder, and for the implementation see notes in the [index.html](index.html). Calculated values are provided in the javascript console (right click and inspect in the browser) for help with debugging. The Docker image is an automated build on Docker Hub, and can also be built from this repository base as follows:

```
docker build -t vanessa/cscc .
```

If you have any questions or other issues please [open an issue](https://researchapps.github.io/cSCC/issues).
